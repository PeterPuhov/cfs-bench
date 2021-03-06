from src.target import Target
from src.results import Results


class TestCase(object):
    def __init__(self, command):
        self.command = command
        # self.test_name = None

    # sudo perf stat -e sched:sched_migrate_task --  perf bench -f simple futex wake -s -t 1024 -w 1
    def run(self, target: Target, results: Results):
        results.log('Running [ {} ] ...'.format(self.command))
        test_result = {}
        test_result['command'] = self.command
        #test_result['result'] = self.parse_result(target.execute(self.command))        
        res = target.execute(self.command)
        pr = self.parse_result(res)
        test_result['result'] = pr
        test_result['raw_result'] = float(next(iter(pr.values())))
         
        results.add_test_result(self.__class__.__name__, test_result)
        results.log('Done.')

    def run_event(self, target: Target, events: [], results: Results):
        results.log('Running [ {} ] ...'.format(self.command))
        test_result = {}        
        test_result['command'] = self.command        
        cmd = 'perf stat'
        for e in events:
            cmd += " -e {} ".format(e)

        cmd += " {}".format(self.command)
        res = target.execute(cmd)
        pr = self.parse_result(res)        
        test_result['result'] = pr
        test_result['raw_result'] = float(next(iter(pr.values())))
        for e in events:
            test_result['result'].update(self.parse_event(e, res))

        results.add_test_result(self.__class__.__name__, test_result)
        results.log('Done.')

    def parse_event(self, event: str, result: str):
        count = "0"
        for l in result.splitlines():
            if event in l:
                count = l.replace(" ", "").split(event)[0]
                break

        return {event: count}