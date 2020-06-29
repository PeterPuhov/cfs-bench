import time
from src.results import Results
from src.target import Target
from src.report import *
import tests.perf_bench_sched
import tests.sysbench
import tests.hackbench
import src.test_registry as test_registry


def run_tests(test_name, target, tests_to_run, iter = 0):
    test_results = Results(target)

    test_time = 60
    event = []
    for test in test_registry.test_registry:
        if not tests_to_run or test(target).__class__.__name__ in tests_to_run:
            t =  test(target, time=test_time)
            time.sleep(1)
            t.run(target, test_results)

    return test_results.store(test_name, iteration=iter)

def run_single_test(result_name, test_name, target, res_files, iter = 1):
    test_results = Results(target)

    test_time = 60
    event = []
    for test in test_registry.test_registry:
        if test(target).__class__.__name__ == test_name:
            for i in range(0, iter):
                t =  test(target, time=test_time)
                time.sleep(1)
                t.run(target, test_results)

    f = test_results.store(result_name + '-' + test_name, iteration=0)
    res_files.append(f)    

def main():
    target = Target()
    res_files = []

    # tests_to_run = ['SysBenchMutex', 'SysBenchThreads', 'SysBenchMemory', 'SysBenchCpu']
    tests_to_run = ['SysBenchThreads', 'HackbenchForkSockets', 'SysBenchMutex', 'PerfBenchFutexWake']
    #tests_to_run = ['SysBenchThreads']
    iter = 3

    target.execute('sysctl kernel.sched_check_group_util=0', as_root=True)
    time.sleep(5)
    result_name='BASELINE'
    for test in test_registry.test_registry:
        test_name = test(target).__class__.__name__
        if not tests_to_run or test_name in tests_to_run:
            run_single_test(result_name, test_name, target, res_files, iter)

    target.execute('sysctl kernel.sched_check_group_util=1', as_root=True)
    time.sleep(5)
    result_name='PATCH'
    for test in test_registry.test_registry:
        test_name = test(target).__class__.__name__
        if not tests_to_run or test_name in tests_to_run:
            run_single_test(result_name, test_name, target, res_files, iter)

    title = "Usage of group_util in update_pick_idlest() impact on common benchmarks"
    description = "In update_pick_idlest() function \
                   When both groups have 'group_has_spare' type \
                   and the same number of idle CPU's. \
                   We suggest evaluating group_util to find idlest group. "

    #create_report(res_files, 'results/group_util', title=title, description= description)
    #create_patch(res_files, 'results/group_util', title=title, description= description)
    create_patch_loop(res_files, 'results/group_util', title=title, description= description)


main()
print("Done")
