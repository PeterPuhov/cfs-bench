import json
from datetime import datetime
from src.target import Target


class Results(object):
    def __init__(self, target: Target):
        self.start_time = datetime.now()
        self.raw_data = []
        self.log_data = []
        self.test_results = {}
        self.test_results['platform'] = target.platform
        self.test_results['tests'] = {}

    def log(self, data: str):
        entry = datetime.now().strftime("%H:%M:%S") + " " + data
        print(entry)
        self.log_data.append(entry)

    def store(self, name=None, iteration = 0):
        if name is not None:
            fname = "{}-{}.json".format(name, iteration)
        else:
            fname = "Test-{}.json".format(datetime.now().strftime("%H:%M:%S"))

        self.test_results['name'] = fname.replace('.json','')
        self.test_results['iteration'] = str(iteration)
        with open(fname, 'w') as outfile:
            json.dump(self.test_results, outfile, indent=2)
        print("Results stored in {}".format(fname))
        return fname

    def add_test_result(self, test, test_result: dict):
        self.test_results['tests'][test] = test_result
