from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry
import re


@test_registry.register_test
class PerfBenchSchedPipe(TestCase):
    def __init__(self, target: Target, **kwargs):
        super().__init__('perf bench -f simple sched pipe -l 4000000')

    def parse_result(self, result: str):
        res = result.splitlines()[0]
        return {'Time (sec)': res}

@test_registry.register_test
class PerfBenchSchedMessaging(TestCase):
    def __init__(self, target: Target, **kwargs):
        l = 500
        if 'time' in kwargs.keys():
            l = l * kwargs['time']
        super().__init__('perf bench -f simple sched messaging -l {}'.format(l))

    def parse_result(self, result: str):
        res = result.splitlines()[0]
        return {'Time (sec)': res}

@test_registry.register_test
class PerfBenchMemMemset(TestCase):
    def __init__(self, target: Target, **kwargs):
        mem = max(1, int(target.platform['Memory (GB)'] / target.platform['CPUs']))
        test_cmd = 'perf bench -f simple  mem memset -s {}GB -l 15 -f default'.format(mem)
        super().__init__(test_cmd)

    def parse_result(self, result: str):
        delimiters = "\n"
        regexPattern = '|'.join(map(re.escape, delimiters))
        r = re.split(regexPattern, result)[1]
        res = "{:.3f}".format(float(r) / (1 << 30))
        return {'Memory BW (GB/s)': res}

@test_registry.register_test
class PerfBenchFutexWake(TestCase):
    def __init__(self, target: Target, **kwargs):
        t = target.platform['CPUs'] * 8 * 10
        super().__init__('perf bench -f simple futex wake -s -t {} -w 1'.format(t))

    def parse_result(self, result: str):
        delimiters = "threads in", "ms"
        regexPattern = '|'.join(map(re.escape, delimiters))
        t = re.split(regexPattern, result)[1]

        return {'Time (ms)': t }
