
NUMA balancing impact on common benchmarks
==========================================


**NUMA balancing can lead to performance degradation on                    NUMA-based arm64 systems when tasks migrate,  
                    and their memory accesses now suffer additional latency.**
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


**<font color="blue">``PerfBenchSchedPipe: perf bench -f simple sched pipe``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|10.139 (usecs/op)|
|numa_balancing-OFF|10.360 (usecs/op)|
  


**<font color="blue">``PerfBenchSchedMessaging: perf bench -f simple sched messaging -l 10000``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|5.391 (Sec)|
|numa_balancing-OFF|5.593 (Sec)|
  


**<font color="blue">``PerfBenchMemMemset: perf bench -f simple  mem memset -s 4GB -l 5 -f default``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|16.926746120812957 (GB/sec)|
|numa_balancing-OFF|17.681621192483895 (GB/sec)|
  


**<font color="blue">``PerfBenchFutexWake: perf bench -f simple futex wake -s -t 1024 -w 1``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON| 8.3887  (ms)|
|numa_balancing-OFF| 9.2038  (ms)|
  


**<font color="blue">``SysBenchCpu: sysbench cpu --time=10 --threads=64 --cpu-max-prime=10000 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|214313.30 (Events/sec)|
|numa_balancing-OFF|214451.04 (Events/sec)|
  


**<font color="blue">``SysBenchMemory: sysbench memory --memory-access-mode=rnd --threads=64 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|2243 (MB/s)|
|numa_balancing-OFF|2868 (MB/s)|
  


**<font color="blue">``SysBenchThreads: sysbench threads --threads=64 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|3048 (Events/sec)|
|numa_balancing-OFF|2050 (Events/sec)|
  


**<font color="blue">``SysBenchMutex: sysbench mutex --mutex-num=1 --threads=512 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|33.3802 (Sec)|
|numa_balancing-OFF|34.5980 (Sec)|
  
