import time
import gc
from src.results import Results
from src.target import Target
from src.report import *
import tests.perf_bench_sched
import tests.sysbench
import tests.hackbench
import src.test_registry as test_registry


def run_tests(test_name, target, tests_to_run, iter = 0):
    test_results = Results(target)

    time = 60
    event = []
    for test in test_registry.test_registry:
        if not tests_to_run or test(target).__class__.__name__ in tests_to_run:
            t =  test(target, time=time)
            t.run(target, test_results)

    return test_results.store(test_name, iteration=iter)


def main():
    target = Target()
    res_files = []

    tests_to_run = ['SysBenchMutex', 'SysBenchThreads', 'SysBenchMemory', 'SysBenchCpu', 'PerfBenchMemMemset']
    iter = 5   
    test_delay = 2
        
    target.execute('sysctl kernel.sched_enable_task_numa_init=0', as_root=True)
    for i in range(iter):
        gc.collect()
        time.sleep(test_delay)
        res_files.append(run_tests(test_name='Default', target=target, tests_to_run=tests_to_run, iter=i))

    target.execute('sysctl kernel.sched_enable_task_numa_init=0', as_root=True)
    for i in range(iter):
        gc.collect()
        time.sleep(test_delay)
        res_files.append(run_tests(test_name='numa_init', target=target, tests_to_run=tests_to_run, iter=i))


    target.execute('sysctl kernel.sched_enable_task_numa_init=0', as_root=True)
    for i in range(iter):
        gc.collect()
        time.sleep(test_delay)
        res_files.append(run_tests(test_name='Default_1', target=target, tests_to_run=tests_to_run, iter=i))

    target.execute('sysctl kernel.sched_enable_task_numa_init=0', as_root=True)
    for i in range(iter):
        gc.collect()
        time.sleep(test_delay)
        res_files.append(run_tests(test_name='numa_init_1', target=target, tests_to_run=tests_to_run, iter=i))


    title = "Impact of setting numa_preferred_nid during wakeup_new phase on common benchmarks"
    description = "In update_pick_idlest() function \
                   When both groups have 'group_has_spare' type \
                   and the same number of idle CPU's. \
                   We suggest evaluating group_util to find idlest group. "

    create_report(res_files, 'results/numa_init', title=title, description= description)


main()
print("Done")
