
NUMA balancing impact on common benchmarks
==========================================


**NUMA balancing can lead to performance degradation on                    NUMA-based arm64 systems when tasks migrate,  
                    and their memory accesses now suffer additional latency.**
# Platform
  

|System|Information|
| :--- | :--- |
|Architecture|x86_64|
|Processor version|AMD FX(tm)-8320 Eight-Core Processor           |
|CPUs|8|
|NUMA nodes|1|
|Kernel release|5.3.0-46-generic|
|Node name|Trinity|

# Test results


**<font color="blue">``PerfBenchSchedPipe: perf bench -f simple sched pipe``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|17.122 (usecs/op)|
|numa_balancing-OFF|17.133 (usecs/op)|
  


**<font color="blue">``PerfBenchSchedMessaging: perf bench -f simple sched messaging -l 10000``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|18.267 (Sec)|
|numa_balancing-OFF|22.384 (Sec)|
  


**<font color="blue">``PerfBenchMemMemset: perf bench -f simple  mem memset -s 4GB -l 5 -f default``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|5.632257515825235 (GB/sec)|
|numa_balancing-OFF|5.740363365001005 (GB/sec)|
  


**<font color="blue">``PerfBenchFutexWake: perf bench -f simple futex wake -s -t 1024 -w 1``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON| 12.6763  (ms)|
|numa_balancing-OFF| 11.8599  (ms)|
  


**<font color="blue">``SysBenchCpu: sysbench cpu --time=10 --threads=4 --cpu-max-prime=10000 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|5940.43 (Events/sec)|
|numa_balancing-OFF|5936.09 (Events/sec)|
  


**<font color="blue">``SysBenchMemory: sysbench memory --memory-access-mode=rnd --threads=4 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|507 (MB/s)|
|numa_balancing-OFF|498 (MB/s)|
  


**<font color="blue">``SysBenchThreads: sysbench threads --threads=4 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|7211 (Events/sec)|
|numa_balancing-OFF|6922 (Events/sec)|
  


**<font color="blue">``SysBenchMutex: sysbench mutex --mutex-num=1 --threads=32 run``</font>**  

|Test|Result|
| :--- | :--- |
|numa_balancing-ON|1.2819 (Sec)|
|numa_balancing-OFF|1.3692 (Sec)|
  
