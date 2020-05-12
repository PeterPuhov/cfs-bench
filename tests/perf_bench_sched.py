from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry
import re


@test_registry.register_test
class PerfBenchSchedPipe(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple sched pipe')

    def parse_result(self, result: str):
        res = result.splitlines()[0]
        return {'Time (sec)': res}

@test_registry.register_test
class PerfBenchSchedMessaging(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple sched messaging -l 10000')

    def parse_result(self, result: str):
        res = result.splitlines()[0]
        return {'Time (sec)': res}

@test_registry.register_test
class PerfBenchMemMemset(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple  mem memset -s 1GB -l 5 -f default')

    def parse_result(self, result: str):
        delimiters = "\n"
        regexPattern = '|'.join(map(re.escape, delimiters))
        r = re.split(regexPattern, result)[1]
        res = "{:.3f}".format(float(r) / (1 << 30))
        return {'Memory BW (GB/s)': res}

@test_registry.register_test
class PerfBenchFutexWake(TestCase):
    def __init__(self, target: Target):
        super().__init__('perf bench -f simple futex wake -s -t 1024 -w 1')

    def parse_result(self, result: str):
        delimiters = "threads in", "ms"
        regexPattern = '|'.join(map(re.escape, delimiters))
        t = re.split(regexPattern, result)[1]

        return {'Time (ms)': t }
