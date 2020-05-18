
NUMA balancing impact on common benchmarks
==========================================


**NUMA balancing can lead to performance degradation on                    NUMA-based arm64 systems when tasks migrate,  
                    and their memory accesses now suffer additional latency.                    NO_WA_IDLE prevents idle CPUs aggressively pull tasks. **
# Platform
  

|System|Information|
| :--- | :--- |
|Architecture|aarch64|
|Processor version|Kunpeng 920-6426|
|CPUs|128|
|NUMA nodes|4|
|Memory (GB)|125|
|Kernel release|5.7.0-rc3+|
|Node name|ARMv2-3|

# Test results

## PerfBenchSchedPipe
  
~~~  
perf bench -f simple sched pipe -l 4000000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|54.369|1,898|0|0|0|0|
|Default-1-0|54.867|2,054|0|0|0|0|
|Default-2-0|55.279|1,996|0|0|0|0|
|NB-OFF-0-0|54.795|1,903|0|0|0|0|
|NB-OFF-1-0|54.462|1,903|0|0|0|0|
|NB-OFF-2-0|53.020|1,814|0|0|0|0|
  

## PerfBenchSchedMessaging
  
~~~  
perf bench -f simple sched messaging -l 30000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|15.416|1,895,534|12|336|327|2,725|
|Default-1-0|12.792|1,915,621|9|228|234|2,605|
|Default-2-0|12.282|1,694,699|12|186|181|2,541|
|NB-OFF-0-0|20.309|2,160,721|0|0|0|0|
|NB-OFF-1-0|12.579|1,909,558|0|0|0|0|
|NB-OFF-2-0|13.901|1,926,374|0|0|0|0|
  

## PerfBenchMemMemset
  
~~~  
perf bench -f simple  mem memset -s 1GB -l 15 -f default  
~~~
|Test|Memory BW (GB/s)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|16.126|1|0|0|0|0|
|Default-1-0|17.518|0|0|0|0|0|
|Default-2-0|17.555|0|0|0|0|0|
|NB-OFF-0-0|16.279|1|0|0|0|0|
|NB-OFF-1-0|16.147|0|0|0|0|0|
|NB-OFF-2-0|16.174|0|0|0|0|0|
  

## PerfBenchFutexWake
  
~~~  
perf bench -f simple futex wake -s -t 10240 -w 1  
~~~
|Test|Time (ms)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0| 185.5735 |60,107|0|0|0|749|
|Default-1-0| 137.1113 |62,493|474|2|0|1,056|
|Default-2-0| 134.9280 |59,499|0|0|0|758|
|NB-OFF-0-0| 152.3028 |64,220|0|0|0|0|
|NB-OFF-1-0| 161.8319 |57,677|0|0|0|0|
|NB-OFF-2-0| 172.1630 |57,157|0|0|0|0|
  

## SysBenchCpu
  
~~~  
sysbench cpu --time=60 --threads=64 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|214576.66|81|127|12|140|190|
|Default-1-0|214385.26|65|90|13|124|406|
|Default-2-0|214741.23|71|106|20|136|151|
|NB-OFF-0-0|214400.39|63|0|0|0|0|
|NB-OFF-1-0|214558.53|54|0|0|0|0|
|NB-OFF-2-0|214543.19|49|0|0|0|0|
  

## SysBenchMemory
  
~~~  
sysbench memory --time=60 --memory-access-mode=rnd --threads=64 run  
~~~
|Test|Memory BW (MB/s)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|10240.000|57|80|20|107|134|
|Default-1-0|10240.000|67|101|16|83|335|
|Default-2-0|10135.526|64|81|21|139|172|
|NB-OFF-0-0|10240.000|61|0|0|0|0|
|NB-OFF-1-0|10240.000|32|0|0|0|0|
|NB-OFF-2-0|9636.294|63|0|0|0|0|
  

## SysBenchThreads
  
~~~  
sysbench threads --time=60 --threads=64 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|24413.300|33,015|126|118|122|135|
|Default-1-0|22437.900|13,336|92|108|109|138|
|Default-2-0|24963.300|37,593|93|96|102|196|
|NB-OFF-0-0|23788.500|22,077|0|0|0|0|
|NB-OFF-1-0|23803.800|25,168|0|0|0|0|
|NB-OFF-2-0|22778.300|24,595|0|0|0|0|
  

## SysBenchMutex
  
~~~  
sysbench mutex --mutex-num=1 --threads=512 run  
~~~
|Test|Time (sec)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|34.0815|466,612|32|128|265|1,619|
|Default-1-0|33.4145|422,058|14|125|294|1,399|
|Default-2-0|31.8836|385,117|24|140|277|1,764|
|NB-OFF-0-0|32.9263|384,145|0|0|0|0|
|NB-OFF-1-0|33.5658|445,599|0|0|0|0|
|NB-OFF-2-0|36.0034|440,887|0|0|0|0|
  

## HackbenchForkSockets
  
~~~  
hackbench --loops 20000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|12.301|1,356,421|12|221|252|2,817|
|Default-1-0|9.198|1,306,309|8|185|118|2,171|
|Default-2-0|11.604|1,333,668|29|197|220|2,634|
|NB-OFF-0-0|9.414|1,182,795|0|0|0|0|
|NB-OFF-1-0|8.343|1,135,907|0|0|0|0|
|NB-OFF-2-0|10.311|1,278,446|0|0|0|0|
  

## HackbenchPipeThreads
  
~~~  
hackbench --pipe --threads --loops 20000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|4.939|3,059,700|40|93|35|347|
|Default-1-0|4.965|3,035,160|38|117|11|365|
|Default-2-0|5.250|2,747,928|73|134|29|343|
|NB-OFF-0-0|5.596|2,962,508|0|0|0|0|
|NB-OFF-1-0|5.105|2,790,556|0|0|0|0|
|NB-OFF-2-0|4.967|2,992,430|0|0|0|0|
  

## HackbenchPipeThreads4k
  
~~~  
hackbench --pipe --threads --loops 20000 --datasize 4096  
~~~
|Test|Time (sec)|sched:sched_migrate_task|sched:sched_stick_numa|sched:sched_move_numa|sched:sched_swap_numa|migrate:mm_migrate_pages|
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
|Default-0-0|20.372|7,699,239|48|168|204|901|
|Default-1-0|20.607|7,452,384|35|178|208|932|
|Default-2-0|25.037|7,325,021|95|382|396|1,107|
|NB-OFF-0-0|21.535|7,175,752|0|0|0|0|
|NB-OFF-1-0|24.839|7,473,639|0|0|0|0|
|NB-OFF-2-0|21.601|7,278,702|0|0|0|0|
  
