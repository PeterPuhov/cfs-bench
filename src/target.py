import subprocess
import re


class Target(object):
    def __init__(self):
        self.platform = {}
        self.platform['nodename'] = self.execute('uname -n')
        self.platform['kernel_release'] = self.execute('uname -r')
        self.platform['number_of_cpus'] = self.number_of_cpus()

    def number_of_cpus(self):
        num_cpus = 0
        corere = re.compile(r'^\s*cpu\d+\s*$')
        output = self.execute('ls /sys/devices/system/cpu', as_root=False)
        for entry in output.split():
            if corere.match(entry):
                num_cpus += 1
        return num_cpus

    def execute(self, command, check=False, as_root=False):
        if as_root:
            command = 'sudo ' + command
        p = subprocess.run(command, shell=True, check=check, stdout=subprocess.PIPE, universal_newlines=True)
        return p.stdout
