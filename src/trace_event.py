import subprocess
import os
from src.target import Target

class TraceEvent(object):
    def __init__(self, target: Target, command, events=None, output=None):
        self.target = target
        
        cmd = "bash -c 'echo event-fork > /sys/kernel/debug/tracing/trace_options'"
        target.execute(cmd)

        cmd = "bash -c 'echo 0 > /sys/kernel/debug/tracing/tracing_on'"
        print(cmd)
        target.execute(cmd)
         
        self.enable_events(events)

        if output is None:
            output = "trace_pipe.txt"
        
        cmd = "cat /sys/kernel/debug/tracing/trace_pipe > {}".format(output)
        proc = subprocess.Popen("sudo bash -c '{}'".format(cmd), shell=True)

        cmd = "sh -c 'echo $$ > /sys/kernel/debug/tracing/set_event_pid; echo 1 > /sys/kernel/debug/tracing/tracing_on; {}'".format(command)
        print(cmd)        
        self.results = target.execute(cmd)

        cmd = "bash -c 'echo 0 > /sys/kernel/debug/tracing/tracing_on'"
        print(cmd)
        target.execute(cmd)

        proc.kill()
        proc.wait()        

        self.disable_events(events)

    def enable_events(self, events: list):
        path = '/sys/kernel/debug/tracing/events/sched'
        for e in events:
            cmd = "bash -c 'echo 1 > {}'".format(os.path.join(path,e,"enable"))
            print(cmd)
            self.target.execute(cmd)

    def disable_events(self, events: list):
        path = '/sys/kernel/debug/tracing/events/sched'
        for e in events:
            cmd = "bash -c 'echo 0 > {}'".format(os.path.join(path,e,"enable"))            
            self.target.execute(cmd)
