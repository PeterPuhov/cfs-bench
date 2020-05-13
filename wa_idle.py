import time
from src.results import Results
from src.target import Target
from src.report import *
import tests.perf_bench_sched
import tests.sysbench
import src.test_registry as test_registry


def run_tests(test_name, target, tests_to_run):
    test_results = Results(target)
    sched_features = target.execute('cat /sys/kernel/debug/sched_features | grep WA_ ', as_root=True)
    for f in sched_features.split(" "):
        if "WA_" in f:
            test_results.log(f)

    for test in test_registry.test_registry:
        if not tests_to_run or test(target).__class__.__name__ in tests_to_run:
            test(target).run_event(target, 'sched:sched_migrate_task', test_results)

    return test_results.store(test_name)


def main():
    target = Target()
    res_files = []

    tests_to_run = []
    iter = 3

    target.execute('sysctl kernel.numa_balancing=1', as_root=True)
    target.execute("bash -c 'echo WA_WEIGHT > /sys/kernel/debug/sched_features'", as_root=True)
    target.execute("bash -c 'echo WA_IDLE > /sys/kernel/debug/sched_features'", as_root=True)    
    for i in range(iter):
        time.sleep(10)
        res_files.append(run_tests(test_name='Default-{}'.format(i), target=target, tests_to_run=tests_to_run))

    target.execute('sysctl kernel.numa_balancing=0', as_root=True)
    for i in range(iter):
        time.sleep(10)
        res_files.append(run_tests(test_name='NB-OFF-{}'.format(i), target=target, tests_to_run=tests_to_run))

    target.execute('sysctl kernel.numa_balancing=0', as_root=True)
    target.execute("bash -c 'echo NO_WA_WEIGHT > /sys/kernel/debug/sched_features'", as_root=True)
    target.execute("bash -c 'echo NO_WA_IDLE > /sys/kernel/debug/sched_features'", as_root=True)
    for i in range(iter):
        time.sleep(10)
        res_files.append(run_tests(test_name='NB-OFF_NO_WA_IDLE-{}'.format(i), target=target, tests_to_run=tests_to_run))

    title = "NUMA balancing impact on common benchmarks"
    description = "NUMA balancing can lead to performance degradation on \
                   NUMA-based arm64 systems when tasks migrate,  \n \
                   and their memory accesses now suffer additional latency. \
                   NO_WA_IDLE prevents idle CPUs aggressively pull tasks. "

    create_report(res_files, 'results/wa_idle', title=title, description= description)


main()
print("Done")
