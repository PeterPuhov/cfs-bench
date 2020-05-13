
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
|Default|12.354|424|
|NB-OFF|12.262|347|
|NB-OFF_NO_WA_IDLE|11.342|0|
  

## PerfBenchSchedMessaging
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched messaging -l 10000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|7.619|847,931|
|NB-OFF|3.629|604,535|
|NB-OFF_NO_WA_IDLE|3.923|2|
  

## PerfBenchMemMemset
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple  mem memset -s 1GB -l 5 -f default  
~~~
|Test|Memory BW (GB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|17.472|0|
|NB-OFF|17.429|0|
|NB-OFF_NO_WA_IDLE|17.261|0|
  

## PerfBenchFutexWake
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple futex wake -s -t 1024 -w 1  
~~~
|Test|Time (ms)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default| 9.4183 |5,707|
|NB-OFF| 9.0085 |7,160|
|NB-OFF_NO_WA_IDLE| 11.4350 |5,690|
  

## SysBenchCpu
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench cpu --time=10 --threads=64 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|214256.73|26|
|NB-OFF|214028.04|20|
|NB-OFF_NO_WA_IDLE|205444.54|0|
  

## SysBenchMemory
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench memory --memory-access-mode=rnd --threads=64 run  
~~~
|Test|Memory BW (MB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|1891.811|47|
|NB-OFF|2069.802|33|
|NB-OFF_NO_WA_IDLE|2175.316|0|
  

## SysBenchThreads
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench threads --threads=64 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|4136.000|40,678|
|NB-OFF|4104.100|30,603|
|NB-OFF_NO_WA_IDLE|3097.200|0|
  

## SysBenchMutex
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench mutex --mutex-num=1 --threads=512 run  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|33.0029|478,114|
|NB-OFF|35.8941|501,071|
|NB-OFF_NO_WA_IDLE|32.8039|1,198|
  
