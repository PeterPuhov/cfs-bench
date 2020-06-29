from src.test_case import TestCase
from src.target import Target
import src.test_registry as test_registry


@test_registry.register_test
class HackbenchForkSockets(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() / 2)
        command = 'hackbench --loops 20000'
        super().__init__(command)

    def parse_result(self, result: str):
        token = "Time:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = line.split(token)[1].replace(' ', '')
                break
        
        return {'Time (sec)': res, 'HIB': False}

@test_registry.register_test
class HackbenchPipeThreads(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() / 2)
        command = 'hackbench --pipe --threads --loops 20000'
        super().__init__(command)

    def parse_result(self, result: str):
        token = "Time:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = line.split(token)[1].replace(' ', '')
                break
        
        return {'Time (sec)': res, 'HIB': False}

@test_registry.register_test
class HackbenchPipeThreads4k(TestCase):
    def __init__(self, target: Target, **kwargs):
        threads = int(target.n_cpus() / 2)
        command = 'hackbench --pipe --threads --loops 20000 --datasize 4096'
        super().__init__(command)

    def parse_result(self, result: str):
        token = "Time:"
        res = result
        for line in result.splitlines():
            if token in line:
                res = line.split(token)[1].replace(' ', '')
                break
        
        return {'Time (sec)': res, 'HIB': False}
