from src.results import Results
from src.target import Target
import tests.perf_bench_sched
import tests.sysbench
import src.test_registry as test_registry


def main():
    target = Target()
    test_results = Results(target)

    # tests_to_run = ['SysBenchCpu', 'SysBenchMemory']
    tests_to_run = ['SysBenchMutex']
    for test in test_registry.test_registry:
        if not tests_to_run or test(target).__class__.__name__ in tests_to_run:
            test(target).run(target, test_results)

    test_results.store()


main()
print("Done")
