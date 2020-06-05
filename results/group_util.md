
Usage of group_util in update_pick_idlest() impact on common benchmarks
=======================================================================


**In update_pick_idlest() function                    When both groups have 'group_has_spare' type  
                    and the same number of idle CPU's.                    We suggest evaluating group_util to find idlest group. **
# Platform
  

|System|Information|
| :--- | :--- |
|Architecture|aarch64|
|Processor version|Kunpeng 920-6426|
|CPUs|128|
|NUMA nodes|4|
|Memory (GB)|125|
|Kernel release|5.7.0-rc5+|
|Node name|ARMv2-3|

# Test results

## PerfBenchSchedPipe
  
~~~  
perf bench -f simple sched pipe -l 4000000  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default-0-0|44.821|
|Default-1-0|45.377|
|Default-2-0|44.636|
|Default-3-0|45.186|
|Default-4-0|44.975|
|G-Util-0-0|45.103|
|G-Util-1-0|45.044|
|G-Util-2-0|44.807|
|G-Util-3-0|45.204|
|G-Util-4-0|45.597|
  

## PerfBenchSchedMessaging
  
~~~  
perf bench -f simple sched messaging -l 30000  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default-0-0|11.568|
|Default-1-0|13.151|
|Default-2-0|21.364|
|Default-3-0|15.537|
|Default-4-0|14.662|
|G-Util-0-0|20.778|
|G-Util-1-0|14.648|
|G-Util-2-0|12.974|
|G-Util-3-0|11.251|
|G-Util-4-0|13.965|
  

## PerfBenchMemMemset
  
~~~  
perf bench -f simple  mem memset -s 31GB -l 15 -f default  
~~~
|Test|Memory BW (GB/s)|
| :--- | :--- |
|Default-0-0|6.442|
|Default-1-0|6.045|
|Default-2-0|6.939|
|Default-3-0|6.783|
|Default-4-0|6.456|
|G-Util-0-0|6.688|
|G-Util-1-0|6.250|
|G-Util-2-0|6.789|
|G-Util-3-0|6.897|
|G-Util-4-0|6.596|
  

## PerfBenchFutexWake
  
~~~  
perf bench -f simple futex wake -s -t 10240 -w 1  
~~~
|Test|Time (ms)|
| :--- | :--- |
|Default-0-0| 120.3559 |
|Default-1-0| 107.4532 |
|Default-2-0| 117.6437 |
|Default-3-0| 130.9546 |
|Default-4-0| 121.5351 |
|G-Util-0-0| 119.7272 |
|G-Util-1-0| 119.1636 |
|G-Util-2-0| 117.1543 |
|G-Util-3-0| 108.0825 |
|G-Util-4-0| 118.2159 |
  

## SysBenchCpu
  
~~~  
sysbench cpu --time=60 --threads=64 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|
| :--- | :--- |
|Default-0-0|214897.15|
|Default-1-0|214961.21|
|Default-2-0|214937.66|
|Default-3-0|214837.28|
|Default-4-0|214865.44|
|G-Util-0-0|213590.74|
|G-Util-1-0|214696.70|
|G-Util-2-0|214687.55|
|G-Util-3-0|214953.15|
|G-Util-4-0|214733.40|
  

## SysBenchMemory
  
~~~  
sysbench memory --time=60 --memory-access-mode=rnd --threads=64 run  
~~~
|Test|Memory BW (MB/s)|
| :--- | :--- |
|Default-0-0|9811.336|
|Default-1-0|10240.000|
|Default-2-0|9856.223|
|Default-3-0|9980.292|
|Default-4-0|10240.000|
|G-Util-0-0|10240.000|
|G-Util-1-0|9824.576|
|G-Util-2-0|9684.329|
|G-Util-3-0|10240.000|
|G-Util-4-0|9889.843|
  

## SysBenchThreads
  
~~~  
sysbench threads --time=60 --threads=64 run  
~~~
|Test|Events/sec|
| :--- | :--- |
|Default-0-0|27648.900|
|Default-1-0|27850.500|
|Default-2-0|30589.400|
|Default-3-0|25594.000|
|Default-4-0|22351.200|
|G-Util-0-0|24376.500|
|G-Util-1-0|26914.300|
|G-Util-2-0|25410.000|
|G-Util-3-0|23053.300|
|G-Util-4-0|19973.500|
  

## SysBenchMutex
  
~~~  
sysbench mutex --mutex-num=1 --threads=512 run  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default-0-0|34.4310|
|Default-1-0|32.8397|
|Default-2-0|33.3377|
|Default-3-0|33.1800|
|Default-4-0|34.3642|
|G-Util-0-0|34.3727|
|G-Util-1-0|34.8483|
|G-Util-2-0|32.0809|
|G-Util-3-0|34.5659|
|G-Util-4-0|34.0385|
  

## HackbenchForkSockets
  
~~~  
hackbench --loops 20000  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default-0-0|14.191|
|Default-1-0|10.083|
|Default-2-0|6.849|
|Default-3-0|8.283|
|Default-4-0|8.742|
|G-Util-0-0|7.291|
|G-Util-1-0|13.371|
|G-Util-2-0|13.296|
|G-Util-3-0|11.405|
|G-Util-4-0|13.118|
  

## HackbenchPipeThreads
  
~~~  
hackbench --pipe --threads --loops 20000  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default-0-0|5.852|
|Default-1-0|7.216|
|Default-2-0|5.900|
|Default-3-0|8.202|
|Default-4-0|5.292|
|G-Util-0-0|5.708|
|G-Util-1-0|6.429|
|G-Util-2-0|5.348|
|G-Util-3-0|4.996|
|G-Util-4-0|4.830|
  

## HackbenchPipeThreads4k
  
~~~  
hackbench --pipe --threads --loops 20000 --datasize 4096  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default-0-0|20.334|
|Default-1-0|19.839|
|Default-2-0|19.997|
|Default-3-0|20.152|
|Default-4-0|20.115|
|G-Util-0-0|20.848|
|G-Util-1-0|20.261|
|G-Util-2-0|20.088|
|G-Util-3-0|20.027|
|G-Util-4-0|19.845|
  
