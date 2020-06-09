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
            time.sleep(10)
            t.run(target, test_results)

    return test_results.store(test_name, iteration=iter)


def main():
    target = Target()
    res_files = []

    tests_to_run = ['SysBenchMutex', 'SysBenchThreads', 'SysBenchMemory', 'SysBenchCpu']
    iter = 5    
    for batch in range(0,4):
        target.execute('sysctl kernel.sched_check_group_util=0', as_root=True)
        for i in range(iter):        
            res_files.append(run_tests(test_name='Default_{}'.format(batch), target=target, tests_to_run=tests_to_run, iter=i))

        target.execute('sysctl kernel.sched_check_group_util=1', as_root=True)
        for i in range(iter):        
            res_files.append(run_tests(test_name='group_util_{}'.format(batch), target=target, tests_to_run=tests_to_run, iter=i))

    title = "Usage of group_util in update_pick_idlest() impact on common benchmarks"
    description = "In update_pick_idlest() function \
                   When both groups have 'group_has_spare' type \
                   and the same number of idle CPU's. \
                   We suggest evaluating group_util to find idlest group. "

    create_report(res_files, 'results/group_util', title=title, description= description)


main()
print("Done")
