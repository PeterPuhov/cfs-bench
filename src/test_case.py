from src.target import Target
from src.results import Results


class TestCase(object):
    def __init__(self, command):
        self.command = command
        self.test_name = None

    def run(self, target: Target, results: Results):
        results.log('Running [ {} ] ...'.format(self.command))
        test_result = {}
        test_result['command'] = self.command
        test_result['result'] = self.parse_result(target.execute(self.command))
        results.add_test_result(self.__class__.__name__, test_result)
        results.log('Done.')

    def parse_result(self, result: str):
        return result

    def install(self, target: Target, dependencies: str):
        for d in dependencies:
            target.execute('DEBIAN_FRONTEND=noninteractive {}'.format(d), as_root=True)
