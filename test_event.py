import time
from src.trace_event import TraceEvent
from src.target import Target

target = Target()

# events = ['sched_wakeup_new', 'sched_wakeup', 'sched_migrate_task', 'sched_move_numa']
# events = ['sched_move_numa', 'sched_preferred_nid', 'sched_numa_faults', 'sched_numa_stats']
events = ['sched_wakeup_new']
# cmd = "perf bench mem memset -s 1536MB -l 10 -f default"
# cmd = "perf bench -f simple futex wake -s -t 32 -w 1"
cmd = "sysbench threads --threads=8 run"

target.execute('sysctl kernel.sched_check_group_util=0', as_root=True)
te = TraceEvent(target, cmd, events=events, output="sched_check_group_util_0.txt")
print(te.results)

time.sleep(5)

target.execute('sysctl kernel.sched_check_group_util=1', as_root=True)
te = TraceEvent(target, cmd, events=events, output="sched_check_group_util_1.txt")
print(te.results)
