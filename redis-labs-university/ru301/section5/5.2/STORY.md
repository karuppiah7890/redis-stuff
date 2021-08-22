I just tried to run all the commands mentioned in the exercise

I found out some good data only in some commands I guess. Especially the `INFO stats` command one, when looking at values with `total` in it

```bash
redislabs-training $ ls
exercises-scaling-redis	ru101
redislabs-training $ cd exercises-scaling-redis/
exercises-scaling-redis $ cd observability-
-bash: cd: observability-: No such file or directory
exercises-scaling-redis $ cd observability-
observability-monitoring/ observability-stats/      
exercises-scaling-redis $ cd observability-stats/
observability-stats $ docker-compose
docker-compose     docker-compose-v1  
observability-stats $ docker-compose up -d
[+] Running 1/1
 ⠿ redis_stats Pulled                                                                                           3.4s
[+] Running 2/2
 ⠿ Network observability-stats_default          Created                                                         0.1s
 ⠿ Container observability-stats_redis_stats_1  Started                                                         0.5s
observability-stats $ docker-compose ps
NAME                                COMMAND                  SERVICE             STATUS              PORTS
observability-stats_redis_stats_1   "docker-entrypoint.s…"   redis_stats         running             0.0.0.0:6379->6379/tcp, :::6379->6379/tcp
observability-stats $ docker-compose exec redis_stats bash
root@3dc9d53afef6:/data# redis-benchmark 
====== PING_INLINE ======                                                   
  100000 requests completed in 3.32 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.607 milliseconds (cumulative count 1)
50.000% <= 1.295 milliseconds (cumulative count 50340)
75.000% <= 1.615 milliseconds (cumulative count 75298)
87.500% <= 1.807 milliseconds (cumulative count 87816)
93.750% <= 1.959 milliseconds (cumulative count 93810)
96.875% <= 2.175 milliseconds (cumulative count 96887)
98.438% <= 2.455 milliseconds (cumulative count 98449)
99.219% <= 2.719 milliseconds (cumulative count 99225)
99.609% <= 2.999 milliseconds (cumulative count 99616)
99.805% <= 3.295 milliseconds (cumulative count 99805)
99.902% <= 3.575 milliseconds (cumulative count 99903)
99.951% <= 3.847 milliseconds (cumulative count 99953)
99.976% <= 4.031 milliseconds (cumulative count 99976)
99.988% <= 4.231 milliseconds (cumulative count 99989)
99.994% <= 4.455 milliseconds (cumulative count 99994)
99.997% <= 4.663 milliseconds (cumulative count 99997)
99.998% <= 5.023 milliseconds (cumulative count 99999)
99.999% <= 5.215 milliseconds (cumulative count 100000)
100.000% <= 5.215 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.607 milliseconds (cumulative count 1)
0.070% <= 0.703 milliseconds (cumulative count 70)
1.832% <= 0.807 milliseconds (cumulative count 1832)
8.091% <= 0.903 milliseconds (cumulative count 8091)
17.809% <= 1.007 milliseconds (cumulative count 17809)
27.632% <= 1.103 milliseconds (cumulative count 27632)
40.686% <= 1.207 milliseconds (cumulative count 40686)
51.090% <= 1.303 milliseconds (cumulative count 51090)
60.216% <= 1.407 milliseconds (cumulative count 60216)
67.500% <= 1.503 milliseconds (cumulative count 67500)
74.723% <= 1.607 milliseconds (cumulative count 74723)
81.155% <= 1.703 milliseconds (cumulative count 81155)
87.816% <= 1.807 milliseconds (cumulative count 87816)
92.302% <= 1.903 milliseconds (cumulative count 92302)
94.823% <= 2.007 milliseconds (cumulative count 94823)
96.195% <= 2.103 milliseconds (cumulative count 96195)
99.702% <= 3.103 milliseconds (cumulative count 99702)
99.979% <= 4.103 milliseconds (cumulative count 99979)
99.999% <= 5.103 milliseconds (cumulative count 99999)
100.000% <= 6.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 30093.29 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.367     0.600     1.295     2.023     2.639     5.215
====== PING_MBULK ======                                                   
  100000 requests completed in 3.34 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.527 milliseconds (cumulative count 1)
50.000% <= 1.303 milliseconds (cumulative count 50550)
75.000% <= 1.623 milliseconds (cumulative count 75483)
87.500% <= 1.823 milliseconds (cumulative count 87801)
93.750% <= 1.999 milliseconds (cumulative count 93882)
96.875% <= 2.239 milliseconds (cumulative count 96881)
98.438% <= 2.471 milliseconds (cumulative count 98454)
99.219% <= 2.663 milliseconds (cumulative count 99235)
99.609% <= 2.871 milliseconds (cumulative count 99623)
99.805% <= 3.063 milliseconds (cumulative count 99807)
99.902% <= 3.271 milliseconds (cumulative count 99905)
99.951% <= 3.567 milliseconds (cumulative count 99952)
99.976% <= 3.719 milliseconds (cumulative count 99976)
99.988% <= 3.823 milliseconds (cumulative count 99988)
99.994% <= 3.975 milliseconds (cumulative count 99994)
99.997% <= 4.055 milliseconds (cumulative count 99997)
99.998% <= 4.247 milliseconds (cumulative count 99999)
99.999% <= 4.279 milliseconds (cumulative count 100000)
100.000% <= 4.279 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.008% <= 0.607 milliseconds (cumulative count 8)
0.136% <= 0.703 milliseconds (cumulative count 136)
2.038% <= 0.807 milliseconds (cumulative count 2038)
7.896% <= 0.903 milliseconds (cumulative count 7896)
17.192% <= 1.007 milliseconds (cumulative count 17192)
26.813% <= 1.103 milliseconds (cumulative count 26813)
39.648% <= 1.207 milliseconds (cumulative count 39648)
50.550% <= 1.303 milliseconds (cumulative count 50550)
59.936% <= 1.407 milliseconds (cumulative count 59936)
67.222% <= 1.503 milliseconds (cumulative count 67222)
74.373% <= 1.607 milliseconds (cumulative count 74373)
80.687% <= 1.703 milliseconds (cumulative count 80687)
86.966% <= 1.807 milliseconds (cumulative count 86966)
91.197% <= 1.903 milliseconds (cumulative count 91197)
94.040% <= 2.007 milliseconds (cumulative count 94040)
95.520% <= 2.103 milliseconds (cumulative count 95520)
99.835% <= 3.103 milliseconds (cumulative count 99835)
99.998% <= 4.103 milliseconds (cumulative count 99998)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 29904.30 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.374     0.520     1.303     2.071     2.599     4.279
====== SET ======                                                   
  100000 requests completed in 3.58 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.591 milliseconds (cumulative count 1)
50.000% <= 1.423 milliseconds (cumulative count 50476)
75.000% <= 1.783 milliseconds (cumulative count 75255)
87.500% <= 1.991 milliseconds (cumulative count 87510)
93.750% <= 2.247 milliseconds (cumulative count 93871)
96.875% <= 2.471 milliseconds (cumulative count 96909)
98.438% <= 2.639 milliseconds (cumulative count 98451)
99.219% <= 2.783 milliseconds (cumulative count 99233)
99.609% <= 2.919 milliseconds (cumulative count 99615)
99.805% <= 3.039 milliseconds (cumulative count 99812)
99.902% <= 3.135 milliseconds (cumulative count 99906)
99.951% <= 3.231 milliseconds (cumulative count 99954)
99.976% <= 3.327 milliseconds (cumulative count 99977)
99.988% <= 3.399 milliseconds (cumulative count 99988)
99.994% <= 3.447 milliseconds (cumulative count 99994)
99.997% <= 3.687 milliseconds (cumulative count 99997)
99.998% <= 3.775 milliseconds (cumulative count 99999)
99.999% <= 3.847 milliseconds (cumulative count 100000)
100.000% <= 3.847 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.002% <= 0.607 milliseconds (cumulative count 2)
0.037% <= 0.703 milliseconds (cumulative count 37)
0.491% <= 0.807 milliseconds (cumulative count 491)
2.992% <= 0.903 milliseconds (cumulative count 2992)
9.942% <= 1.007 milliseconds (cumulative count 9942)
17.451% <= 1.103 milliseconds (cumulative count 17451)
27.290% <= 1.207 milliseconds (cumulative count 27290)
38.851% <= 1.303 milliseconds (cumulative count 38851)
49.122% <= 1.407 milliseconds (cumulative count 49122)
56.574% <= 1.503 milliseconds (cumulative count 56574)
63.895% <= 1.607 milliseconds (cumulative count 63895)
70.181% <= 1.703 milliseconds (cumulative count 70181)
76.789% <= 1.807 milliseconds (cumulative count 76789)
82.840% <= 1.903 milliseconds (cumulative count 82840)
88.273% <= 2.007 milliseconds (cumulative count 88273)
91.117% <= 2.103 milliseconds (cumulative count 91117)
99.878% <= 3.103 milliseconds (cumulative count 99878)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 27917.37 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.503     0.584     1.423     2.327     2.727     3.847
====== GET ======                                                   
  100000 requests completed in 3.54 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.583 milliseconds (cumulative count 1)
50.000% <= 1.399 milliseconds (cumulative count 50327)
75.000% <= 1.751 milliseconds (cumulative count 75384)
87.500% <= 1.967 milliseconds (cumulative count 87811)
93.750% <= 2.215 milliseconds (cumulative count 93856)
96.875% <= 2.471 milliseconds (cumulative count 96879)
98.438% <= 2.671 milliseconds (cumulative count 98469)
99.219% <= 2.847 milliseconds (cumulative count 99231)
99.609% <= 3.023 milliseconds (cumulative count 99613)
99.805% <= 3.215 milliseconds (cumulative count 99808)
99.902% <= 3.463 milliseconds (cumulative count 99909)
99.951% <= 3.679 milliseconds (cumulative count 99952)
99.976% <= 3.863 milliseconds (cumulative count 99976)
99.988% <= 4.007 milliseconds (cumulative count 99988)
99.994% <= 4.095 milliseconds (cumulative count 99994)
99.997% <= 4.143 milliseconds (cumulative count 99997)
99.998% <= 4.215 milliseconds (cumulative count 99999)
99.999% <= 4.239 milliseconds (cumulative count 100000)
100.000% <= 4.239 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.607 milliseconds (cumulative count 1)
0.030% <= 0.703 milliseconds (cumulative count 30)
0.518% <= 0.807 milliseconds (cumulative count 518)
3.526% <= 0.903 milliseconds (cumulative count 3526)
10.689% <= 1.007 milliseconds (cumulative count 10689)
18.283% <= 1.103 milliseconds (cumulative count 18283)
29.277% <= 1.207 milliseconds (cumulative count 29277)
40.873% <= 1.303 milliseconds (cumulative count 40873)
51.012% <= 1.407 milliseconds (cumulative count 51012)
58.639% <= 1.503 milliseconds (cumulative count 58639)
65.998% <= 1.607 milliseconds (cumulative count 65998)
72.294% <= 1.703 milliseconds (cumulative count 72294)
79.022% <= 1.807 milliseconds (cumulative count 79022)
84.792% <= 1.903 milliseconds (cumulative count 84792)
89.366% <= 2.007 milliseconds (cumulative count 89366)
91.859% <= 2.103 milliseconds (cumulative count 91859)
99.714% <= 3.103 milliseconds (cumulative count 99714)
99.994% <= 4.103 milliseconds (cumulative count 99994)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 28288.54 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.484     0.576     1.399     2.303     2.783     4.239
====== INCR ======                                                   
  100000 requests completed in 3.64 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.551 milliseconds (cumulative count 1)
50.000% <= 1.447 milliseconds (cumulative count 50661)
75.000% <= 1.783 milliseconds (cumulative count 75307)
87.500% <= 2.007 milliseconds (cumulative count 87600)
93.750% <= 2.263 milliseconds (cumulative count 93779)
96.875% <= 2.535 milliseconds (cumulative count 96904)
98.438% <= 2.815 milliseconds (cumulative count 98448)
99.219% <= 3.087 milliseconds (cumulative count 99219)
99.609% <= 3.415 milliseconds (cumulative count 99611)
99.805% <= 3.679 milliseconds (cumulative count 99810)
99.902% <= 3.911 milliseconds (cumulative count 99904)
99.951% <= 4.119 milliseconds (cumulative count 99953)
99.976% <= 4.303 milliseconds (cumulative count 99976)
99.988% <= 4.487 milliseconds (cumulative count 99988)
99.994% <= 4.615 milliseconds (cumulative count 99994)
99.997% <= 4.759 milliseconds (cumulative count 99997)
99.998% <= 4.847 milliseconds (cumulative count 99999)
99.999% <= 4.959 milliseconds (cumulative count 100000)
100.000% <= 4.959 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.005% <= 0.607 milliseconds (cumulative count 5)
0.045% <= 0.703 milliseconds (cumulative count 45)
0.477% <= 0.807 milliseconds (cumulative count 477)
3.004% <= 0.903 milliseconds (cumulative count 3004)
8.889% <= 1.007 milliseconds (cumulative count 8889)
15.600% <= 1.103 milliseconds (cumulative count 15600)
25.622% <= 1.207 milliseconds (cumulative count 25622)
36.668% <= 1.303 milliseconds (cumulative count 36668)
47.038% <= 1.407 milliseconds (cumulative count 47038)
55.423% <= 1.503 milliseconds (cumulative count 55423)
63.419% <= 1.607 milliseconds (cumulative count 63419)
70.054% <= 1.703 milliseconds (cumulative count 70054)
76.937% <= 1.807 milliseconds (cumulative count 76937)
82.841% <= 1.903 milliseconds (cumulative count 82841)
87.600% <= 2.007 milliseconds (cumulative count 87600)
90.569% <= 2.103 milliseconds (cumulative count 90569)
99.242% <= 3.103 milliseconds (cumulative count 99242)
99.949% <= 4.103 milliseconds (cumulative count 99949)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 27472.53 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.524     0.544     1.447     2.351     2.991     4.959
====== LPUSH ======                                                   
  100000 requests completed in 3.43 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.599 milliseconds (cumulative count 1)
50.000% <= 1.375 milliseconds (cumulative count 50447)
75.000% <= 1.687 milliseconds (cumulative count 75384)
87.500% <= 1.879 milliseconds (cumulative count 87651)
93.750% <= 2.031 milliseconds (cumulative count 93870)
96.875% <= 2.215 milliseconds (cumulative count 96884)
98.438% <= 2.463 milliseconds (cumulative count 98478)
99.219% <= 2.751 milliseconds (cumulative count 99222)
99.609% <= 3.095 milliseconds (cumulative count 99612)
99.805% <= 3.487 milliseconds (cumulative count 99807)
99.902% <= 3.807 milliseconds (cumulative count 99903)
99.951% <= 4.135 milliseconds (cumulative count 99952)
99.976% <= 4.495 milliseconds (cumulative count 99976)
99.988% <= 4.759 milliseconds (cumulative count 99988)
99.994% <= 5.055 milliseconds (cumulative count 99994)
99.997% <= 5.239 milliseconds (cumulative count 99997)
99.998% <= 5.407 milliseconds (cumulative count 99999)
99.999% <= 5.463 milliseconds (cumulative count 100000)
100.000% <= 5.463 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.002% <= 0.607 milliseconds (cumulative count 2)
0.036% <= 0.703 milliseconds (cumulative count 36)
0.554% <= 0.807 milliseconds (cumulative count 554)
3.378% <= 0.903 milliseconds (cumulative count 3378)
10.785% <= 1.007 milliseconds (cumulative count 10785)
18.328% <= 1.103 milliseconds (cumulative count 18328)
29.673% <= 1.207 milliseconds (cumulative count 29673)
42.514% <= 1.303 milliseconds (cumulative count 42514)
53.511% <= 1.407 milliseconds (cumulative count 53511)
62.105% <= 1.503 milliseconds (cumulative count 62105)
69.890% <= 1.607 milliseconds (cumulative count 69890)
76.453% <= 1.703 milliseconds (cumulative count 76453)
83.217% <= 1.807 milliseconds (cumulative count 83217)
89.061% <= 1.903 milliseconds (cumulative count 89061)
93.232% <= 2.007 milliseconds (cumulative count 93232)
95.432% <= 2.103 milliseconds (cumulative count 95432)
99.616% <= 3.103 milliseconds (cumulative count 99616)
99.949% <= 4.103 milliseconds (cumulative count 99949)
99.994% <= 5.103 milliseconds (cumulative count 99994)
100.000% <= 6.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 29171.53 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.442     0.592     1.375     2.087     2.639     5.463
====== RPUSH ======                                                   
  100000 requests completed in 3.33 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.543 milliseconds (cumulative count 1)
50.000% <= 1.343 milliseconds (cumulative count 50170)
75.000% <= 1.655 milliseconds (cumulative count 75458)
87.500% <= 1.847 milliseconds (cumulative count 87894)
93.750% <= 1.983 milliseconds (cumulative count 93799)
96.875% <= 2.167 milliseconds (cumulative count 96832)
98.438% <= 2.415 milliseconds (cumulative count 98411)
99.219% <= 2.687 milliseconds (cumulative count 99183)
99.609% <= 2.959 milliseconds (cumulative count 99571)
99.805% <= 3.231 milliseconds (cumulative count 99761)
99.902% <= 3.663 milliseconds (cumulative count 99857)
99.951% <= 4.207 milliseconds (cumulative count 99905)
99.976% <= 4.663 milliseconds (cumulative count 99929)
99.988% <= 5.087 milliseconds (cumulative count 99941)
99.994% <= 5.391 milliseconds (cumulative count 99947)
99.997% <= 5.551 milliseconds (cumulative count 99950)
99.998% <= 5.687 milliseconds (cumulative count 99952)
99.999% <= 5.775 milliseconds (cumulative count 99953)
100.000% <= 5.775 milliseconds (cumulative count 99953)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.005% <= 0.607 milliseconds (cumulative count 5)
0.075% <= 0.703 milliseconds (cumulative count 75)
0.779% <= 0.807 milliseconds (cumulative count 779)
4.245% <= 0.903 milliseconds (cumulative count 4243)
12.224% <= 1.007 milliseconds (cumulative count 12218)
20.240% <= 1.103 milliseconds (cumulative count 20230)
32.837% <= 1.207 milliseconds (cumulative count 32822)
45.748% <= 1.303 milliseconds (cumulative count 45726)
56.352% <= 1.407 milliseconds (cumulative count 56326)
64.535% <= 1.503 milliseconds (cumulative count 64505)
72.184% <= 1.607 milliseconds (cumulative count 72150)
78.686% <= 1.703 milliseconds (cumulative count 78649)
85.471% <= 1.807 milliseconds (cumulative count 85431)
91.036% <= 1.903 milliseconds (cumulative count 90993)
94.404% <= 2.007 milliseconds (cumulative count 94360)
96.102% <= 2.103 milliseconds (cumulative count 96057)
99.746% <= 3.103 milliseconds (cumulative count 99699)
99.949% <= 4.103 milliseconds (cumulative count 99902)
99.989% <= 5.103 milliseconds (cumulative count 99942)
100.000% <= 6.103 milliseconds (cumulative count 99953)

Summary:
  throughput summary: 30039.05 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.413     0.536     1.343     2.039     2.583     5.775
====== LPOP ======                                                   
  100000 requests completed in 3.41 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.543 milliseconds (cumulative count 1)
50.000% <= 1.367 milliseconds (cumulative count 50309)
75.000% <= 1.679 milliseconds (cumulative count 75343)
87.500% <= 1.871 milliseconds (cumulative count 87609)
93.750% <= 2.007 milliseconds (cumulative count 93774)
96.875% <= 2.175 milliseconds (cumulative count 96957)
98.438% <= 2.359 milliseconds (cumulative count 98458)
99.219% <= 2.567 milliseconds (cumulative count 99225)
99.609% <= 2.783 milliseconds (cumulative count 99621)
99.805% <= 2.951 milliseconds (cumulative count 99814)
99.902% <= 3.087 milliseconds (cumulative count 99903)
99.951% <= 3.231 milliseconds (cumulative count 99952)
99.976% <= 3.351 milliseconds (cumulative count 99976)
99.988% <= 3.431 milliseconds (cumulative count 99989)
99.994% <= 3.559 milliseconds (cumulative count 99995)
99.997% <= 3.631 milliseconds (cumulative count 99997)
99.998% <= 3.679 milliseconds (cumulative count 99999)
99.999% <= 3.727 milliseconds (cumulative count 100000)
100.000% <= 3.727 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.002% <= 0.607 milliseconds (cumulative count 2)
0.035% <= 0.703 milliseconds (cumulative count 35)
0.515% <= 0.807 milliseconds (cumulative count 515)
3.404% <= 0.903 milliseconds (cumulative count 3404)
11.077% <= 1.007 milliseconds (cumulative count 11077)
18.865% <= 1.103 milliseconds (cumulative count 18865)
30.439% <= 1.207 milliseconds (cumulative count 30439)
43.231% <= 1.303 milliseconds (cumulative count 43231)
54.202% <= 1.407 milliseconds (cumulative count 54202)
62.648% <= 1.503 milliseconds (cumulative count 62648)
70.470% <= 1.607 milliseconds (cumulative count 70470)
76.951% <= 1.703 milliseconds (cumulative count 76951)
83.635% <= 1.807 milliseconds (cumulative count 83635)
89.510% <= 1.903 milliseconds (cumulative count 89510)
93.774% <= 2.007 milliseconds (cumulative count 93774)
95.906% <= 2.103 milliseconds (cumulative count 95906)
99.911% <= 3.103 milliseconds (cumulative count 99911)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 29351.33 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.430     0.536     1.367     2.063     2.495     3.727
====== RPOP ======                                                   
  100000 requests completed in 3.52 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.551 milliseconds (cumulative count 1)
50.000% <= 1.399 milliseconds (cumulative count 50259)
75.000% <= 1.727 milliseconds (cumulative count 75211)
87.500% <= 1.927 milliseconds (cumulative count 87543)
93.750% <= 2.127 milliseconds (cumulative count 93826)
96.875% <= 2.367 milliseconds (cumulative count 96877)
98.438% <= 2.631 milliseconds (cumulative count 98454)
99.219% <= 2.887 milliseconds (cumulative count 99231)
99.609% <= 3.159 milliseconds (cumulative count 99615)
99.805% <= 3.439 milliseconds (cumulative count 99806)
99.902% <= 3.711 milliseconds (cumulative count 99903)
99.951% <= 4.015 milliseconds (cumulative count 99952)
99.976% <= 4.303 milliseconds (cumulative count 99976)
99.988% <= 4.447 milliseconds (cumulative count 99988)
99.994% <= 4.559 milliseconds (cumulative count 99994)
99.997% <= 4.615 milliseconds (cumulative count 99998)
99.998% <= 4.639 milliseconds (cumulative count 99999)
99.999% <= 4.831 milliseconds (cumulative count 100000)
100.000% <= 4.831 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.003% <= 0.607 milliseconds (cumulative count 3)
0.055% <= 0.703 milliseconds (cumulative count 55)
0.506% <= 0.807 milliseconds (cumulative count 506)
3.180% <= 0.903 milliseconds (cumulative count 3180)
10.019% <= 1.007 milliseconds (cumulative count 10019)
17.308% <= 1.103 milliseconds (cumulative count 17308)
28.228% <= 1.207 milliseconds (cumulative count 28228)
40.307% <= 1.303 milliseconds (cumulative count 40307)
50.979% <= 1.407 milliseconds (cumulative count 50979)
59.300% <= 1.503 milliseconds (cumulative count 59300)
67.109% <= 1.607 milliseconds (cumulative count 67109)
73.667% <= 1.703 milliseconds (cumulative count 73667)
80.448% <= 1.807 milliseconds (cumulative count 80448)
86.320% <= 1.903 milliseconds (cumulative count 86320)
90.788% <= 2.007 milliseconds (cumulative count 90788)
93.341% <= 2.103 milliseconds (cumulative count 93341)
99.561% <= 3.103 milliseconds (cumulative count 99561)
99.956% <= 4.103 milliseconds (cumulative count 99956)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 28425.24 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.475     0.544     1.399     2.199     2.799     4.831
====== SADD ======                                                   
  100000 requests completed in 3.42 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.559 milliseconds (cumulative count 1)
50.000% <= 1.367 milliseconds (cumulative count 50749)
75.000% <= 1.679 milliseconds (cumulative count 75011)
87.500% <= 1.879 milliseconds (cumulative count 87603)
93.750% <= 2.055 milliseconds (cumulative count 93830)
96.875% <= 2.287 milliseconds (cumulative count 96927)
98.438% <= 2.519 milliseconds (cumulative count 98474)
99.219% <= 2.719 milliseconds (cumulative count 99231)
99.609% <= 2.919 milliseconds (cumulative count 99613)
99.805% <= 3.127 milliseconds (cumulative count 99806)
99.902% <= 3.359 milliseconds (cumulative count 99903)
99.951% <= 3.599 milliseconds (cumulative count 99952)
99.976% <= 3.807 milliseconds (cumulative count 99976)
99.988% <= 3.967 milliseconds (cumulative count 99988)
99.994% <= 4.103 milliseconds (cumulative count 99994)
99.997% <= 4.167 milliseconds (cumulative count 99997)
99.998% <= 4.295 milliseconds (cumulative count 99999)
99.999% <= 4.383 milliseconds (cumulative count 100000)
100.000% <= 4.383 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.006% <= 0.607 milliseconds (cumulative count 6)
0.071% <= 0.703 milliseconds (cumulative count 71)
0.791% <= 0.807 milliseconds (cumulative count 791)
4.175% <= 0.903 milliseconds (cumulative count 4175)
11.766% <= 1.007 milliseconds (cumulative count 11766)
19.596% <= 1.103 milliseconds (cumulative count 19596)
31.565% <= 1.207 milliseconds (cumulative count 31565)
43.926% <= 1.303 milliseconds (cumulative count 43926)
54.543% <= 1.407 milliseconds (cumulative count 54543)
62.655% <= 1.503 milliseconds (cumulative count 62655)
70.135% <= 1.607 milliseconds (cumulative count 70135)
76.577% <= 1.703 milliseconds (cumulative count 76577)
83.349% <= 1.807 milliseconds (cumulative count 83349)
88.836% <= 1.903 milliseconds (cumulative count 88836)
92.688% <= 2.007 milliseconds (cumulative count 92688)
94.738% <= 2.103 milliseconds (cumulative count 94738)
99.795% <= 3.103 milliseconds (cumulative count 99795)
99.994% <= 4.103 milliseconds (cumulative count 99994)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 29265.44 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.435     0.552     1.367     2.119     2.647     4.383
====== HSET ======                                                   
  100000 requests completed in 3.48 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.591 milliseconds (cumulative count 1)
50.000% <= 1.383 milliseconds (cumulative count 50310)
75.000% <= 1.719 milliseconds (cumulative count 75499)
87.500% <= 1.919 milliseconds (cumulative count 87812)
93.750% <= 2.103 milliseconds (cumulative count 93878)
96.875% <= 2.359 milliseconds (cumulative count 96898)
98.438% <= 2.583 milliseconds (cumulative count 98450)
99.219% <= 2.775 milliseconds (cumulative count 99240)
99.609% <= 2.959 milliseconds (cumulative count 99620)
99.805% <= 3.135 milliseconds (cumulative count 99806)
99.902% <= 3.319 milliseconds (cumulative count 99903)
99.951% <= 3.511 milliseconds (cumulative count 99952)
99.976% <= 3.711 milliseconds (cumulative count 99976)
99.988% <= 4.047 milliseconds (cumulative count 99988)
99.994% <= 4.239 milliseconds (cumulative count 99994)
99.997% <= 4.351 milliseconds (cumulative count 99997)
99.998% <= 4.447 milliseconds (cumulative count 99999)
99.999% <= 4.455 milliseconds (cumulative count 100000)
100.000% <= 4.455 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.002% <= 0.607 milliseconds (cumulative count 2)
0.046% <= 0.703 milliseconds (cumulative count 46)
0.565% <= 0.807 milliseconds (cumulative count 565)
3.368% <= 0.903 milliseconds (cumulative count 3368)
10.553% <= 1.007 milliseconds (cumulative count 10553)
18.280% <= 1.103 milliseconds (cumulative count 18280)
29.417% <= 1.207 milliseconds (cumulative count 29417)
41.681% <= 1.303 milliseconds (cumulative count 41681)
52.547% <= 1.407 milliseconds (cumulative count 52547)
60.601% <= 1.503 milliseconds (cumulative count 60601)
68.045% <= 1.607 milliseconds (cumulative count 68045)
74.447% <= 1.703 milliseconds (cumulative count 74447)
81.156% <= 1.807 milliseconds (cumulative count 81156)
86.980% <= 1.903 milliseconds (cumulative count 86980)
91.496% <= 2.007 milliseconds (cumulative count 91496)
93.878% <= 2.103 milliseconds (cumulative count 93878)
99.786% <= 3.103 milliseconds (cumulative count 99786)
99.989% <= 4.103 milliseconds (cumulative count 99989)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 28752.16 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.460     0.584     1.383     2.175     2.703     4.455
====== SPOP ======                                                   
  100000 requests completed in 3.28 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.535 milliseconds (cumulative count 1)
50.000% <= 1.327 milliseconds (cumulative count 50836)
75.000% <= 1.607 milliseconds (cumulative count 75014)
87.500% <= 1.799 milliseconds (cumulative count 87623)
93.750% <= 1.919 milliseconds (cumulative count 93806)
96.875% <= 2.039 milliseconds (cumulative count 96925)
98.438% <= 2.215 milliseconds (cumulative count 98466)
99.219% <= 2.439 milliseconds (cumulative count 99239)
99.609% <= 2.679 milliseconds (cumulative count 99611)
99.805% <= 2.927 milliseconds (cumulative count 99808)
99.902% <= 3.199 milliseconds (cumulative count 99903)
99.951% <= 3.439 milliseconds (cumulative count 99952)
99.976% <= 3.623 milliseconds (cumulative count 99976)
99.988% <= 3.743 milliseconds (cumulative count 99988)
99.994% <= 3.839 milliseconds (cumulative count 99995)
99.997% <= 3.903 milliseconds (cumulative count 99997)
99.998% <= 4.015 milliseconds (cumulative count 99999)
99.999% <= 4.095 milliseconds (cumulative count 100000)
100.000% <= 4.095 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.019% <= 0.607 milliseconds (cumulative count 19)
0.161% <= 0.703 milliseconds (cumulative count 161)
1.097% <= 0.807 milliseconds (cumulative count 1097)
4.756% <= 0.903 milliseconds (cumulative count 4756)
12.805% <= 1.007 milliseconds (cumulative count 12805)
21.699% <= 1.103 milliseconds (cumulative count 21699)
35.280% <= 1.207 milliseconds (cumulative count 35280)
48.049% <= 1.303 milliseconds (cumulative count 48049)
59.057% <= 1.407 milliseconds (cumulative count 59057)
67.335% <= 1.503 milliseconds (cumulative count 67335)
75.014% <= 1.607 milliseconds (cumulative count 75014)
81.462% <= 1.703 milliseconds (cumulative count 81462)
88.064% <= 1.807 milliseconds (cumulative count 88064)
93.164% <= 1.903 milliseconds (cumulative count 93164)
96.340% <= 2.007 milliseconds (cumulative count 96340)
97.709% <= 2.103 milliseconds (cumulative count 97709)
99.878% <= 3.103 milliseconds (cumulative count 99878)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 30459.95 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.380     0.528     1.327     1.959     2.351     4.095
====== ZADD ======                                                   
  100000 requests completed in 3.36 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.543 milliseconds (cumulative count 2)
50.000% <= 1.351 milliseconds (cumulative count 50019)
75.000% <= 1.655 milliseconds (cumulative count 75495)
87.500% <= 1.847 milliseconds (cumulative count 87664)
93.750% <= 1.967 milliseconds (cumulative count 93897)
96.875% <= 2.087 milliseconds (cumulative count 97012)
98.438% <= 2.239 milliseconds (cumulative count 98453)
99.219% <= 2.431 milliseconds (cumulative count 99223)
99.609% <= 2.671 milliseconds (cumulative count 99620)
99.805% <= 2.903 milliseconds (cumulative count 99805)
99.902% <= 3.151 milliseconds (cumulative count 99903)
99.951% <= 3.431 milliseconds (cumulative count 99952)
99.976% <= 3.607 milliseconds (cumulative count 99976)
99.988% <= 3.735 milliseconds (cumulative count 99988)
99.994% <= 3.887 milliseconds (cumulative count 99994)
99.997% <= 4.271 milliseconds (cumulative count 99997)
99.998% <= 4.479 milliseconds (cumulative count 99999)
99.999% <= 4.551 milliseconds (cumulative count 100000)
100.000% <= 4.551 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.012% <= 0.607 milliseconds (cumulative count 12)
0.109% <= 0.703 milliseconds (cumulative count 109)
0.700% <= 0.807 milliseconds (cumulative count 700)
3.436% <= 0.903 milliseconds (cumulative count 3436)
11.039% <= 1.007 milliseconds (cumulative count 11039)
19.481% <= 1.103 milliseconds (cumulative count 19481)
31.426% <= 1.207 milliseconds (cumulative count 31426)
44.400% <= 1.303 milliseconds (cumulative count 44400)
55.910% <= 1.407 milliseconds (cumulative count 55910)
64.393% <= 1.503 milliseconds (cumulative count 64393)
72.231% <= 1.607 milliseconds (cumulative count 72231)
78.618% <= 1.703 milliseconds (cumulative count 78618)
85.211% <= 1.807 milliseconds (cumulative count 85211)
90.886% <= 1.903 milliseconds (cumulative count 90886)
95.266% <= 2.007 milliseconds (cumulative count 95266)
97.258% <= 2.103 milliseconds (cumulative count 97258)
99.890% <= 3.103 milliseconds (cumulative count 99890)
99.996% <= 4.103 milliseconds (cumulative count 99996)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 29770.77 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.412     0.536     1.351     1.999     2.359     4.551
====== ZPOPMIN ======                                                   
  100000 requests completed in 3.27 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.535 milliseconds (cumulative count 1)
50.000% <= 1.319 milliseconds (cumulative count 50208)
75.000% <= 1.607 milliseconds (cumulative count 75447)
87.500% <= 1.799 milliseconds (cumulative count 87878)
93.750% <= 1.919 milliseconds (cumulative count 94009)
96.875% <= 2.023 milliseconds (cumulative count 96979)
98.438% <= 2.159 milliseconds (cumulative count 98471)
99.219% <= 2.351 milliseconds (cumulative count 99223)
99.609% <= 2.567 milliseconds (cumulative count 99619)
99.805% <= 2.783 milliseconds (cumulative count 99808)
99.902% <= 2.983 milliseconds (cumulative count 99903)
99.951% <= 3.183 milliseconds (cumulative count 99953)
99.976% <= 3.343 milliseconds (cumulative count 99977)
99.988% <= 3.455 milliseconds (cumulative count 99988)
99.994% <= 3.583 milliseconds (cumulative count 99994)
99.997% <= 3.647 milliseconds (cumulative count 99997)
99.998% <= 3.727 milliseconds (cumulative count 99999)
99.999% <= 3.815 milliseconds (cumulative count 100000)
100.000% <= 3.815 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.017% <= 0.607 milliseconds (cumulative count 17)
0.206% <= 0.703 milliseconds (cumulative count 206)
1.312% <= 0.807 milliseconds (cumulative count 1312)
5.080% <= 0.903 milliseconds (cumulative count 5080)
13.217% <= 1.007 milliseconds (cumulative count 13217)
22.350% <= 1.103 milliseconds (cumulative count 22350)
35.774% <= 1.207 milliseconds (cumulative count 35774)
48.358% <= 1.303 milliseconds (cumulative count 48358)
59.461% <= 1.407 milliseconds (cumulative count 59461)
67.741% <= 1.503 milliseconds (cumulative count 67741)
75.447% <= 1.607 milliseconds (cumulative count 75447)
81.783% <= 1.703 milliseconds (cumulative count 81783)
88.347% <= 1.807 milliseconds (cumulative count 88347)
93.341% <= 1.903 milliseconds (cumulative count 93341)
96.641% <= 2.007 milliseconds (cumulative count 96641)
98.062% <= 2.103 milliseconds (cumulative count 98062)
99.933% <= 3.103 milliseconds (cumulative count 99933)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 30581.04 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.373     0.528     1.319     1.951     2.279     3.815
====== LPUSH (needed to benchmark LRANGE) ======                                                   
  100000 requests completed in 3.35 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.535 milliseconds (cumulative count 1)
50.000% <= 1.351 milliseconds (cumulative count 50000)
75.000% <= 1.647 milliseconds (cumulative count 75432)
87.500% <= 1.839 milliseconds (cumulative count 87616)
93.750% <= 1.959 milliseconds (cumulative count 93857)
96.875% <= 2.071 milliseconds (cumulative count 96969)
98.438% <= 2.215 milliseconds (cumulative count 98441)
99.219% <= 2.415 milliseconds (cumulative count 99229)
99.609% <= 2.647 milliseconds (cumulative count 99618)
99.805% <= 2.847 milliseconds (cumulative count 99806)
99.902% <= 3.071 milliseconds (cumulative count 99905)
99.951% <= 3.279 milliseconds (cumulative count 99952)
99.976% <= 3.455 milliseconds (cumulative count 99976)
99.988% <= 3.591 milliseconds (cumulative count 99988)
99.994% <= 3.687 milliseconds (cumulative count 99994)
99.997% <= 3.807 milliseconds (cumulative count 99997)
99.998% <= 3.975 milliseconds (cumulative count 99999)
99.999% <= 4.015 milliseconds (cumulative count 100000)
100.000% <= 4.015 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.008% <= 0.607 milliseconds (cumulative count 8)
0.088% <= 0.703 milliseconds (cumulative count 88)
0.703% <= 0.807 milliseconds (cumulative count 703)
3.427% <= 0.903 milliseconds (cumulative count 3427)
10.508% <= 1.007 milliseconds (cumulative count 10508)
18.599% <= 1.103 milliseconds (cumulative count 18599)
30.867% <= 1.207 milliseconds (cumulative count 30867)
44.130% <= 1.303 milliseconds (cumulative count 44130)
56.055% <= 1.407 milliseconds (cumulative count 56055)
64.960% <= 1.503 milliseconds (cumulative count 64960)
72.707% <= 1.607 milliseconds (cumulative count 72707)
79.075% <= 1.703 milliseconds (cumulative count 79075)
85.624% <= 1.807 milliseconds (cumulative count 85624)
91.214% <= 1.903 milliseconds (cumulative count 91214)
95.524% <= 2.007 milliseconds (cumulative count 95524)
97.447% <= 2.103 milliseconds (cumulative count 97447)
99.919% <= 3.103 milliseconds (cumulative count 99919)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 29850.75 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.411     0.528     1.351     1.999     2.343     4.015
====== LRANGE_100 (first 100 elements) ======                                                   
  100000 requests completed in 3.95 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.495 milliseconds (cumulative count 1)
50.000% <= 1.143 milliseconds (cumulative count 51751)
75.000% <= 1.255 milliseconds (cumulative count 75350)
87.500% <= 1.351 milliseconds (cumulative count 87579)
93.750% <= 1.455 milliseconds (cumulative count 93932)
96.875% <= 1.575 milliseconds (cumulative count 96938)
98.438% <= 1.751 milliseconds (cumulative count 98409)
99.219% <= 1.991 milliseconds (cumulative count 99198)
99.609% <= 2.191 milliseconds (cumulative count 99582)
99.805% <= 2.359 milliseconds (cumulative count 99776)
99.902% <= 2.487 milliseconds (cumulative count 99875)
99.951% <= 2.599 milliseconds (cumulative count 99926)
99.976% <= 2.687 milliseconds (cumulative count 99947)
99.988% <= 2.775 milliseconds (cumulative count 99959)
99.994% <= 2.823 milliseconds (cumulative count 99965)
99.997% <= 2.967 milliseconds (cumulative count 99968)
99.998% <= 3.151 milliseconds (cumulative count 99970)
99.999% <= 3.303 milliseconds (cumulative count 99971)
100.000% <= 3.303 milliseconds (cumulative count 99971)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.503 milliseconds (cumulative count 1)
0.005% <= 0.607 milliseconds (cumulative count 5)
0.010% <= 0.703 milliseconds (cumulative count 10)
0.025% <= 0.807 milliseconds (cumulative count 25)
1.818% <= 0.903 milliseconds (cumulative count 1817)
17.157% <= 1.007 milliseconds (cumulative count 17152)
41.665% <= 1.103 milliseconds (cumulative count 41653)
66.304% <= 1.207 milliseconds (cumulative count 66285)
82.373% <= 1.303 milliseconds (cumulative count 82349)
91.696% <= 1.407 milliseconds (cumulative count 91669)
95.533% <= 1.503 milliseconds (cumulative count 95505)
97.383% <= 1.607 milliseconds (cumulative count 97355)
98.178% <= 1.703 milliseconds (cumulative count 98150)
98.673% <= 1.807 milliseconds (cumulative count 98644)
98.984% <= 1.903 milliseconds (cumulative count 98955)
99.263% <= 2.007 milliseconds (cumulative count 99234)
99.463% <= 2.103 milliseconds (cumulative count 99434)
99.998% <= 3.103 milliseconds (cumulative count 99969)
100.000% <= 4.103 milliseconds (cumulative count 99971)

Summary:
  throughput summary: 25297.24 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.168     0.488     1.143     1.487     1.911     3.303
====== LRANGE_300 (first 300 elements) ======                                                   
  100000 requests completed in 6.09 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 1.031 milliseconds (cumulative count 1)
50.000% <= 1.519 milliseconds (cumulative count 50562)
75.000% <= 1.631 milliseconds (cumulative count 75731)
87.500% <= 1.759 milliseconds (cumulative count 87702)
93.750% <= 1.975 milliseconds (cumulative count 93773)
96.875% <= 2.263 milliseconds (cumulative count 96909)
98.438% <= 2.519 milliseconds (cumulative count 98480)
99.219% <= 2.703 milliseconds (cumulative count 99228)
99.609% <= 2.887 milliseconds (cumulative count 99619)
99.805% <= 3.071 milliseconds (cumulative count 99807)
99.902% <= 3.263 milliseconds (cumulative count 99903)
99.951% <= 3.399 milliseconds (cumulative count 99953)
99.976% <= 3.543 milliseconds (cumulative count 99978)
99.988% <= 3.607 milliseconds (cumulative count 99988)
99.994% <= 3.679 milliseconds (cumulative count 99994)
99.997% <= 3.719 milliseconds (cumulative count 99997)
99.998% <= 3.783 milliseconds (cumulative count 99999)
99.999% <= 3.911 milliseconds (cumulative count 100000)
100.000% <= 3.911 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.005% <= 1.103 milliseconds (cumulative count 5)
0.015% <= 1.207 milliseconds (cumulative count 15)
0.103% <= 1.303 milliseconds (cumulative count 103)
14.618% <= 1.407 milliseconds (cumulative count 14618)
45.601% <= 1.503 milliseconds (cumulative count 45601)
71.794% <= 1.607 milliseconds (cumulative count 71794)
84.083% <= 1.703 milliseconds (cumulative count 84083)
89.685% <= 1.807 milliseconds (cumulative count 89685)
92.408% <= 1.903 milliseconds (cumulative count 92408)
94.267% <= 2.007 milliseconds (cumulative count 94267)
95.426% <= 2.103 milliseconds (cumulative count 95426)
99.831% <= 3.103 milliseconds (cumulative count 99831)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 16431.15 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.582     1.024     1.519     2.071     2.639     3.911
====== LRANGE_500 (first 500 elements) ======                                                   
  100000 requests completed in 7.70 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 1.223 milliseconds (cumulative count 1)
50.000% <= 1.927 milliseconds (cumulative count 50776)
75.000% <= 2.047 milliseconds (cumulative count 75896)
87.500% <= 2.167 milliseconds (cumulative count 87704)
93.750% <= 2.327 milliseconds (cumulative count 93935)
96.875% <= 2.551 milliseconds (cumulative count 96878)
98.438% <= 2.823 milliseconds (cumulative count 98454)
99.219% <= 3.071 milliseconds (cumulative count 99225)
99.609% <= 3.311 milliseconds (cumulative count 99623)
99.805% <= 3.567 milliseconds (cumulative count 99809)
99.902% <= 3.839 milliseconds (cumulative count 99907)
99.951% <= 4.335 milliseconds (cumulative count 99952)
99.976% <= 5.079 milliseconds (cumulative count 99976)
99.988% <= 5.255 milliseconds (cumulative count 99988)
99.994% <= 5.695 milliseconds (cumulative count 99994)
99.997% <= 6.919 milliseconds (cumulative count 99997)
99.998% <= 7.191 milliseconds (cumulative count 99999)
99.999% <= 7.287 milliseconds (cumulative count 100000)
100.000% <= 7.287 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.002% <= 1.303 milliseconds (cumulative count 2)
0.005% <= 1.503 milliseconds (cumulative count 5)
0.063% <= 1.607 milliseconds (cumulative count 63)
2.875% <= 1.703 milliseconds (cumulative count 2875)
18.894% <= 1.807 milliseconds (cumulative count 18894)
44.315% <= 1.903 milliseconds (cumulative count 44315)
69.140% <= 2.007 milliseconds (cumulative count 69140)
82.754% <= 2.103 milliseconds (cumulative count 82754)
99.287% <= 3.103 milliseconds (cumulative count 99287)
99.937% <= 4.103 milliseconds (cumulative count 99937)
99.977% <= 5.103 milliseconds (cumulative count 99977)
99.996% <= 6.103 milliseconds (cumulative count 99996)
99.998% <= 7.103 milliseconds (cumulative count 99998)
100.000% <= 8.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 12983.64 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.975     1.216     1.927     2.391     2.967     7.287
====== LRANGE_600 (first 600 elements) ======                                                   
  100000 requests completed in 8.57 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 1.223 milliseconds (cumulative count 1)
50.000% <= 2.103 milliseconds (cumulative count 51218)
75.000% <= 2.263 milliseconds (cumulative count 75726)
87.500% <= 2.447 milliseconds (cumulative count 87541)
93.750% <= 2.703 milliseconds (cumulative count 93789)
96.875% <= 3.007 milliseconds (cumulative count 96878)
98.438% <= 3.295 milliseconds (cumulative count 98438)
99.219% <= 3.623 milliseconds (cumulative count 99220)
99.609% <= 3.967 milliseconds (cumulative count 99614)
99.805% <= 4.223 milliseconds (cumulative count 99806)
99.902% <= 4.703 milliseconds (cumulative count 99904)
99.951% <= 5.207 milliseconds (cumulative count 99952)
99.976% <= 5.671 milliseconds (cumulative count 99976)
99.988% <= 5.879 milliseconds (cumulative count 99988)
99.994% <= 6.047 milliseconds (cumulative count 99994)
99.997% <= 6.175 milliseconds (cumulative count 99997)
99.998% <= 6.279 milliseconds (cumulative count 99999)
99.999% <= 6.343 milliseconds (cumulative count 100000)
100.000% <= 6.343 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.003% <= 1.303 milliseconds (cumulative count 3)
0.007% <= 1.407 milliseconds (cumulative count 7)
0.009% <= 1.503 milliseconds (cumulative count 9)
0.011% <= 1.607 milliseconds (cumulative count 11)
0.015% <= 1.703 milliseconds (cumulative count 15)
0.215% <= 1.807 milliseconds (cumulative count 215)
4.411% <= 1.903 milliseconds (cumulative count 4411)
25.577% <= 2.007 milliseconds (cumulative count 25577)
51.218% <= 2.103 milliseconds (cumulative count 51218)
97.538% <= 3.103 milliseconds (cumulative count 97538)
99.747% <= 4.103 milliseconds (cumulative count 99747)
99.948% <= 5.103 milliseconds (cumulative count 99948)
99.994% <= 6.103 milliseconds (cumulative count 99994)
100.000% <= 7.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 11665.89 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        2.189     1.216     2.103     2.799     3.519     6.343
====== MSET (10 keys) ======                                                   
  100000 requests completed in 3.54 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.687 milliseconds (cumulative count 2)
50.000% <= 1.407 milliseconds (cumulative count 50528)
75.000% <= 1.735 milliseconds (cumulative count 75034)
87.500% <= 1.943 milliseconds (cumulative count 87702)
93.750% <= 2.095 milliseconds (cumulative count 93882)
96.875% <= 2.319 milliseconds (cumulative count 96940)
98.438% <= 2.591 milliseconds (cumulative count 98457)
99.219% <= 2.895 milliseconds (cumulative count 99223)
99.609% <= 3.191 milliseconds (cumulative count 99616)
99.805% <= 3.551 milliseconds (cumulative count 99805)
99.902% <= 3.839 milliseconds (cumulative count 99905)
99.951% <= 4.135 milliseconds (cumulative count 99952)
99.976% <= 4.327 milliseconds (cumulative count 99976)
99.988% <= 4.551 milliseconds (cumulative count 99988)
99.994% <= 4.791 milliseconds (cumulative count 99994)
99.997% <= 4.871 milliseconds (cumulative count 99998)
99.998% <= 4.911 milliseconds (cumulative count 99999)
99.999% <= 4.935 milliseconds (cumulative count 100000)
100.000% <= 4.935 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.007% <= 0.703 milliseconds (cumulative count 7)
0.269% <= 0.807 milliseconds (cumulative count 269)
2.118% <= 0.903 milliseconds (cumulative count 2118)
8.886% <= 1.007 milliseconds (cumulative count 8886)
16.891% <= 1.103 milliseconds (cumulative count 16891)
26.555% <= 1.207 milliseconds (cumulative count 26555)
38.946% <= 1.303 milliseconds (cumulative count 38946)
50.528% <= 1.407 milliseconds (cumulative count 50528)
58.852% <= 1.503 milliseconds (cumulative count 58852)
66.651% <= 1.607 milliseconds (cumulative count 66651)
73.043% <= 1.703 milliseconds (cumulative count 73043)
79.473% <= 1.807 milliseconds (cumulative count 79473)
85.364% <= 1.903 milliseconds (cumulative count 85364)
91.056% <= 2.007 milliseconds (cumulative count 91056)
94.076% <= 2.103 milliseconds (cumulative count 94076)
99.534% <= 3.103 milliseconds (cumulative count 99534)
99.950% <= 4.103 milliseconds (cumulative count 99950)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 28248.59 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.483     0.680     1.407     2.151     2.783     4.935

root@3dc9d53afef6:/data# ^C
root@3dc9d53afef6:/data# exit
observability-stats $ 
```

I was running benchmark as the exercise said and I ran the commands -

```bash
observability-stats $ docker-compose exec redis_stats bash
root@3dc9d53afef6:/data# redis-cli info
# Server
redis_version:6.2.5
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:69ab6eec4665acbc
redis_mode:standalone
os:Linux 5.10.47-linuxkit x86_64
arch_bits:64
multiplexing_api:epoll
atomicvar_api:c11-builtin
gcc_version:8.3.0
process_id:1
process_supervised:no
run_id:c8d62ab9ad8e3384d7144cf23a3a67bb629f0a31
tcp_port:6379
server_time_usec:1629655117533994
uptime_in_seconds:132
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:2265165
executable:/data/redis-server
config_file:
io_threads_active:0

# Clients
connected_clients:1
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:0
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:1376928
used_memory_human:1.31M
used_memory_rss:11141120
used_memory_rss_human:10.62M
used_memory_peak:4912720
used_memory_peak_human:4.69M
used_memory_peak_perc:28.03%
used_memory_overhead:810072
used_memory_startup:809880
used_memory_dataset:566856
used_memory_dataset_perc:99.97%
allocator_allocated:1791616
allocator_active:2146304
allocator_resident:8036352
total_system_memory:10447507456
total_system_memory_human:9.73G
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.20
allocator_frag_bytes:354688
allocator_rss_ratio:3.74
allocator_rss_bytes:5890048
rss_overhead_ratio:1.39
rss_overhead_bytes:3104768
mem_fragmentation_ratio:8.48
mem_fragmentation_bytes:9827904
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:0
mem_aof_buffer:0
mem_allocator:jemalloc-5.1.0
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:783250
rdb_bgsave_in_progress:0
rdb_last_save_time:1629655107
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:856064
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:1002
total_commands_processed:2000002
instantaneous_ops_per_sec:0
total_net_input_bytes:104000091
total_net_output_bytes:1362866814
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:11
evicted_keys:0
keyspace_hits:500000
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:485
total_forks:2
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:0
dump_payload_sanitizations:0
total_reads_processed:2001003
total_writes_processed:2000001
io_threaded_reads_processed:0
io_threaded_writes_processed:0

# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:784356888003ee4c56ba78bc7c080bd523cf1f9d
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:66.833675
used_cpu_user:13.635417
used_cpu_sys_children:0.005382
used_cpu_user_children:0.004290
used_cpu_sys_main_thread:66.822881
used_cpu_user_main_thread:13.633954

# Modules

# Errorstats

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=4,expires=0,avg_ttl=0
root@3dc9d53afef6:/data# redis-cli config set maxmemory 100000
OK
root@3dc9d53afef6:/data# redis-cli INFO | grep used_memory:
used_memory:1376928
root@3dc9d53afef6:/data# redis-cli CONFIG GET maxmemory
1) "maxmemory"
2) "100000"
root@3dc9d53afef6:/data# redis-cli info clients
# Clients
connected_clients:1
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:0
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0
root@3dc9d53afef6:/data# redis-cli info clients | grep connected_clients
connected_clients:1
root@3dc9d53afef6:/data# redis-cli info stats
# Stats
total_connections_received:1008
total_commands_processed:2000008
instantaneous_ops_per_sec:0
total_net_input_bytes:104000276
total_net_output_bytes:1362875567
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:18
evicted_keys:0
keyspace_hits:500000
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:485
total_forks:2
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:0
dump_payload_sanitizations:0
total_reads_processed:2001015
total_writes_processed:2000007
io_threaded_reads_processed:0
io_threaded_writes_processed:0
root@3dc9d53afef6:/data# redis-cli INFO stats | grep keyspace 
keyspace_hits:500000
keyspace_misses:0
root@3dc9d53afef6:/data# redis-cli INFO stats | grep evicted_keys
evicted_keys:0
root@3dc9d53afef6:/data# redis-cli INFO stats | grep expired_keys
expired_keys:0
root@3dc9d53afef6:/data# redis-cli INFO keyspace
# Keyspace
db0:keys=4,expires=0,avg_ttl=0
root@3dc9d53afef6:/data# redis-cli INFO keyspace
# Keyspace
db0:keys=4,expires=0,avg_ttl=0
root@3dc9d53afef6:/data# redis-cli INFO keyspace
# Keyspace
db0:keys=4,expires=0,avg_ttl=0
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1015
total_commands_processed:2000015
total_net_input_bytes:104000460
total_net_output_bytes:1362879712
total_forks:3
total_error_replies:0
total_reads_processed:2001029
total_writes_processed:2000014
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1016
total_commands_processed:2000016
total_net_input_bytes:104000485
total_net_output_bytes:1362880710
total_forks:3
total_error_replies:0
total_reads_processed:2001031
total_writes_processed:2000015
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1017
total_commands_processed:2000017
total_net_input_bytes:104000510
total_net_output_bytes:1362881708
total_forks:3
total_error_replies:0
total_reads_processed:2001033
total_writes_processed:2000016
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1018
total_commands_processed:2000018
total_net_input_bytes:104000535
total_net_output_bytes:1362882706
total_forks:3
total_error_replies:0
total_reads_processed:2001035
total_writes_processed:2000017
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1019
total_commands_processed:2000019
total_net_input_bytes:104000560
total_net_output_bytes:1362883704
total_forks:3
total_error_replies:0
total_reads_processed:2001037
total_writes_processed:2000018
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1020
total_commands_processed:2000020
total_net_input_bytes:104000585
total_net_output_bytes:1362884702
total_forks:3
total_error_replies:0
total_reads_processed:2001039
total_writes_processed:2000019
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1021
total_commands_processed:2000021
total_net_input_bytes:104000610
total_net_output_bytes:1362885700
total_forks:3
total_error_replies:0
total_reads_processed:2001041
total_writes_processed:2000020
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1022
total_commands_processed:2000022
total_net_input_bytes:104000635
total_net_output_bytes:1362886698
total_forks:3
total_error_replies:0
total_reads_processed:2001043
total_writes_processed:2000021
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1023
total_commands_processed:2000023
total_net_input_bytes:104000660
total_net_output_bytes:1362887696
total_forks:3
total_error_replies:0
total_reads_processed:2001045
total_writes_processed:2000022
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1024
total_commands_processed:2000024
total_net_input_bytes:104000685
total_net_output_bytes:1362888694
total_forks:3
total_error_replies:0
total_reads_processed:2001047
total_writes_processed:2000023
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1025
total_commands_processed:2000025
total_net_input_bytes:104000710
total_net_output_bytes:1362889692
total_forks:3
total_error_replies:0
total_reads_processed:2001049
total_writes_processed:2000024
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1026
total_commands_processed:2000026
total_net_input_bytes:104000735
total_net_output_bytes:1362890690
total_forks:3
total_error_replies:0
total_reads_processed:2001051
total_writes_processed:2000025
root@3dc9d53afef6:/data# redis-cli INFO stats | egrep "^total_"
total_connections_received:1027
total_commands_processed:2000027
total_net_input_bytes:104000760
total_net_output_bytes:1362891688
total_forks:3
total_error_replies:0
total_reads_processed:2001053
total_writes_processed:2000026
root@3dc9d53afef6:/data# 
```

It's cool to see that the redis-server received a 1027 connections and maybe a bit more, while I was running the `redis-cli INFO stats | egrep "^total_"` command

`2000027` commands processed!! wow! That's 20 lakhs! More like 2 million commands! Wow

Wow, I tried benchmark again and it stopped

```bash
observability-stats $ docker-compose exec redis_stats redis-benchmark
====== PING_INLINE ======                                                   
  100000 requests completed in 3.21 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.503 milliseconds (cumulative count 1)
50.000% <= 1.279 milliseconds (cumulative count 50703)
75.000% <= 1.575 milliseconds (cumulative count 75448)
87.500% <= 1.751 milliseconds (cumulative count 87512)
93.750% <= 1.871 milliseconds (cumulative count 93948)
96.875% <= 2.023 milliseconds (cumulative count 96912)
98.438% <= 2.207 milliseconds (cumulative count 98442)
99.219% <= 2.423 milliseconds (cumulative count 99228)
99.609% <= 2.623 milliseconds (cumulative count 99619)
99.805% <= 2.839 milliseconds (cumulative count 99811)
99.902% <= 3.103 milliseconds (cumulative count 99903)
99.951% <= 3.351 milliseconds (cumulative count 99953)
99.976% <= 3.559 milliseconds (cumulative count 99976)
99.988% <= 3.759 milliseconds (cumulative count 99988)
99.994% <= 3.919 milliseconds (cumulative count 99994)
99.997% <= 4.119 milliseconds (cumulative count 99997)
99.998% <= 4.303 milliseconds (cumulative count 99999)
99.999% <= 4.327 milliseconds (cumulative count 100000)
100.000% <= 4.327 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.503 milliseconds (cumulative count 1)
0.011% <= 0.607 milliseconds (cumulative count 11)
0.145% <= 0.703 milliseconds (cumulative count 145)
1.797% <= 0.807 milliseconds (cumulative count 1797)
7.869% <= 0.903 milliseconds (cumulative count 7869)
17.608% <= 1.007 milliseconds (cumulative count 17608)
27.296% <= 1.103 milliseconds (cumulative count 27296)
41.914% <= 1.207 milliseconds (cumulative count 41914)
53.245% <= 1.303 milliseconds (cumulative count 53245)
62.750% <= 1.407 milliseconds (cumulative count 62750)
70.300% <= 1.503 milliseconds (cumulative count 70300)
77.772% <= 1.607 milliseconds (cumulative count 77772)
84.296% <= 1.703 milliseconds (cumulative count 84296)
91.015% <= 1.807 milliseconds (cumulative count 91015)
94.853% <= 1.903 milliseconds (cumulative count 94853)
96.713% <= 2.007 milliseconds (cumulative count 96713)
97.736% <= 2.103 milliseconds (cumulative count 97736)
99.903% <= 3.103 milliseconds (cumulative count 99903)
99.996% <= 4.103 milliseconds (cumulative count 99996)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 31133.25 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.336     0.496     1.279     1.911     2.343     4.327
====== PING_MBULK ======                                                   
  100000 requests completed in 3.22 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.535 milliseconds (cumulative count 1)
50.000% <= 1.271 milliseconds (cumulative count 50146)
75.000% <= 1.567 milliseconds (cumulative count 75205)
87.500% <= 1.759 milliseconds (cumulative count 88018)
93.750% <= 1.871 milliseconds (cumulative count 93768)
96.875% <= 2.039 milliseconds (cumulative count 96922)
98.438% <= 2.263 milliseconds (cumulative count 98440)
99.219% <= 2.543 milliseconds (cumulative count 99223)
99.609% <= 2.847 milliseconds (cumulative count 99614)
99.805% <= 3.151 milliseconds (cumulative count 99807)
99.902% <= 3.407 milliseconds (cumulative count 99904)
99.951% <= 3.647 milliseconds (cumulative count 99953)
99.976% <= 3.895 milliseconds (cumulative count 99976)
99.988% <= 4.095 milliseconds (cumulative count 99988)
99.994% <= 4.399 milliseconds (cumulative count 99994)
99.997% <= 4.543 milliseconds (cumulative count 99997)
99.998% <= 4.615 milliseconds (cumulative count 99999)
99.999% <= 4.671 milliseconds (cumulative count 100000)
100.000% <= 4.671 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.013% <= 0.607 milliseconds (cumulative count 13)
0.182% <= 0.703 milliseconds (cumulative count 182)
1.992% <= 0.807 milliseconds (cumulative count 1992)
7.943% <= 0.903 milliseconds (cumulative count 7943)
17.449% <= 1.007 milliseconds (cumulative count 17449)
27.257% <= 1.103 milliseconds (cumulative count 27257)
41.949% <= 1.207 milliseconds (cumulative count 41949)
53.593% <= 1.303 milliseconds (cumulative count 53593)
63.148% <= 1.407 milliseconds (cumulative count 63148)
70.638% <= 1.503 milliseconds (cumulative count 70638)
77.933% <= 1.607 milliseconds (cumulative count 77933)
84.340% <= 1.703 milliseconds (cumulative count 84340)
90.909% <= 1.807 milliseconds (cumulative count 90909)
94.744% <= 1.903 milliseconds (cumulative count 94744)
96.543% <= 2.007 milliseconds (cumulative count 96543)
97.512% <= 2.103 milliseconds (cumulative count 97512)
99.786% <= 3.103 milliseconds (cumulative count 99786)
99.989% <= 4.103 milliseconds (cumulative count 99989)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 31026.99 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.338     0.528     1.271     1.919     2.439     4.671
Error from server: OOM command not allowed when used memory > 'maxmemory'.
observability-stats $ 
```

Gotta check what that means. `Error from server: OOM command not allowed when used memory > 'maxmemory'.`

Why would they call it the OOM command? Out of Memory command? Is that the benchmark command? Idk

```bash
root@3dc9d53afef6:/data# redis-cli latency
(error) ERR wrong number of arguments for 'latency' command
root@3dc9d53afef6:/data# redis-cli latency doctor
I'm sorry, Dave, I can't do that. Latency monitoring is disabled in this Redis instance. You may use "CONFIG SET latency-monitor-threshold <milliseconds>." in order to enable it. If we weren't in a deep space mission I'd suggest to take a look at https://redis.io/topics/latency-monitor.
root@3dc9d53afef6:/data# redis-cli config set latency-montior-threshold 1
(error) ERR Unsupported CONFIG parameter: latency-montior-threshold
root@3dc9d53afef6:/data# redis-cli config set latency-monitor-threshold 1
OK
root@3dc9d53afef6:/data# redis-cli latency doctor
Dave, no latency spike was observed during the lifetime of this Redis instance, not in the slightest bit. I honestly think you ought to sit down calmly, take a stress pill, and think things over.
root@3dc9d53afef6:/data# redis-cli latency history
(error) ERR Unknown subcommand or wrong number of arguments for 'history'. Try LATENCY HELP.
root@3dc9d53afef6:/data# redis-cli latency latest
(empty array)
root@3dc9d53afef6:/data# redis-cli latency latest
(empty array)
root@3dc9d53afef6:/data# 
```

```bash
root@3dc9d53afef6:/data# redis-cli INFO | grep used_memory:
used_memory:1377024
root@3dc9d53afef6:/data# 
```

That's a lot of used memory I guess. Hmm

Actually it's just 1.3 MB. But in bytes it looks bigger, hmm

I'm thinking if the max memory I set is 0.1 MB because I set 100000 and I think it maybe 100000 bytes, hmm

Probably that's why the OOM thing? Hmm

Time to check some units ;) [TODO]

```bash
observability-stats $ docker-compose ps
NAME                                COMMAND                  SERVICE             STATUS              PORTS
observability-stats_redis_stats_1   "docker-entrypoint.s…"   redis_stats         running             0.0.0.0:6379->6379/tcp, :::6379->6379/tcp
observability-stats $ docker-compose stop 
[+] Running 1/1
 ⠿ Container observability-stats_redis_stats_1  Stopped                                                         0.2s
observability-stats $ docker-compose ps
NAME                                COMMAND                  SERVICE             STATUS              PORTS
observability-stats_redis_stats_1   "docker-entrypoint.s…"   redis_stats         exited (0)          
observability-stats $ docker ps -a
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS                     PORTS     NAMES
3dc9d53afef6   redis:6.2   "docker-entrypoint.s…"   12 minutes ago   Exited (0) 4 seconds ago             observability-stats_redis_stats_1
observability-stats $ 
```
