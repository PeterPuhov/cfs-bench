from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry


@test_registry.register_test
class SysBenchCpu(TestCase):
    def __init__(self, target: Target):
        threads = int(target.n_cpus() / 2)
        command = 'sysbench cpu --time=10 --threads={} --cpu-max-prime=10000 run'.format(threads)
        super().__init__(command)

    def unit(self):
        return "Events/sec"

    def parse_result(self, result: str):
        token = "events per second:"
        for line in result.splitlines():
            if token in line:
                res = line.split(token)
                return res[1].replace(' ', '')

        super.parse_result(result)


@test_registry.register_test
class SysBenchMemory(TestCase):
    def __init__(self, target: Target):
        threads = int(target.n_cpus() / 2)
        command = 'sysbench memory --memory-access-mode=rnd --threads={} run'.format(threads)
        super().__init__(command)

    def unit(self):
        return "MB/s"

    def parse_result(self, result: str):
        token = "total number of events:"
        for line in result.splitlines():
            if token in line:
                res = line.split(token)
                return str(int(int(res[1].replace(' ', '')) / (10 * 1024)))

        super.parse_result(result)


@test_registry.register_test
class SysBenchThreads(TestCase):
    def __init__(self, target: Target):
        threads = int(target.n_cpus() / 2)
        command = 'sysbench threads --threads={} run'.format(threads)
        super().__init__(command)

    def unit(self):
        return "Events/sec"

    def parse_result(self, result: str):
        token = "total number of events:"
        for line in result.splitlines():
            if token in line:
                res = line.split(token)
                return str(int(int(res[1].replace(' ', '')) / 10))

        super.parse_result(result)


@test_registry.register_test
class SysBenchMutex(TestCase):
    def __init__(self, target: Target):
        threads = int(target.n_cpus() * 4)
        command = 'sysbench mutex --mutex-num=1 --threads={} run'.format(threads)
        super().__init__(command)

    def unit(self):
        return "Sec"

    def parse_result(self, result: str):
        token = "total time:"
        for line in result.splitlines():
            if token in line:
                res = line.split(token)
                return res[1].replace(' ', '').replace('s', '')

        super.parse_result(result)
