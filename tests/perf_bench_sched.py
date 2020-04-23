from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry
import re


@test_registry.register_test
class PerfBenchSchedPipe(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple sched pipe')


@test_registry.register_test
class PerfBenchSchedMessaging(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple sched messaging -l 10000')


@test_registry.register_test
class PerfBenchMemMemset(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple  mem memset -s 4GB -l 5 -f default')

    def get_result(self, result: str):
        res = result.split('\n')
        return res[1]

    def parse_result(self, result: str):
        delimiters = "\n"
        regexPattern = '|'.join(map(re.escape, delimiters))
        res = re.split(regexPattern, result)
        return res[1]


@test_registry.register_test
class PerfBenchFutexWake(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple futex wake -s -t 1024 -w 1')

    def parse_result(self, result: str):
        delimiters = "threads in", "ms"
        regexPattern = '|'.join(map(re.escape, delimiters))
        res = re.split(regexPattern, result)
        return res[1]
