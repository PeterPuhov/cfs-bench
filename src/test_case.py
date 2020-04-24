from src.target import Target
from src.results import Results


class TestCase(object):
    def __init__(self, command):
        self.command = command
        # self.test_name = None

    def run(self, target: Target, results: Results):
        results.log('Running [ {} ] ...'.format(self.command))
        test_result = {}
        test_result['command'] = self.command
        test_result['result'] = self.parse_result(target.execute(self.command))
        test_result['unit'] = self.unit()
        results.add_test_result(self.__class__.__name__, test_result)
        results.log('Done.')

    def unit(self):
        return ""

    def parse_result(self, result: str):
        return result
