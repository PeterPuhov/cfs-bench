from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry


@test_registry.register_test
class SysBenchCpu(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() / 2)
        command = 'sysbench cpu --time=60 --threads={} --cpu-max-prime=10000 run'.format(threads)
        super().__init__(command)

    def parse_result(self, result: str):
        token = "events per second:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = line.split(token)[1].replace(' ', '')
                break
        
        return {'Events/sec': res}


@test_registry.register_test
class SysBenchMemory(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() / 2)
        command = 'sysbench memory --time=60 --memory-access-mode=rnd --threads={} run'.format(threads)
        super().__init__(command)

    def parse_result(self, result: str):
        token = "total number of events:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = line.split(token)[1].replace(' ', '')
                res = "{:.3f}".format(int(res) / (10 * 1024))
                break
                
        return {'Memory BW (MB/s)': res}


@test_registry.register_test
class SysBenchThreads(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() / 2)
        command = 'sysbench threads --time=60 --threads={} run'.format(threads)
        super().__init__(command)

    def parse_result(self, result: str):
        token = "total number of events:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = int(line.split(token)[1].replace(' ', '')) / 10
                res = "{:.3f}".format(res)
                break

        return {'Events/sec': res}


@test_registry.register_test
class SysBenchMutex(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() * 4)
        command = 'sysbench mutex --mutex-num=1 --threads={} run'.format(threads)
        super().__init__(command)

    def parse_result(self, result: str):
        token = "total time:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = line.split(token)[1].replace(' ', '').replace('s', '')
                break

        return {'Time (sec)': res}
