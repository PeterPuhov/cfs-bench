
Usage of group_util in update_pick_idlest() impact on common benchmarks
=======================================================================


**In update_pick_idlest() function                    When both groups have 'group_has_spare' type                    and the same number of idle CPU's.                    We suggest evaluating group_util to find idlest group. **
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

## SysBenchCpu
  
~~~  
sysbench cpu --threads=32 --cpu-max-prime=10000 run  
~~~
|Test|Events/sec|
| :--- | :--- |
|Default (0)|107591.61|
|Default (1)|107688.30|
|Default (2)|107701.81|
|Default (3)|107607.66|
|Default (4)|107685.04|
|group_util (0)|107643.39|
|group_util (1)|107640.77|
|group_util (2)|107624.95|
|group_util (3)|107649.54|
|group_util (4)|107661.51|
|Default (avg)|107654.884|
|group_util (avg)|107644.032|
  

## SysBenchMemory
  
~~~  
sysbench memory --memory-access-mode=rnd --threads=32 run  
~~~
|Test|Memory BW (MB/s)|
| :--- | :--- |
|Default (0)|2759.848|
|Default (1)|3168.569|
|Default (2)|3187.909|
|Default (3)|2935.968|
|Default (4)|3168.384|
|group_util (0)|3102.000|
|group_util (1)|2597.826|
|group_util (2)|3149.183|
|group_util (3)|2615.611|
|group_util (4)|2692.906|
|Default (avg)|3044.136|
|group_util (avg)|2831.505|
  

## SysBenchThreads
  
~~~  
sysbench threads --threads=32 run  
~~~
|Test|Events/sec|
| :--- | :--- |
|Default (0)|5758.200|
|Default (1)|5725.000|
|Default (2)|6229.400|
|Default (3)|6156.200|
|Default (4)|6177.400|
|group_util (0)|6354.900|
|group_util (1)|6037.700|
|group_util (2)|6300.000|
|group_util (3)|6186.000|
|group_util (4)|4773.400|
|Default (avg)|6009.24|
|group_util (avg)|5930.4|
  

## SysBenchMutex
  
~~~  
sysbench mutex --mutex-num=1 --threads=32 run  
~~~
|Test|Time (sec)|
| :--- | :--- |
|Default (0)|0.8254|
|Default (1)|0.8039|
|Default (2)|0.8151|
|Default (3)|0.8266|
|Default (4)|0.8387|
|group_util (0)|0.9016|
|group_util (1)|0.8175|
|group_util (2)|0.8212|
|group_util (3)|0.9045|
|group_util (4)|0.8332|
|Default (avg)|0.822|
|group_util (avg)|0.856|
  
