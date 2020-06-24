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

    for test in test_registry.test_registry:
        t =  test(target, time=60)            
        print(t.command)

main()
print("Done")
