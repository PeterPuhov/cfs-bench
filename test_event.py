from src.trace_event import TraceEvent
from src.target import Target

target = Target()
# events = ['sched_wakeup_new', 'sched_wakeup', 'sched_migrate_task', 'sched_move_numa']
events = ['sched_move_numa']
cmd = "perf bench mem memset -s 2GB -l 100 -f default"
te = TraceEvent(target, cmd, events)
print(te.results)
