from src.results import Results
from src.target import Target
from src.report import *
import tests.perf_bench_sched
import tests.sysbench
import tests.hackbench
import src.test_registry as test_registry


def main():
    target = Target()
    test_results = Results(target)

    test_results.log(target.execute('cat /sys/kernel/debug/sched_features | grep _WA_ ', as_root=True))

    tests_to_run = []
    # tests_to_run = ['SysBenchCpu', 'SysBenchMemory']
    tests_to_run = ['HackbenchForkSockets', 'HackbenchPipeThreads', 'HackbenchPipeThreads4k']
    for test in test_registry.test_registry:
        if not tests_to_run or test(target).__class__.__name__ in tests_to_run:
            test(target).run_event(target, 'sched:sched_migrate_task', test_results)

    res_files = []
    res_files.append(test_results.store('Res1'))
    res_files.append(test_results.store('Res2'))

    create_report(res_files, 'Report', 'Test Run')
main()
print("Done")
