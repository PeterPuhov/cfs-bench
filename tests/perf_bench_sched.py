from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry
import re


@test_registry.register_test
class PerfBenchSchedPipe(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple sched pipe')

    def unit(self):
        return "usecs/op"

    def parse_result(self, result: str):
        return result.rstrip('\n')

@test_registry.register_test
class PerfBenchSchedMessaging(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple sched messaging -l 10000')

    def unit(self):
        return "Sec"

    def parse_result(self, result: str):
        return result.rstrip('\n')

@test_registry.register_test
class PerfBenchMemMemset(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple  mem memset -s 4GB -l 5 -f default')

    def unit(self):
        return "GB/sec"

    def parse_result(self, result: str):
        delimiters = "\n"
        regexPattern = '|'.join(map(re.escape, delimiters))
        res = re.split(regexPattern, result)
        return str(float(res[1]) / (1 << 30))


@test_registry.register_test
class PerfBenchFutexWake(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple futex wake -s -t 1024 -w 1')

    def unit(self):
        return "ms"

    def parse_result(self, result: str):
        delimiters = "threads in", "ms"
        regexPattern = '|'.join(map(re.escape, delimiters))
        res = re.split(regexPattern, result)
        return res[1]
