
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
|Kernel release|5.7.0-rc3+|
|Node name|ARMv2-3|

# Test results

## PerfBenchSchedPipe
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched pipe  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|12.336|395|
|Default-1|12.444|409|
|Default-2|12.176|408|
|NB-OFF-0|12.247|361|
|NB-OFF-1|12.407|368|
|NB-OFF-2|12.446|392|
|NB-OFF_NO_WA_IDLE-0|11.456|0|
|NB-OFF_NO_WA_IDLE-1|11.376|0|
|NB-OFF_NO_WA_IDLE-2|11.502|0|
  

## PerfBenchSchedMessaging
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched messaging -l 10000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|5.540|701,093|
|Default-1|3.507|538,236|
|Default-2|3.300|585,005|
|NB-OFF-0|5.049|705,629|
|NB-OFF-1|6.313|735,459|
|NB-OFF-2|4.656|600,063|
|NB-OFF_NO_WA_IDLE-0|3.655|0|
|NB-OFF_NO_WA_IDLE-1|3.899|1|
|NB-OFF_NO_WA_IDLE-2|4.118|3|
  

## PerfBenchMemMemset
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple  mem memset -s 1GB -l 5 -f default  
~~~
|Test|Memory BW (GB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|17.806|0|
|Default-1|17.931|0|
|Default-2|17.823|0|
|NB-OFF-0|17.832|0|
|NB-OFF-1|17.356|0|
|NB-OFF-2|17.361|0|
|NB-OFF_NO_WA_IDLE-0|17.388|0|
|NB-OFF_NO_WA_IDLE-1|17.332|0|
|NB-OFF_NO_WA_IDLE-2|17.343|0|
  

## PerfBenchFutexWake
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple futex wake -s -t 1024 -w 1  
~~~
|Test|Time (ms)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0| 8.3858 |7,126|
|Default-1| 9.5230 |6,547|
|Default-2| 9.1789 |6,862|
|NB-OFF-0| 9.9239 |6,778|
|NB-OFF-1| 8.5282 |6,456|
|NB-OFF-2| 8.9811 |5,771|
|NB-OFF_NO_WA_IDLE-0| 11.5021 |4,985|
|NB-OFF_NO_WA_IDLE-1| 12.7811 |3,528|
|NB-OFF_NO_WA_IDLE-2| 11.8338 |4,943|
  

## SysBenchCpu
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench cpu --time=10 --threads=64 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|209320.70|30|
|Default-1|213404.55|45|
|Default-2|212784.36|39|
|NB-OFF-0|213257.64|46|
|NB-OFF-1|213463.56|30|
|NB-OFF-2|213477.43|38|
|NB-OFF_NO_WA_IDLE-0|206974.98|0|
|NB-OFF_NO_WA_IDLE-1|205283.03|0|
|NB-OFF_NO_WA_IDLE-2|204709.92|1|
  

## SysBenchMemory
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench memory --memory-access-mode=rnd --threads=64 run  
~~~
|Test|Memory BW (MB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|2179.069|29|
|Default-1|1790.665|57|
|Default-2|1961.600|50|
|NB-OFF-0|2017.468|35|
|NB-OFF-1|1988.998|21|
|NB-OFF-2|2112.257|28|
|NB-OFF_NO_WA_IDLE-0|2210.283|0|
|NB-OFF_NO_WA_IDLE-1|2175.308|2|
|NB-OFF_NO_WA_IDLE-2|2306.381|0|
  

## SysBenchThreads
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench threads --threads=64 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|5435.700|8,313|
|Default-1|3593.200|5,635|
|Default-2|2587.200|29,271|
|NB-OFF-0|3618.900|9,832|
|NB-OFF-1|4756.400|10,731|
|NB-OFF-2|3498.000|11,136|
|NB-OFF_NO_WA_IDLE-0|3144.200|0|
|NB-OFF_NO_WA_IDLE-1|3069.100|0|
|NB-OFF_NO_WA_IDLE-2|3266.800|0|
  

## SysBenchMutex
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench mutex --mutex-num=1 --threads=512 run  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default-0|35.4043|474,463|
|Default-1|33.7266|448,026|
|Default-2|35.1500|516,744|
|NB-OFF-0|35.5076|557,096|
|NB-OFF-1|33.2707|391,050|
|NB-OFF-2|33.3526|442,954|
|NB-OFF_NO_WA_IDLE-0|34.2531|1,050|
|NB-OFF_NO_WA_IDLE-1|32.7277|1,052|
|NB-OFF_NO_WA_IDLE-2|33.1484|758|
  
