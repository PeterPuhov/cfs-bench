
NUMA balancing impact on common benchmarks
==========================================


**NUMA balancing can lead to performance degradation on NUMA-based arm64 systems when tasks migrate,and their memory accesses now suffer additional latency.  
NO_WA_IDLE prevents idle CPUs aggressively pull tasks. **

# Platform
  

|System|Information|
| :--- | :--- |
|Architecture|aarch64|
|Processor version|Kunpeng 920-6426|
|CPUs|128|
|NUMA nodes|4|
|Kernel release|5.7.0-rc3+|
|Node name|ARMv2-3|

# Test results

## PerfBenchSchedPipe
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched pipe -l 4000000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|49.934|1,703|
|Default-1|48.809|1,544|
|Default-2|47.600|1,358|
|NB-OFF-0|49.575|1,682|
|NB-OFF-1|49.865|1,731|
|NB-OFF-2|50.126|1,810|
|NB-OFF_NO_WA_IDLE-0|63.215|0|
|NB-OFF_NO_WA_IDLE-1|64.077|0|
|NB-OFF_NO_WA_IDLE-2|44.903|0|


<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>


## PerfBenchSchedMessaging
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched messaging -l 100000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|57.716|6,507,533|
|Default-1|45.206|5,642,778|
|Default-2|64.176|7,095,030|
|NB-OFF-0|48.855|6,331,755|
|NB-OFF-1|46.853|6,273,548|
|NB-OFF-2|34.420|5,382,656|
|NB-OFF_NO_WA_IDLE-0|36.347|46|
|NB-OFF_NO_WA_IDLE-1|36.659|29|
|NB-OFF_NO_WA_IDLE-2|41.381|38|
  

## PerfBenchMemMemset
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple  mem memset -s 32GB -l 15 -f default  
~~~
|Test|Memory BW (GB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|7.164|1|
|Default-1|6.998|3|
|Default-2|7.033|1|
|NB-OFF-0|17.393|0|
|NB-OFF-1|17.357|0|
|NB-OFF-2|17.376|1|
|NB-OFF_NO_WA_IDLE-0|17.375|0|
|NB-OFF_NO_WA_IDLE-1|17.368|0|
|NB-OFF_NO_WA_IDLE-2|17.326|0|
  

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>


## PerfBenchFutexWake
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple futex wake -s -t 10240 -w 1  
~~~
|Test|Time (ms)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0| 139.4135 |78,599|
|Default-1| 122.9004 |81,151|
|Default-2| 117.7445 |83,845|
|NB-OFF-0| 136.9212 |84,728|
|NB-OFF-1| 113.7560 |79,767|
|NB-OFF-2| 120.1279 |81,057|
|NB-OFF_NO_WA_IDLE-0| 160.7393 |61,722|
|NB-OFF_NO_WA_IDLE-1| 160.3825 |81,997|
|NB-OFF_NO_WA_IDLE-2| 161.5401 |81,251|
  

## SysBenchCpu
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench cpu --time=60 --threads=64 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|214985.51|101|
|Default-1|214439.17|71|
|Default-2|214646.15|79|
|NB-OFF-0|214428.81|68|
|NB-OFF-1|214565.80|70|
|NB-OFF-2|214758.68|88|
|NB-OFF_NO_WA_IDLE-0|211450.02|3|
|NB-OFF_NO_WA_IDLE-1|212692.05|0|
|NB-OFF_NO_WA_IDLE-2|212341.53|0|
  

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## SysBenchMemory
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench memory --time=60 --memory-access-mode=rnd --threads=64 run  
~~~
|Test|Memory BW (MB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|10089.189|105|
|Default-1|10240.000|72|
|Default-2|10240.000|60|
|NB-OFF-0|9853.770|62|
|NB-OFF-1|9997.260|75|
|NB-OFF-2|10005.835|61|
|NB-OFF_NO_WA_IDLE-0|10240.000|1|
|NB-OFF_NO_WA_IDLE-1|10240.000|1|
|NB-OFF_NO_WA_IDLE-2|10240.000|0|
  

## SysBenchThreads
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench threads --time=60 --threads=64 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|24719.700|34,294|
|Default-1|24106.100|26,795|
|Default-2|25683.500|62,310|
|NB-OFF-0|22040.200|15,397|
|NB-OFF-1|25707.700|17,083|
|NB-OFF-2|23164.200|11,549|
|NB-OFF_NO_WA_IDLE-0|16947.900|0|
|NB-OFF_NO_WA_IDLE-1|17221.000|0|
|NB-OFF_NO_WA_IDLE-2|14859.700|0|
  

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## SysBenchMutex
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench mutex --mutex-num=1 --threads=512 run  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|32.7852|510,595|
|Default-1|33.0499|411,586|
|Default-2|32.8612|466,768|
|NB-OFF-0|35.6705|482,710|
|NB-OFF-1|35.4064|561,330|
|NB-OFF-2|33.0703|495,844|
|NB-OFF_NO_WA_IDLE-0|32.2315|793|
|NB-OFF_NO_WA_IDLE-1|35.0284|1,075|
|NB-OFF_NO_WA_IDLE-2|35.5196|1,084|
  

## HackbenchForkSockets
  
~~~  
perf stat -e sched:sched_migrate_task -- hackbench --loops 20000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|9.985|1,247,936|
|Default-1|9.847|1,247,309|
|Default-2|10.275|1,441,956|
|NB-OFF-0|7.976|1,185,273|
|NB-OFF-1|8.936|1,353,946|
|NB-OFF-2|9.676|1,298,643|
|NB-OFF_NO_WA_IDLE-0|9.756|2|
|NB-OFF_NO_WA_IDLE-1|6.933|7|
|NB-OFF_NO_WA_IDLE-2|8.006|5|
  

<div style="page-break-after: always; visibility: hidden"> 
\pagebreak 
</div>

## HackbenchPipeThreads
  
~~~  
perf stat -e sched:sched_migrate_task -- hackbench --pipe --threads --loops 20000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|5.349|2,833,593|
|Default-1|5.207|2,973,888|
|Default-2|5.427|2,885,721|
|NB-OFF-0|4.968|3,078,874|
|NB-OFF-1|5.008|2,875,476|
|NB-OFF-2|5.033|3,128,029|
|NB-OFF_NO_WA_IDLE-0|12.248|9|
|NB-OFF_NO_WA_IDLE-1|11.085|8|
|NB-OFF_NO_WA_IDLE-2|12.460|5|
  

## HackbenchPipeThreads4k
  
~~~  
perf stat -e sched:sched_migrate_task -- hackbench --pipe --threads --loops 20000 --datasize 4096  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|23.819|7,353,183|
|Default-1|23.788|7,492,891|
|Default-2|20.225|7,722,235|
|NB-OFF-0|21.289|7,429,308|
|NB-OFF-1|21.265|7,537,477|
|NB-OFF-2|21.161|7,529,834|
|NB-OFF_NO_WA_IDLE-0|21.883|7|
|NB-OFF_NO_WA_IDLE-1|22.359|0|
|NB-OFF_NO_WA_IDLE-2|22.263|0|
  
