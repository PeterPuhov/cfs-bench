import subprocess
import re


class Target(object):
    def __init__(self):
        self.platform = {}
        self.platform['Architecture'] = self.execute('uname -m').rstrip()
        self.platform['Processor version'] = self.execute('dmidecode  -s processor-version', as_root=True).splitlines()[0]
        self.platform['CPUs'] = self.number_of_cpus()
        self.platform['NUMA nodes'] = self.number_of_nodes()
        self.platform['Memory (GB)'] = self.memory()
        self.platform['Kernel release'] = self.execute('uname -r').rstrip()
        self.platform['Node name'] = self.execute('uname -n').rstrip()
        

    def n_cpus(self):
        return self.platform['CPUs']

    def n_nodes(self):
        return self.platform['NUMA nodes']

    def number_of_cpus(self):
        num_cpus = 0
        corere = re.compile(r'^\s*cpu\d+\s*$')
        output = self.execute('ls /sys/devices/system/cpu')
        for entry in output.split():
            if corere.match(entry):
                num_cpus += 1
        return num_cpus

    def number_of_nodes(self):
        num_nodes = 0
        nodere = re.compile(r'^\s*node\d+\s*$')
        output = self.execute('ls /sys/devices/system/node')
        for entry in output.split():
            if nodere.match(entry):
                num_nodes += 1
        return num_nodes

    def memory(self):
        res = self.execute('free -g')        
        mem = 0
        for l in res.splitlines():
            if 'Mem:' in l:
                mem = ' '.join(l.split()).split()[1]
                break
        return int(mem)

    def execute(self, command, check=False, as_root=True):
        if as_root:
            command = 'sudo ' + command
        p = subprocess.run(command, shell=True, check=check, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)        
        return p.stdout