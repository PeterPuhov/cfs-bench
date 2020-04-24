from src.results import Results
from src.target import Target
from src.report import *
import tests.perf_bench_sched
import tests.sysbench
import src.test_registry as test_registry


def run_tests(test_name, target, tests_to_run):
    test_results = Results(target)
    for test in test_registry.test_registry:
        if not tests_to_run or test(target).__class__.__name__ in tests_to_run:
            test(target).run(target, test_results)

    return test_results.store(test_name)


def main():
    target = Target()
    res_files = []

    tests_to_run = []

    target.execute('sysctl kernel.numa_balancing=1', as_root=True)
    res_files.append(run_tests(test_name='numa_balancing-ON', target=target, tests_to_run=tests_to_run))

    target.execute('sysctl kernel.numa_balancing=0', as_root=True)
    res_files.append(run_tests(test_name='numa_balancing-OFF', target=target, tests_to_run=tests_to_run))

    title = "NUMA balancing impact on common benchmarks"
    description = "NUMA balancing can lead to performance degradation on \
                   NUMA-based arm64 systems when tasks migrate,  \n \
                   and their memory accesses now suffer additional latency."

    create_report(res_files, 'results/numa-balancing', title=title, description= description)


main()
print("Done")
