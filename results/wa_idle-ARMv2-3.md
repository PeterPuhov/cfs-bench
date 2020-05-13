
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
|Kernel release|5.6.0+|
|Node name|ARMv2-3|

# Test results

## PerfBenchSchedPipe
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched pipe  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|11.913|301|
|NB-OFF|11.111|179|
|NB-OFF_NO_WA_IDLE|13.639|448|
  

## PerfBenchSchedMessaging
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple sched messaging -l 10000  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|6.057|773,099|
|NB-OFF|8.003|908,927|
|NB-OFF_NO_WA_IDLE|6.018|462,440|
  

## PerfBenchMemMemset
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple  mem memset -s 1GB -l 5 -f default  
~~~
|Test|Memory BW (GB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|16.711|1|
|NB-OFF|16.753|0|
|NB-OFF_NO_WA_IDLE|16.727|0|
  

## PerfBenchFutexWake
  
~~~  
perf stat -e sched:sched_migrate_task -- perf bench -f simple futex wake -s -t 1024 -w 1  
~~~
|Test|Time (ms)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default| 9.5056 |6,990|
|NB-OFF| 9.7695 |6,575|
|NB-OFF_NO_WA_IDLE| 9.5672 |6,936|
  

## SysBenchCpu
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench cpu --time=10 --threads=64 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|213870.43|116|
|NB-OFF|213281.87|99|
|NB-OFF_NO_WA_IDLE|214342.12|103|
  

## SysBenchMemory
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench memory --memory-access-mode=rnd --threads=64 run  
~~~
|Test|Memory BW (MB/s)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|2689.767|164|
|NB-OFF|2546.486|146|
|NB-OFF_NO_WA_IDLE|2178.907|96|
  

## SysBenchThreads
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench threads --threads=64 run  
~~~
|Test|Events/sec|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|4383.300|24,899|
|NB-OFF|5109.000|8,486|
|NB-OFF_NO_WA_IDLE|3853.300|25,354|
  

## SysBenchMutex
  
~~~  
perf stat -e sched:sched_migrate_task -- sysbench mutex --mutex-num=1 --threads=512 run  
~~~
|Test|Time (sec)|sched:sched_migrate_task|
| :--- | :--- | :--- |
|Default|34.1339|471,916|
|NB-OFF|32.7279|447,373|
|NB-OFF_NO_WA_IDLE|32.4349|5,192|
  
