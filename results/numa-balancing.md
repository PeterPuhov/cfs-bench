
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
|numa_balancing-ON|10.442 (usecs/op)|
|numa_balancing-OFF|10.099 (usecs/op)|
  


**<font color="blue">``PerfBenchSchedMessaging: perf bench -f simple sched messaging -l 10000``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|6.766 (Sec)|
|numa_balancing-OFF|6.058 (Sec)|
  


**<font color="blue">``PerfBenchMemMemset: perf bench -f simple  mem memset -s 4GB -l 5 -f default``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|16.87722410168865 (GB/sec)|
|numa_balancing-OFF|17.135948907454736 (GB/sec)|
  


**<font color="blue">``PerfBenchFutexWake: perf bench -f simple futex wake -s -t 1024 -w 1``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON| 10.3396  (ms)|
|numa_balancing-OFF| 8.1553  (ms)|
  


**<font color="blue">``SysBenchCpu: sysbench cpu --time=10 --threads=64 --cpu-max-prime=10000 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|214005.88 (Events/sec)|
|numa_balancing-OFF|215078.81 (Events/sec)|
  


**<font color="blue">``SysBenchMemory: sysbench memory --memory-access-mode=rnd --threads=64 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|2437 (MB/s)|
|numa_balancing-OFF|2611 (MB/s)|
  


**<font color="blue">``SysBenchThreads: sysbench threads --threads=64 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|4588 (Events/sec)|
|numa_balancing-OFF|3958 (Events/sec)|
  


**<font color="blue">``SysBenchMutex: sysbench mutex --mutex-num=1 --threads=512 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|32.8115 (Sec)|
|numa_balancing-OFF|32.1530 (Sec)|
  
