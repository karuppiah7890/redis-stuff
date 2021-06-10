# Chapter 2: Explore meaning of all redis binaries


Explore -

redis-benchmark
redis-check-aof
redis-check-rdb
redis-cli
redis-sentinel
redis-server

---

reds-benchmark

I'm starting with redis-benchmark . Like the name, it is used to benchmark the
redis server

```bash
$ redis-benchmark 
====== PING_INLINE ======                                                   
  100000 requests completed in 2.57 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.271 milliseconds (cumulative count 2)
50.000% <= 0.647 milliseconds (cumulative count 54384)
75.000% <= 0.703 milliseconds (cumulative count 76200)
87.500% <= 0.807 milliseconds (cumulative count 87879)
93.750% <= 0.975 milliseconds (cumulative count 93795)
96.875% <= 1.127 milliseconds (cumulative count 96957)
98.438% <= 1.319 milliseconds (cumulative count 98472)
99.219% <= 1.511 milliseconds (cumulative count 99231)
99.609% <= 1.719 milliseconds (cumulative count 99610)
99.805% <= 1.951 milliseconds (cumulative count 99805)
99.902% <= 2.175 milliseconds (cumulative count 99904)
99.951% <= 2.503 milliseconds (cumulative count 99952)
99.976% <= 2.711 milliseconds (cumulative count 99976)
99.988% <= 2.903 milliseconds (cumulative count 99989)
99.994% <= 2.967 milliseconds (cumulative count 99996)
99.997% <= 2.983 milliseconds (cumulative count 99997)
99.998% <= 3.047 milliseconds (cumulative count 99999)
99.999% <= 3.111 milliseconds (cumulative count 100000)
100.000% <= 3.111 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.003% <= 0.303 milliseconds (cumulative count 3)
0.010% <= 0.407 milliseconds (cumulative count 10)
0.091% <= 0.503 milliseconds (cumulative count 91)
16.490% <= 0.607 milliseconds (cumulative count 16490)
76.200% <= 0.703 milliseconds (cumulative count 76200)
87.879% <= 0.807 milliseconds (cumulative count 87879)
91.569% <= 0.903 milliseconds (cumulative count 91569)
94.734% <= 1.007 milliseconds (cumulative count 94734)
96.635% <= 1.103 milliseconds (cumulative count 96635)
97.799% <= 1.207 milliseconds (cumulative count 97799)
98.390% <= 1.303 milliseconds (cumulative count 98390)
98.891% <= 1.407 milliseconds (cumulative count 98891)
99.214% <= 1.503 milliseconds (cumulative count 99214)
99.436% <= 1.607 milliseconds (cumulative count 99436)
99.585% <= 1.703 milliseconds (cumulative count 99585)
99.711% <= 1.807 milliseconds (cumulative count 99711)
99.778% <= 1.903 milliseconds (cumulative count 99778)
99.833% <= 2.007 milliseconds (cumulative count 99833)
99.873% <= 2.103 milliseconds (cumulative count 99873)
99.999% <= 3.103 milliseconds (cumulative count 99999)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 38895.37 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.697     0.264     0.647     1.023     1.439     3.111
====== PING_MBULK ======                                                   
  100000 requests completed in 2.60 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.367 milliseconds (cumulative count 1)
50.000% <= 0.647 milliseconds (cumulative count 50236)
75.000% <= 0.703 milliseconds (cumulative count 75990)
87.500% <= 0.799 milliseconds (cumulative count 88048)
93.750% <= 0.959 milliseconds (cumulative count 93955)
96.875% <= 1.095 milliseconds (cumulative count 97002)
98.438% <= 1.263 milliseconds (cumulative count 98469)
99.219% <= 1.495 milliseconds (cumulative count 99220)
99.609% <= 1.695 milliseconds (cumulative count 99624)
99.805% <= 1.847 milliseconds (cumulative count 99814)
99.902% <= 1.967 milliseconds (cumulative count 99903)
99.951% <= 2.047 milliseconds (cumulative count 99952)
99.976% <= 2.215 milliseconds (cumulative count 99976)
99.988% <= 2.383 milliseconds (cumulative count 99988)
99.994% <= 2.439 milliseconds (cumulative count 99994)
99.997% <= 2.487 milliseconds (cumulative count 99997)
99.998% <= 2.591 milliseconds (cumulative count 100000)
100.000% <= 2.591 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.006% <= 0.407 milliseconds (cumulative count 6)
0.046% <= 0.503 milliseconds (cumulative count 46)
10.380% <= 0.607 milliseconds (cumulative count 10380)
75.990% <= 0.703 milliseconds (cumulative count 75990)
88.578% <= 0.807 milliseconds (cumulative count 88578)
92.174% <= 0.903 milliseconds (cumulative count 92174)
95.279% <= 1.007 milliseconds (cumulative count 95279)
97.111% <= 1.103 milliseconds (cumulative count 97111)
98.100% <= 1.207 milliseconds (cumulative count 98100)
98.648% <= 1.303 milliseconds (cumulative count 98648)
99.008% <= 1.407 milliseconds (cumulative count 99008)
99.239% <= 1.503 milliseconds (cumulative count 99239)
99.468% <= 1.607 milliseconds (cumulative count 99468)
99.636% <= 1.703 milliseconds (cumulative count 99636)
99.784% <= 1.807 milliseconds (cumulative count 99784)
99.860% <= 1.903 milliseconds (cumulative count 99860)
99.926% <= 2.007 milliseconds (cumulative count 99926)
99.964% <= 2.103 milliseconds (cumulative count 99964)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 38476.34 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.697     0.360     0.647     0.999     1.407     2.591
^CT: rps=39430.3 (overall: 39204.1) avg_msec=0.692 (overall: 0.690)
```

```bash
$ redis-benchmark -h
Invalid option "-h" or option argument missing

Usage: redis-benchmark [-h <host>] [-p <port>] [-c <clients>] [-n <requests>] [-k <boolean>]

 -h <hostname>      Server hostname (default 127.0.0.1)
 -p <port>          Server port (default 6379)
 -s <socket>        Server socket (overrides host and port)
 -a <password>      Password for Redis Auth
 --user <username>  Used to send ACL style 'AUTH username pass'. Needs -a.
 -c <clients>       Number of parallel connections (default 50)
 -n <requests>      Total number of requests (default 100000)
 -d <size>          Data size of SET/GET value in bytes (default 3)
 --dbnum <db>       SELECT the specified db number (default 0)
 --threads <num>    Enable multi-thread mode.
 --cluster          Enable cluster mode.
 --enable-tracking  Send CLIENT TRACKING on before starting benchmark.
 -k <boolean>       1=keep alive 0=reconnect (default 1)
 -r <keyspacelen>   Use random keys for SET/GET/INCR, random values for SADD,
                    random members and scores for ZADD.
  Using this option the benchmark will expand the string __rand_int__
  inside an argument with a 12 digits number in the specified range
  from 0 to keyspacelen-1. The substitution changes every time a command
  is executed. Default tests use this to hit random keys in the
  specified range.
 -P <numreq>        Pipeline <numreq> requests. Default 1 (no pipeline).
 -e                 If server replies with errors, show them on stdout.
                    (no more than 1 error per second is displayed)
 -q                 Quiet. Just show query/sec values
 --precision        Number of decimal places to display in latency output (default 0)
 --csv              Output in CSV format
 -l                 Loop. Run the tests forever
 -t <tests>         Only run the comma separated list of tests. The test
                    names are the same as the ones produced as output.
 -I                 Idle mode. Just open N idle connections and wait.
 --tls              Establish a secure TLS connection.
 --sni <host>       Server name indication for TLS.
 --cacert <file>    CA Certificate file to verify with.
 --cacertdir <dir>  Directory where trusted CA certificates are stored.
                    If neither cacert nor cacertdir are specified, the default
                    system-wide trusted root certs configuration will apply.
 --insecure         Allow insecure TLS connection by skipping cert validation.
 --cert <file>      Client certificate to authenticate with.
 --key <file>       Private key file to authenticate with.
 --tls-ciphers <list> Sets the list of prefered ciphers (TLSv1.2 and below)
                    in order of preference from highest to lowest separated by colon (":").
                    See the ciphers(1ssl) manpage for more information about the syntax of this string.
 --tls-ciphersuites <list> Sets the list of prefered ciphersuites (TLSv1.3)
                    in order of preference from highest to lowest separated by colon (":").
                    See the ciphers(1ssl) manpage for more information about the syntax of this string,
                    and specifically for TLSv1.3 ciphersuites.
 --help             Output this help and exit.
 --version          Output version and exit.

Examples:

 Run the benchmark with the default configuration against 127.0.0.1:6379:
   $ redis-benchmark

 Use 20 parallel clients, for a total of 100k requests, against 192.168.1.1:
   $ redis-benchmark -h 192.168.1.1 -p 6379 -n 100000 -c 20

 Fill 127.0.0.1:6379 with about 1 million keys only using the SET test:
   $ redis-benchmark -t set -n 1000000 -r 100000000

 Benchmark 127.0.0.1:6379 for a few commands producing CSV output:
   $ redis-benchmark -t ping,set,get -n 100000 --csv

 Benchmark a specific command line:
   $ redis-benchmark -r 10000 -n 10000 eval 'return redis.call("ping")' 0

 Fill a list with 10000 random elements:
   $ redis-benchmark -r 10000 -n 10000 lpush mylist __rand_int__

 On user specified command lines __rand_int__ is replaced with a random integer
 with a range of values selected by the -r option. 
```

I actually stopped the benchmark in between, but the full one takes only a few
moments to complete

```bash
$ redis-benchmark
====== PING_INLINE ======                                                   
  100000 requests completed in 2.53 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.335 milliseconds (cumulative count 1)
50.000% <= 0.639 milliseconds (cumulative count 53049)
75.000% <= 0.687 milliseconds (cumulative count 76389)
87.500% <= 0.775 milliseconds (cumulative count 87633)
93.750% <= 0.935 milliseconds (cumulative count 93832)
96.875% <= 1.127 milliseconds (cumulative count 96957)
98.438% <= 1.311 milliseconds (cumulative count 98468)
99.219% <= 1.471 milliseconds (cumulative count 99225)
99.609% <= 1.639 milliseconds (cumulative count 99611)
99.805% <= 1.799 milliseconds (cumulative count 99809)
99.902% <= 1.919 milliseconds (cumulative count 99904)
99.951% <= 2.039 milliseconds (cumulative count 99952)
99.976% <= 2.167 milliseconds (cumulative count 99976)
99.988% <= 2.239 milliseconds (cumulative count 99988)
99.994% <= 2.311 milliseconds (cumulative count 99994)
99.997% <= 2.359 milliseconds (cumulative count 99997)
99.998% <= 2.471 milliseconds (cumulative count 99999)
99.999% <= 2.527 milliseconds (cumulative count 100000)
100.000% <= 2.527 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.011% <= 0.407 milliseconds (cumulative count 11)
0.073% <= 0.503 milliseconds (cumulative count 73)
19.124% <= 0.607 milliseconds (cumulative count 19124)
79.863% <= 0.703 milliseconds (cumulative count 79863)
89.437% <= 0.807 milliseconds (cumulative count 89437)
93.096% <= 0.903 milliseconds (cumulative count 93096)
95.158% <= 1.007 milliseconds (cumulative count 95158)
96.653% <= 1.103 milliseconds (cumulative count 96653)
97.699% <= 1.207 milliseconds (cumulative count 97699)
98.428% <= 1.303 milliseconds (cumulative count 98428)
98.957% <= 1.407 milliseconds (cumulative count 98957)
99.307% <= 1.503 milliseconds (cumulative count 99307)
99.551% <= 1.607 milliseconds (cumulative count 99551)
99.710% <= 1.703 milliseconds (cumulative count 99710)
99.818% <= 1.807 milliseconds (cumulative count 99818)
99.898% <= 1.903 milliseconds (cumulative count 99898)
99.944% <= 2.007 milliseconds (cumulative count 99944)
99.962% <= 2.103 milliseconds (cumulative count 99962)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39556.96 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.686     0.328     0.639     0.999     1.423     2.527
====== PING_MBULK ======                                                   
  100000 requests completed in 2.64 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.335 milliseconds (cumulative count 1)
50.000% <= 0.655 milliseconds (cumulative count 54194)
75.000% <= 0.711 milliseconds (cumulative count 76324)
87.500% <= 0.831 milliseconds (cumulative count 87783)
93.750% <= 0.999 milliseconds (cumulative count 93801)
96.875% <= 1.191 milliseconds (cumulative count 96908)
98.438% <= 1.383 milliseconds (cumulative count 98476)
99.219% <= 1.551 milliseconds (cumulative count 99230)
99.609% <= 1.711 milliseconds (cumulative count 99615)
99.805% <= 1.863 milliseconds (cumulative count 99806)
99.902% <= 1.983 milliseconds (cumulative count 99908)
99.951% <= 2.087 milliseconds (cumulative count 99952)
99.976% <= 2.183 milliseconds (cumulative count 99976)
99.988% <= 2.271 milliseconds (cumulative count 99988)
99.994% <= 2.343 milliseconds (cumulative count 99994)
99.997% <= 2.447 milliseconds (cumulative count 99997)
99.998% <= 2.503 milliseconds (cumulative count 99999)
99.999% <= 2.543 milliseconds (cumulative count 100000)
100.000% <= 2.543 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.005% <= 0.407 milliseconds (cumulative count 5)
0.033% <= 0.503 milliseconds (cumulative count 33)
8.344% <= 0.607 milliseconds (cumulative count 8344)
74.626% <= 0.703 milliseconds (cumulative count 74626)
86.429% <= 0.807 milliseconds (cumulative count 86429)
90.999% <= 0.903 milliseconds (cumulative count 90999)
93.973% <= 1.007 milliseconds (cumulative count 93973)
95.773% <= 1.103 milliseconds (cumulative count 95773)
97.076% <= 1.207 milliseconds (cumulative count 97076)
97.929% <= 1.303 milliseconds (cumulative count 97929)
98.605% <= 1.407 milliseconds (cumulative count 98605)
99.046% <= 1.503 milliseconds (cumulative count 99046)
99.399% <= 1.607 milliseconds (cumulative count 99399)
99.599% <= 1.703 milliseconds (cumulative count 99599)
99.742% <= 1.807 milliseconds (cumulative count 99742)
99.844% <= 1.903 milliseconds (cumulative count 99844)
99.920% <= 2.007 milliseconds (cumulative count 99920)
99.958% <= 2.103 milliseconds (cumulative count 99958)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 37878.79 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.709     0.328     0.655     1.063     1.495     2.543
====== SET ======                                                   
  100000 requests completed in 2.93 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.311 milliseconds (cumulative count 1)
50.000% <= 0.671 milliseconds (cumulative count 51553)
75.000% <= 0.815 milliseconds (cumulative count 75238)
87.500% <= 1.127 milliseconds (cumulative count 87603)
93.750% <= 1.383 milliseconds (cumulative count 93777)
96.875% <= 1.655 milliseconds (cumulative count 96902)
98.438% <= 1.927 milliseconds (cumulative count 98442)
99.219% <= 2.191 milliseconds (cumulative count 99220)
99.609% <= 2.559 milliseconds (cumulative count 99610)
99.805% <= 3.063 milliseconds (cumulative count 99806)
99.902% <= 4.279 milliseconds (cumulative count 99903)
99.951% <= 6.047 milliseconds (cumulative count 99952)
99.976% <= 6.911 milliseconds (cumulative count 99976)
99.988% <= 7.711 milliseconds (cumulative count 99988)
99.994% <= 8.471 milliseconds (cumulative count 99994)
99.997% <= 8.919 milliseconds (cumulative count 99997)
99.998% <= 9.087 milliseconds (cumulative count 99999)
99.999% <= 9.159 milliseconds (cumulative count 100000)
100.000% <= 9.159 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.012% <= 0.407 milliseconds (cumulative count 12)
0.058% <= 0.503 milliseconds (cumulative count 58)
5.785% <= 0.607 milliseconds (cumulative count 5785)
61.847% <= 0.703 milliseconds (cumulative count 61847)
74.681% <= 0.807 milliseconds (cumulative count 74681)
79.489% <= 0.903 milliseconds (cumulative count 79489)
83.579% <= 1.007 milliseconds (cumulative count 83579)
86.875% <= 1.103 milliseconds (cumulative count 86875)
89.915% <= 1.207 milliseconds (cumulative count 89915)
92.319% <= 1.303 milliseconds (cumulative count 92319)
94.142% <= 1.407 milliseconds (cumulative count 94142)
95.446% <= 1.503 milliseconds (cumulative count 95446)
96.509% <= 1.607 milliseconds (cumulative count 96509)
97.264% <= 1.703 milliseconds (cumulative count 97264)
97.908% <= 1.807 milliseconds (cumulative count 97908)
98.361% <= 1.903 milliseconds (cumulative count 98361)
98.732% <= 2.007 milliseconds (cumulative count 98732)
99.011% <= 2.103 milliseconds (cumulative count 99011)
99.813% <= 3.103 milliseconds (cumulative count 99813)
99.893% <= 4.103 milliseconds (cumulative count 99893)
99.925% <= 5.103 milliseconds (cumulative count 99925)
99.953% <= 6.103 milliseconds (cumulative count 99953)
99.983% <= 7.103 milliseconds (cumulative count 99983)
99.991% <= 8.103 milliseconds (cumulative count 99991)
99.999% <= 9.103 milliseconds (cumulative count 99999)
100.000% <= 10.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 34141.35 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.806     0.304     0.671     1.471     2.103     9.159
====== GET ======                                                   
  100000 requests completed in 2.64 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.335 milliseconds (cumulative count 1)
50.000% <= 0.663 milliseconds (cumulative count 55516)
75.000% <= 0.719 milliseconds (cumulative count 76230)
87.500% <= 0.823 milliseconds (cumulative count 87760)
93.750% <= 0.999 milliseconds (cumulative count 93879)
96.875% <= 1.135 milliseconds (cumulative count 96880)
98.438% <= 1.319 milliseconds (cumulative count 98442)
99.219% <= 1.519 milliseconds (cumulative count 99227)
99.609% <= 1.679 milliseconds (cumulative count 99617)
99.805% <= 1.799 milliseconds (cumulative count 99810)
99.902% <= 1.911 milliseconds (cumulative count 99904)
99.951% <= 2.015 milliseconds (cumulative count 99953)
99.976% <= 2.087 milliseconds (cumulative count 99980)
99.988% <= 2.143 milliseconds (cumulative count 99989)
99.994% <= 2.167 milliseconds (cumulative count 99994)
99.997% <= 2.247 milliseconds (cumulative count 99997)
99.998% <= 2.327 milliseconds (cumulative count 99999)
99.999% <= 2.375 milliseconds (cumulative count 100000)
100.000% <= 2.375 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.009% <= 0.407 milliseconds (cumulative count 9)
0.024% <= 0.503 milliseconds (cumulative count 24)
5.774% <= 0.607 milliseconds (cumulative count 5774)
72.565% <= 0.703 milliseconds (cumulative count 72565)
86.771% <= 0.807 milliseconds (cumulative count 86771)
90.999% <= 0.903 milliseconds (cumulative count 90999)
94.115% <= 1.007 milliseconds (cumulative count 94115)
96.419% <= 1.103 milliseconds (cumulative count 96419)
97.676% <= 1.207 milliseconds (cumulative count 97676)
98.351% <= 1.303 milliseconds (cumulative count 98351)
98.837% <= 1.407 milliseconds (cumulative count 98837)
99.172% <= 1.503 milliseconds (cumulative count 99172)
99.455% <= 1.607 milliseconds (cumulative count 99455)
99.661% <= 1.703 milliseconds (cumulative count 99661)
99.821% <= 1.807 milliseconds (cumulative count 99821)
99.899% <= 1.903 milliseconds (cumulative count 99899)
99.950% <= 2.007 milliseconds (cumulative count 99950)
99.981% <= 2.103 milliseconds (cumulative count 99981)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 37907.50 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.711     0.328     0.663     1.039     1.455     2.375
====== INCR ======                                                   
  100000 requests completed in 2.58 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.399 milliseconds (cumulative count 1)
50.000% <= 0.647 milliseconds (cumulative count 51162)
75.000% <= 0.703 milliseconds (cumulative count 76458)
87.500% <= 0.791 milliseconds (cumulative count 87633)
93.750% <= 0.951 milliseconds (cumulative count 93854)
96.875% <= 1.071 milliseconds (cumulative count 96926)
98.438% <= 1.231 milliseconds (cumulative count 98448)
99.219% <= 1.423 milliseconds (cumulative count 99233)
99.609% <= 1.599 milliseconds (cumulative count 99620)
99.805% <= 1.775 milliseconds (cumulative count 99806)
99.902% <= 1.991 milliseconds (cumulative count 99903)
99.951% <= 2.391 milliseconds (cumulative count 99952)
99.976% <= 3.223 milliseconds (cumulative count 99976)
99.988% <= 3.415 milliseconds (cumulative count 99988)
99.994% <= 3.527 milliseconds (cumulative count 99994)
99.997% <= 3.607 milliseconds (cumulative count 99997)
99.998% <= 4.151 milliseconds (cumulative count 99999)
99.999% <= 4.191 milliseconds (cumulative count 100000)
100.000% <= 4.191 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.407 milliseconds (cumulative count 1)
0.029% <= 0.503 milliseconds (cumulative count 29)
11.125% <= 0.607 milliseconds (cumulative count 11125)
76.458% <= 0.703 milliseconds (cumulative count 76458)
88.589% <= 0.807 milliseconds (cumulative count 88589)
92.277% <= 0.903 milliseconds (cumulative count 92277)
95.546% <= 1.007 milliseconds (cumulative count 95546)
97.381% <= 1.103 milliseconds (cumulative count 97381)
98.315% <= 1.207 milliseconds (cumulative count 98315)
98.797% <= 1.303 milliseconds (cumulative count 98797)
99.182% <= 1.407 milliseconds (cumulative count 99182)
99.433% <= 1.503 milliseconds (cumulative count 99433)
99.630% <= 1.607 milliseconds (cumulative count 99630)
99.763% <= 1.703 milliseconds (cumulative count 99763)
99.827% <= 1.807 milliseconds (cumulative count 99827)
99.867% <= 1.903 milliseconds (cumulative count 99867)
99.910% <= 2.007 milliseconds (cumulative count 99910)
99.932% <= 2.103 milliseconds (cumulative count 99932)
99.971% <= 3.103 milliseconds (cumulative count 99971)
99.998% <= 4.103 milliseconds (cumulative count 99998)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 38804.81 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.695     0.392     0.647     0.991     1.359     4.191
====== LPUSH ======                                                   
  100000 requests completed in 2.57 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.295 milliseconds (cumulative count 1)
50.000% <= 0.655 milliseconds (cumulative count 53466)
75.000% <= 0.711 milliseconds (cumulative count 76484)
87.500% <= 0.799 milliseconds (cumulative count 87519)
93.750% <= 0.967 milliseconds (cumulative count 93825)
96.875% <= 1.103 milliseconds (cumulative count 96975)
98.438% <= 1.263 milliseconds (cumulative count 98450)
99.219% <= 1.399 milliseconds (cumulative count 99241)
99.609% <= 1.535 milliseconds (cumulative count 99621)
99.805% <= 1.631 milliseconds (cumulative count 99805)
99.902% <= 1.743 milliseconds (cumulative count 99908)
99.951% <= 1.831 milliseconds (cumulative count 99954)
99.976% <= 1.943 milliseconds (cumulative count 99977)
99.988% <= 2.031 milliseconds (cumulative count 99988)
99.994% <= 2.111 milliseconds (cumulative count 99994)
99.997% <= 2.167 milliseconds (cumulative count 99997)
99.998% <= 2.231 milliseconds (cumulative count 99999)
99.999% <= 2.247 milliseconds (cumulative count 100000)
100.000% <= 2.247 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.303 milliseconds (cumulative count 1)
0.008% <= 0.407 milliseconds (cumulative count 8)
0.036% <= 0.503 milliseconds (cumulative count 36)
8.203% <= 0.607 milliseconds (cumulative count 8203)
74.529% <= 0.703 milliseconds (cumulative count 74529)
88.014% <= 0.807 milliseconds (cumulative count 88014)
91.850% <= 0.903 milliseconds (cumulative count 91850)
94.970% <= 1.007 milliseconds (cumulative count 94970)
96.975% <= 1.103 milliseconds (cumulative count 96975)
98.035% <= 1.207 milliseconds (cumulative count 98035)
98.702% <= 1.303 milliseconds (cumulative count 98702)
99.280% <= 1.407 milliseconds (cumulative count 99280)
99.551% <= 1.503 milliseconds (cumulative count 99551)
99.766% <= 1.607 milliseconds (cumulative count 99766)
99.884% <= 1.703 milliseconds (cumulative count 99884)
99.946% <= 1.807 milliseconds (cumulative count 99946)
99.970% <= 1.903 milliseconds (cumulative count 99970)
99.985% <= 2.007 milliseconds (cumulative count 99985)
99.993% <= 2.103 milliseconds (cumulative count 99993)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 38865.14 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.701     0.288     0.655     1.015     1.359     2.247
====== RPUSH ======                                                   
  100000 requests completed in 2.53 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.311 milliseconds (cumulative count 1)
50.000% <= 0.647 milliseconds (cumulative count 53000)
75.000% <= 0.687 milliseconds (cumulative count 75950)
87.500% <= 0.759 milliseconds (cumulative count 87881)
93.750% <= 0.879 milliseconds (cumulative count 93811)
96.875% <= 1.039 milliseconds (cumulative count 96926)
98.438% <= 1.215 milliseconds (cumulative count 98440)
99.219% <= 1.399 milliseconds (cumulative count 99226)
99.609% <= 1.583 milliseconds (cumulative count 99618)
99.805% <= 1.743 milliseconds (cumulative count 99806)
99.902% <= 1.887 milliseconds (cumulative count 99904)
99.951% <= 2.023 milliseconds (cumulative count 99952)
99.976% <= 2.183 milliseconds (cumulative count 99976)
99.988% <= 2.399 milliseconds (cumulative count 99989)
99.994% <= 2.663 milliseconds (cumulative count 99994)
99.997% <= 2.775 milliseconds (cumulative count 99997)
99.998% <= 2.903 milliseconds (cumulative count 99999)
99.999% <= 2.927 milliseconds (cumulative count 100000)
100.000% <= 2.927 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.009% <= 0.407 milliseconds (cumulative count 9)
0.041% <= 0.503 milliseconds (cumulative count 41)
9.749% <= 0.607 milliseconds (cumulative count 9749)
80.320% <= 0.703 milliseconds (cumulative count 80320)
91.133% <= 0.807 milliseconds (cumulative count 91133)
94.464% <= 0.903 milliseconds (cumulative count 94464)
96.441% <= 1.007 milliseconds (cumulative count 96441)
97.651% <= 1.103 milliseconds (cumulative count 97651)
98.394% <= 1.207 milliseconds (cumulative count 98394)
98.852% <= 1.303 milliseconds (cumulative count 98852)
99.247% <= 1.407 milliseconds (cumulative count 99247)
99.475% <= 1.503 milliseconds (cumulative count 99475)
99.644% <= 1.607 milliseconds (cumulative count 99644)
99.771% <= 1.703 milliseconds (cumulative count 99771)
99.852% <= 1.807 milliseconds (cumulative count 99852)
99.913% <= 1.903 milliseconds (cumulative count 99913)
99.946% <= 2.007 milliseconds (cumulative count 99946)
99.967% <= 2.103 milliseconds (cumulative count 99967)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39541.32 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.685     0.304     0.647     0.927     1.343     2.927
====== LPOP ======                                                   
  100000 requests completed in 2.53 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.343 milliseconds (cumulative count 1)
50.000% <= 0.655 milliseconds (cumulative count 55607)
75.000% <= 0.695 milliseconds (cumulative count 76118)
87.500% <= 0.767 milliseconds (cumulative count 88232)
93.750% <= 0.871 milliseconds (cumulative count 93980)
96.875% <= 1.015 milliseconds (cumulative count 96993)
98.438% <= 1.183 milliseconds (cumulative count 98474)
99.219% <= 1.359 milliseconds (cumulative count 99238)
99.609% <= 1.511 milliseconds (cumulative count 99619)
99.805% <= 1.663 milliseconds (cumulative count 99809)
99.902% <= 1.863 milliseconds (cumulative count 99903)
99.951% <= 2.143 milliseconds (cumulative count 99953)
99.976% <= 2.359 milliseconds (cumulative count 99976)
99.988% <= 2.767 milliseconds (cumulative count 99988)
99.994% <= 3.015 milliseconds (cumulative count 99994)
99.997% <= 3.103 milliseconds (cumulative count 99997)
99.998% <= 3.223 milliseconds (cumulative count 99999)
99.999% <= 3.247 milliseconds (cumulative count 100000)
100.000% <= 3.247 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.009% <= 0.407 milliseconds (cumulative count 9)
0.047% <= 0.503 milliseconds (cumulative count 47)
7.097% <= 0.607 milliseconds (cumulative count 7097)
78.421% <= 0.703 milliseconds (cumulative count 78421)
91.103% <= 0.807 milliseconds (cumulative count 91103)
94.885% <= 0.903 milliseconds (cumulative count 94885)
96.873% <= 1.007 milliseconds (cumulative count 96873)
97.901% <= 1.103 milliseconds (cumulative count 97901)
98.600% <= 1.207 milliseconds (cumulative count 98600)
99.047% <= 1.303 milliseconds (cumulative count 99047)
99.373% <= 1.407 milliseconds (cumulative count 99373)
99.604% <= 1.503 milliseconds (cumulative count 99604)
99.753% <= 1.607 milliseconds (cumulative count 99753)
99.833% <= 1.703 milliseconds (cumulative count 99833)
99.882% <= 1.807 milliseconds (cumulative count 99882)
99.912% <= 1.903 milliseconds (cumulative count 99912)
99.934% <= 2.007 milliseconds (cumulative count 99934)
99.948% <= 2.103 milliseconds (cumulative count 99948)
99.997% <= 3.103 milliseconds (cumulative count 99997)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39478.88 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.687     0.336     0.655     0.911     1.295     3.247
====== RPOP ======                                                   
  100000 requests completed in 2.53 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.303 milliseconds (cumulative count 1)
50.000% <= 0.647 milliseconds (cumulative count 52240)
75.000% <= 0.687 milliseconds (cumulative count 75039)
87.500% <= 0.759 milliseconds (cumulative count 87802)
93.750% <= 0.871 milliseconds (cumulative count 93766)
96.875% <= 1.055 milliseconds (cumulative count 96966)
98.438% <= 1.231 milliseconds (cumulative count 98477)
99.219% <= 1.415 milliseconds (cumulative count 99247)
99.609% <= 1.575 milliseconds (cumulative count 99614)
99.805% <= 1.727 milliseconds (cumulative count 99811)
99.902% <= 1.879 milliseconds (cumulative count 99907)
99.951% <= 2.039 milliseconds (cumulative count 99952)
99.976% <= 2.215 milliseconds (cumulative count 99977)
99.988% <= 2.311 milliseconds (cumulative count 99988)
99.994% <= 2.423 milliseconds (cumulative count 99994)
99.997% <= 2.479 milliseconds (cumulative count 99997)
99.998% <= 2.919 milliseconds (cumulative count 99999)
99.999% <= 2.975 milliseconds (cumulative count 100000)
100.000% <= 2.975 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.303 milliseconds (cumulative count 1)
0.008% <= 0.407 milliseconds (cumulative count 8)
0.035% <= 0.503 milliseconds (cumulative count 35)
9.709% <= 0.607 milliseconds (cumulative count 9709)
79.531% <= 0.703 milliseconds (cumulative count 79531)
91.090% <= 0.807 milliseconds (cumulative count 91090)
94.622% <= 0.903 milliseconds (cumulative count 94622)
96.338% <= 1.007 milliseconds (cumulative count 96338)
97.505% <= 1.103 milliseconds (cumulative count 97505)
98.356% <= 1.207 milliseconds (cumulative count 98356)
98.827% <= 1.303 milliseconds (cumulative count 98827)
99.218% <= 1.407 milliseconds (cumulative count 99218)
99.486% <= 1.503 milliseconds (cumulative count 99486)
99.660% <= 1.607 milliseconds (cumulative count 99660)
99.792% <= 1.703 milliseconds (cumulative count 99792)
99.865% <= 1.807 milliseconds (cumulative count 99865)
99.914% <= 1.903 milliseconds (cumulative count 99914)
99.945% <= 2.007 milliseconds (cumulative count 99945)
99.966% <= 2.103 milliseconds (cumulative count 99966)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39588.28 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.686     0.296     0.647     0.927     1.343     2.975
====== SADD ======                                                   
  100000 requests completed in 2.53 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.295 milliseconds (cumulative count 1)
50.000% <= 0.647 milliseconds (cumulative count 53745)
75.000% <= 0.687 milliseconds (cumulative count 75696)
87.500% <= 0.759 milliseconds (cumulative count 87514)
93.750% <= 0.887 milliseconds (cumulative count 93883)
96.875% <= 1.055 milliseconds (cumulative count 96977)
98.438% <= 1.231 milliseconds (cumulative count 98443)
99.219% <= 1.431 milliseconds (cumulative count 99230)
99.609% <= 1.623 milliseconds (cumulative count 99622)
99.805% <= 1.775 milliseconds (cumulative count 99808)
99.902% <= 1.919 milliseconds (cumulative count 99906)
99.951% <= 2.175 milliseconds (cumulative count 99952)
99.976% <= 2.615 milliseconds (cumulative count 99976)
99.988% <= 2.759 milliseconds (cumulative count 99988)
99.994% <= 2.903 milliseconds (cumulative count 99994)
99.997% <= 3.039 milliseconds (cumulative count 99997)
99.998% <= 3.127 milliseconds (cumulative count 99999)
99.999% <= 3.167 milliseconds (cumulative count 100000)
100.000% <= 3.167 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.303 milliseconds (cumulative count 1)
0.005% <= 0.407 milliseconds (cumulative count 5)
0.058% <= 0.503 milliseconds (cumulative count 58)
10.977% <= 0.607 milliseconds (cumulative count 10977)
79.855% <= 0.703 milliseconds (cumulative count 79855)
90.760% <= 0.807 milliseconds (cumulative count 90760)
94.287% <= 0.903 milliseconds (cumulative count 94287)
96.278% <= 1.007 milliseconds (cumulative count 96278)
97.510% <= 1.103 milliseconds (cumulative count 97510)
98.300% <= 1.207 milliseconds (cumulative count 98300)
98.810% <= 1.303 milliseconds (cumulative count 98810)
99.165% <= 1.407 milliseconds (cumulative count 99165)
99.390% <= 1.503 milliseconds (cumulative count 99390)
99.589% <= 1.607 milliseconds (cumulative count 99589)
99.736% <= 1.703 milliseconds (cumulative count 99736)
99.833% <= 1.807 milliseconds (cumulative count 99833)
99.898% <= 1.903 milliseconds (cumulative count 99898)
99.930% <= 2.007 milliseconds (cumulative count 99930)
99.944% <= 2.103 milliseconds (cumulative count 99944)
99.998% <= 3.103 milliseconds (cumulative count 99998)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39510.08 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.686     0.288     0.647     0.935     1.359     3.167
====== HSET ======                                                   
  100000 requests completed in 2.57 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.319 milliseconds (cumulative count 1)
50.000% <= 0.655 milliseconds (cumulative count 53687)
75.000% <= 0.703 milliseconds (cumulative count 75291)
87.500% <= 0.807 milliseconds (cumulative count 87863)
93.750% <= 0.967 milliseconds (cumulative count 93794)
96.875% <= 1.159 milliseconds (cumulative count 96921)
98.438% <= 1.375 milliseconds (cumulative count 98453)
99.219% <= 1.591 milliseconds (cumulative count 99231)
99.609% <= 1.847 milliseconds (cumulative count 99619)
99.805% <= 2.047 milliseconds (cumulative count 99809)
99.902% <= 2.215 milliseconds (cumulative count 99904)
99.951% <= 2.423 milliseconds (cumulative count 99953)
99.976% <= 2.607 milliseconds (cumulative count 99976)
99.988% <= 2.783 milliseconds (cumulative count 99988)
99.994% <= 3.119 milliseconds (cumulative count 99994)
99.997% <= 3.247 milliseconds (cumulative count 99997)
99.998% <= 3.351 milliseconds (cumulative count 99999)
99.999% <= 3.391 milliseconds (cumulative count 100000)
100.000% <= 3.391 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.008% <= 0.407 milliseconds (cumulative count 8)
0.036% <= 0.503 milliseconds (cumulative count 36)
7.763% <= 0.607 milliseconds (cumulative count 7763)
75.291% <= 0.703 milliseconds (cumulative count 75291)
87.863% <= 0.807 milliseconds (cumulative count 87863)
92.051% <= 0.903 milliseconds (cumulative count 92051)
94.623% <= 1.007 milliseconds (cumulative count 94623)
96.234% <= 1.103 milliseconds (cumulative count 96234)
97.364% <= 1.207 milliseconds (cumulative count 97364)
98.054% <= 1.303 milliseconds (cumulative count 98054)
98.598% <= 1.407 milliseconds (cumulative count 98598)
98.964% <= 1.503 milliseconds (cumulative count 98964)
99.263% <= 1.607 milliseconds (cumulative count 99263)
99.430% <= 1.703 milliseconds (cumulative count 99430)
99.567% <= 1.807 milliseconds (cumulative count 99567)
99.681% <= 1.903 milliseconds (cumulative count 99681)
99.775% <= 2.007 milliseconds (cumulative count 99775)
99.846% <= 2.103 milliseconds (cumulative count 99846)
99.993% <= 3.103 milliseconds (cumulative count 99993)
100.000% <= 4.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 38955.98 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.706     0.312     0.655     1.031     1.519     3.391
====== SPOP ======                                                   
  100000 requests completed in 2.48 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.311 milliseconds (cumulative count 1)
50.000% <= 0.639 milliseconds (cumulative count 55709)
75.000% <= 0.679 milliseconds (cumulative count 76765)
87.500% <= 0.743 milliseconds (cumulative count 87879)
93.750% <= 0.863 milliseconds (cumulative count 93855)
96.875% <= 1.047 milliseconds (cumulative count 96960)
98.438% <= 1.199 milliseconds (cumulative count 98438)
99.219% <= 1.359 milliseconds (cumulative count 99244)
99.609% <= 1.495 milliseconds (cumulative count 99614)
99.805% <= 1.623 milliseconds (cumulative count 99814)
99.902% <= 1.743 milliseconds (cumulative count 99905)
99.951% <= 1.895 milliseconds (cumulative count 99952)
99.976% <= 2.007 milliseconds (cumulative count 99976)
99.988% <= 2.119 milliseconds (cumulative count 99988)
99.994% <= 2.335 milliseconds (cumulative count 99994)
99.997% <= 2.399 milliseconds (cumulative count 99997)
99.998% <= 2.439 milliseconds (cumulative count 99999)
99.999% <= 2.463 milliseconds (cumulative count 100000)
100.000% <= 2.463 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.004% <= 0.407 milliseconds (cumulative count 4)
0.042% <= 0.503 milliseconds (cumulative count 42)
21.647% <= 0.607 milliseconds (cumulative count 21647)
82.474% <= 0.703 milliseconds (cumulative count 82474)
91.938% <= 0.807 milliseconds (cumulative count 91938)
94.858% <= 0.903 milliseconds (cumulative count 94858)
96.438% <= 1.007 milliseconds (cumulative count 96438)
97.606% <= 1.103 milliseconds (cumulative count 97606)
98.498% <= 1.207 milliseconds (cumulative count 98498)
99.042% <= 1.303 milliseconds (cumulative count 99042)
99.383% <= 1.407 milliseconds (cumulative count 99383)
99.632% <= 1.503 milliseconds (cumulative count 99632)
99.786% <= 1.607 milliseconds (cumulative count 99786)
99.886% <= 1.703 milliseconds (cumulative count 99886)
99.925% <= 1.807 milliseconds (cumulative count 99925)
99.954% <= 1.903 milliseconds (cumulative count 99954)
99.976% <= 2.007 milliseconds (cumulative count 99976)
99.987% <= 2.103 milliseconds (cumulative count 99987)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 40273.86 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.673     0.304     0.639     0.911     1.295     2.463
====== ZADD ======                                                   
  100000 requests completed in 2.52 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.271 milliseconds (cumulative count 1)
50.000% <= 0.655 milliseconds (cumulative count 54795)
75.000% <= 0.695 milliseconds (cumulative count 76202)
87.500% <= 0.767 milliseconds (cumulative count 88003)
93.750% <= 0.879 milliseconds (cumulative count 93877)
96.875% <= 1.023 milliseconds (cumulative count 96883)
98.438% <= 1.175 milliseconds (cumulative count 98439)
99.219% <= 1.367 milliseconds (cumulative count 99228)
99.609% <= 1.551 milliseconds (cumulative count 99616)
99.805% <= 1.711 milliseconds (cumulative count 99810)
99.902% <= 1.839 milliseconds (cumulative count 99906)
99.951% <= 1.991 milliseconds (cumulative count 99954)
99.976% <= 2.143 milliseconds (cumulative count 99976)
99.988% <= 2.351 milliseconds (cumulative count 99988)
99.994% <= 2.447 milliseconds (cumulative count 99994)
99.997% <= 2.559 milliseconds (cumulative count 99997)
99.998% <= 2.639 milliseconds (cumulative count 99999)
99.999% <= 2.711 milliseconds (cumulative count 100000)
100.000% <= 2.711 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.003% <= 0.303 milliseconds (cumulative count 3)
0.010% <= 0.407 milliseconds (cumulative count 10)
0.042% <= 0.503 milliseconds (cumulative count 42)
6.891% <= 0.607 milliseconds (cumulative count 6891)
78.429% <= 0.703 milliseconds (cumulative count 78429)
90.818% <= 0.807 milliseconds (cumulative count 90818)
94.612% <= 0.903 milliseconds (cumulative count 94612)
96.659% <= 1.007 milliseconds (cumulative count 96659)
97.898% <= 1.103 milliseconds (cumulative count 97898)
98.603% <= 1.207 milliseconds (cumulative count 98603)
98.998% <= 1.303 milliseconds (cumulative count 98998)
99.326% <= 1.407 milliseconds (cumulative count 99326)
99.537% <= 1.503 milliseconds (cumulative count 99537)
99.698% <= 1.607 milliseconds (cumulative count 99698)
99.800% <= 1.703 milliseconds (cumulative count 99800)
99.888% <= 1.807 milliseconds (cumulative count 99888)
99.931% <= 1.903 milliseconds (cumulative count 99931)
99.958% <= 2.007 milliseconds (cumulative count 99958)
99.972% <= 2.103 milliseconds (cumulative count 99972)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39635.36 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.689     0.264     0.655     0.919     1.311     2.711
====== ZPOPMIN ======                                                   
  100000 requests completed in 2.50 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.311 milliseconds (cumulative count 1)
50.000% <= 0.631 milliseconds (cumulative count 50660)
75.000% <= 0.679 milliseconds (cumulative count 76909)
87.500% <= 0.751 milliseconds (cumulative count 87584)
93.750% <= 0.903 milliseconds (cumulative count 93890)
96.875% <= 1.063 milliseconds (cumulative count 96935)
98.438% <= 1.223 milliseconds (cumulative count 98491)
99.219% <= 1.367 milliseconds (cumulative count 99221)
99.609% <= 1.511 milliseconds (cumulative count 99612)
99.805% <= 1.679 milliseconds (cumulative count 99806)
99.902% <= 1.991 milliseconds (cumulative count 99903)
99.951% <= 2.463 milliseconds (cumulative count 99953)
99.976% <= 3.071 milliseconds (cumulative count 99976)
99.988% <= 3.447 milliseconds (cumulative count 99988)
99.994% <= 4.031 milliseconds (cumulative count 99994)
99.997% <= 4.183 milliseconds (cumulative count 99997)
99.998% <= 4.295 milliseconds (cumulative count 99999)
99.999% <= 4.359 milliseconds (cumulative count 100000)
100.000% <= 4.359 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.009% <= 0.407 milliseconds (cumulative count 9)
0.054% <= 0.503 milliseconds (cumulative count 54)
23.403% <= 0.607 milliseconds (cumulative count 23403)
82.035% <= 0.703 milliseconds (cumulative count 82035)
90.869% <= 0.807 milliseconds (cumulative count 90869)
93.890% <= 0.903 milliseconds (cumulative count 93890)
96.098% <= 1.007 milliseconds (cumulative count 96098)
97.455% <= 1.103 milliseconds (cumulative count 97455)
98.377% <= 1.207 milliseconds (cumulative count 98377)
98.935% <= 1.303 milliseconds (cumulative count 98935)
99.356% <= 1.407 milliseconds (cumulative count 99356)
99.600% <= 1.503 milliseconds (cumulative count 99600)
99.751% <= 1.607 milliseconds (cumulative count 99751)
99.822% <= 1.703 milliseconds (cumulative count 99822)
99.869% <= 1.807 milliseconds (cumulative count 99869)
99.892% <= 1.903 milliseconds (cumulative count 99892)
99.906% <= 2.007 milliseconds (cumulative count 99906)
99.917% <= 2.103 milliseconds (cumulative count 99917)
99.977% <= 3.103 milliseconds (cumulative count 99977)
99.995% <= 4.103 milliseconds (cumulative count 99995)
100.000% <= 5.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 40064.10 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.675     0.304     0.631     0.951     1.319     4.359
====== LPUSH (needed to benchmark LRANGE) ======                                                   
  100000 requests completed in 2.52 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.335 milliseconds (cumulative count 1)
50.000% <= 0.647 milliseconds (cumulative count 51565)
75.000% <= 0.695 milliseconds (cumulative count 77559)
87.500% <= 0.759 milliseconds (cumulative count 87960)
93.750% <= 0.871 milliseconds (cumulative count 93877)
96.875% <= 1.023 milliseconds (cumulative count 96945)
98.438% <= 1.191 milliseconds (cumulative count 98443)
99.219% <= 1.399 milliseconds (cumulative count 99256)
99.609% <= 1.511 milliseconds (cumulative count 99617)
99.805% <= 1.639 milliseconds (cumulative count 99807)
99.902% <= 1.759 milliseconds (cumulative count 99903)
99.951% <= 1.887 milliseconds (cumulative count 99953)
99.976% <= 2.063 milliseconds (cumulative count 99976)
99.988% <= 2.375 milliseconds (cumulative count 99988)
99.994% <= 2.527 milliseconds (cumulative count 99994)
99.997% <= 2.575 milliseconds (cumulative count 99997)
99.998% <= 2.663 milliseconds (cumulative count 99999)
99.999% <= 2.727 milliseconds (cumulative count 100000)
100.000% <= 2.727 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.007% <= 0.407 milliseconds (cumulative count 7)
0.038% <= 0.503 milliseconds (cumulative count 38)
8.567% <= 0.607 milliseconds (cumulative count 8567)
79.633% <= 0.703 milliseconds (cumulative count 79633)
91.258% <= 0.807 milliseconds (cumulative count 91258)
94.830% <= 0.903 milliseconds (cumulative count 94830)
96.756% <= 1.007 milliseconds (cumulative count 96756)
97.793% <= 1.103 milliseconds (cumulative count 97793)
98.538% <= 1.207 milliseconds (cumulative count 98538)
98.903% <= 1.303 milliseconds (cumulative count 98903)
99.293% <= 1.407 milliseconds (cumulative count 99293)
99.603% <= 1.503 milliseconds (cumulative count 99603)
99.767% <= 1.607 milliseconds (cumulative count 99767)
99.874% <= 1.703 milliseconds (cumulative count 99874)
99.926% <= 1.807 milliseconds (cumulative count 99926)
99.958% <= 1.903 milliseconds (cumulative count 99958)
99.972% <= 2.007 milliseconds (cumulative count 99972)
99.978% <= 2.103 milliseconds (cumulative count 99978)
100.000% <= 3.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 39714.06 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.685     0.328     0.647     0.911     1.335     2.727
====== LRANGE_100 (first 100 elements) ======                                                   
  100000 requests completed in 6.24 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.815 milliseconds (cumulative count 2)
50.000% <= 1.263 milliseconds (cumulative count 50187)
75.000% <= 2.055 milliseconds (cumulative count 75770)
87.500% <= 2.191 milliseconds (cumulative count 87832)
93.750% <= 2.303 milliseconds (cumulative count 93813)
96.875% <= 2.431 milliseconds (cumulative count 96927)
98.438% <= 2.583 milliseconds (cumulative count 98483)
99.219% <= 2.759 milliseconds (cumulative count 99223)
99.609% <= 3.103 milliseconds (cumulative count 99612)
99.805% <= 3.503 milliseconds (cumulative count 99806)
99.902% <= 4.095 milliseconds (cumulative count 99903)
99.951% <= 4.823 milliseconds (cumulative count 99952)
99.976% <= 5.647 milliseconds (cumulative count 99976)
99.988% <= 6.839 milliseconds (cumulative count 99988)
99.994% <= 7.879 milliseconds (cumulative count 99994)
99.997% <= 8.423 milliseconds (cumulative count 99997)
99.998% <= 8.655 milliseconds (cumulative count 99999)
99.999% <= 8.799 milliseconds (cumulative count 100000)
100.000% <= 8.799 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
1.730% <= 0.903 milliseconds (cumulative count 1730)
11.143% <= 1.007 milliseconds (cumulative count 11143)
29.698% <= 1.103 milliseconds (cumulative count 29698)
45.438% <= 1.207 milliseconds (cumulative count 45438)
52.103% <= 1.303 milliseconds (cumulative count 52103)
54.307% <= 1.407 milliseconds (cumulative count 54307)
55.238% <= 1.503 milliseconds (cumulative count 55238)
55.553% <= 1.607 milliseconds (cumulative count 55553)
55.954% <= 1.703 milliseconds (cumulative count 55954)
57.592% <= 1.807 milliseconds (cumulative count 57592)
62.214% <= 1.903 milliseconds (cumulative count 62214)
71.020% <= 2.007 milliseconds (cumulative count 71020)
80.256% <= 2.103 milliseconds (cumulative count 80256)
99.612% <= 3.103 milliseconds (cumulative count 99612)
99.903% <= 4.103 milliseconds (cumulative count 99903)
99.961% <= 5.103 milliseconds (cumulative count 99961)
99.984% <= 6.103 milliseconds (cumulative count 99984)
99.989% <= 7.103 milliseconds (cumulative count 99989)
99.995% <= 8.103 milliseconds (cumulative count 99995)
100.000% <= 9.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 16023.07 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        1.554     0.808     1.263     2.343     2.695     8.799
====== LRANGE_300 (first 300 elements) ======                                                 
  100000 requests completed in 10.53 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.559 milliseconds (cumulative count 1)
50.000% <= 2.575 milliseconds (cumulative count 50664)
75.000% <= 2.751 milliseconds (cumulative count 77432)
87.500% <= 2.847 milliseconds (cumulative count 88085)
93.750% <= 2.959 milliseconds (cumulative count 93762)
96.875% <= 3.087 milliseconds (cumulative count 96928)
98.438% <= 3.215 milliseconds (cumulative count 98487)
99.219% <= 3.375 milliseconds (cumulative count 99230)
99.609% <= 3.575 milliseconds (cumulative count 99611)
99.805% <= 3.799 milliseconds (cumulative count 99814)
99.902% <= 3.975 milliseconds (cumulative count 99908)
99.951% <= 4.231 milliseconds (cumulative count 99952)
99.976% <= 4.447 milliseconds (cumulative count 99976)
99.988% <= 4.759 milliseconds (cumulative count 99988)
99.994% <= 4.887 milliseconds (cumulative count 99994)
99.997% <= 5.039 milliseconds (cumulative count 99997)
99.998% <= 5.167 milliseconds (cumulative count 99999)
99.999% <= 5.263 milliseconds (cumulative count 100000)
100.000% <= 5.263 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.607 milliseconds (cumulative count 1)
0.002% <= 0.703 milliseconds (cumulative count 2)
0.003% <= 0.807 milliseconds (cumulative count 3)
0.005% <= 0.903 milliseconds (cumulative count 5)
0.007% <= 1.007 milliseconds (cumulative count 7)
0.009% <= 1.103 milliseconds (cumulative count 9)
0.011% <= 1.207 milliseconds (cumulative count 11)
0.018% <= 1.303 milliseconds (cumulative count 18)
0.052% <= 1.407 milliseconds (cumulative count 52)
0.102% <= 1.503 milliseconds (cumulative count 102)
0.154% <= 1.607 milliseconds (cumulative count 154)
0.225% <= 1.703 milliseconds (cumulative count 225)
0.321% <= 1.807 milliseconds (cumulative count 321)
0.507% <= 1.903 milliseconds (cumulative count 507)
0.841% <= 2.007 milliseconds (cumulative count 841)
1.285% <= 2.103 milliseconds (cumulative count 1285)
97.227% <= 3.103 milliseconds (cumulative count 97227)
99.936% <= 4.103 milliseconds (cumulative count 99936)
99.998% <= 5.103 milliseconds (cumulative count 99998)
100.000% <= 6.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 9493.07 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        2.593     0.552     2.575     2.999     3.311     5.263
====== LRANGE_500 (first 450 elements) ======                                                 
  100000 requests completed in 21.79 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.295 milliseconds (cumulative count 1)
50.000% <= 5.407 milliseconds (cumulative count 50002)
75.000% <= 6.975 milliseconds (cumulative count 75122)
87.500% <= 7.527 milliseconds (cumulative count 87557)
93.750% <= 7.919 milliseconds (cumulative count 93790)
96.875% <= 8.239 milliseconds (cumulative count 96897)
98.438% <= 8.567 milliseconds (cumulative count 98450)
99.219% <= 8.935 milliseconds (cumulative count 99225)
99.609% <= 9.423 milliseconds (cumulative count 99613)
99.805% <= 9.895 milliseconds (cumulative count 99805)
99.902% <= 10.287 milliseconds (cumulative count 99903)
99.951% <= 10.623 milliseconds (cumulative count 99952)
99.976% <= 11.015 milliseconds (cumulative count 99976)
99.988% <= 11.191 milliseconds (cumulative count 99988)
99.994% <= 11.583 milliseconds (cumulative count 99994)
99.997% <= 12.375 milliseconds (cumulative count 99997)
99.998% <= 12.615 milliseconds (cumulative count 99999)
99.999% <= 12.655 milliseconds (cumulative count 100000)
100.000% <= 12.655 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.303 milliseconds (cumulative count 1)
0.002% <= 0.503 milliseconds (cumulative count 2)
0.003% <= 0.607 milliseconds (cumulative count 3)
0.004% <= 0.807 milliseconds (cumulative count 4)
0.005% <= 0.903 milliseconds (cumulative count 5)
0.006% <= 1.007 milliseconds (cumulative count 6)
0.008% <= 1.207 milliseconds (cumulative count 8)
0.010% <= 1.303 milliseconds (cumulative count 10)
0.011% <= 1.407 milliseconds (cumulative count 11)
0.015% <= 1.503 milliseconds (cumulative count 15)
0.020% <= 1.607 milliseconds (cumulative count 20)
0.026% <= 1.703 milliseconds (cumulative count 26)
0.046% <= 1.807 milliseconds (cumulative count 46)
0.061% <= 1.903 milliseconds (cumulative count 61)
0.094% <= 2.007 milliseconds (cumulative count 94)
0.140% <= 2.103 milliseconds (cumulative count 140)
2.388% <= 3.103 milliseconds (cumulative count 2388)
43.425% <= 4.103 milliseconds (cumulative count 43425)
49.289% <= 5.103 milliseconds (cumulative count 49289)
56.060% <= 6.103 milliseconds (cumulative count 56060)
78.056% <= 7.103 milliseconds (cumulative count 78056)
95.885% <= 8.103 milliseconds (cumulative count 95885)
99.421% <= 9.103 milliseconds (cumulative count 99421)
99.863% <= 10.103 milliseconds (cumulative count 99863)
99.981% <= 11.103 milliseconds (cumulative count 99981)
99.996% <= 12.103 milliseconds (cumulative count 99996)
100.000% <= 13.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 4589.68 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        5.362     0.288     5.407     8.023     8.791    12.655
====== LRANGE_600 (first 600 elements) ======                                                 
  100000 requests completed in 30.08 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.447 milliseconds (cumulative count 1)
50.000% <= 7.055 milliseconds (cumulative count 50007)
75.000% <= 9.471 milliseconds (cumulative count 75018)
87.500% <= 10.967 milliseconds (cumulative count 87503)
93.750% <= 12.095 milliseconds (cumulative count 93795)
96.875% <= 12.735 milliseconds (cumulative count 96887)
98.438% <= 13.151 milliseconds (cumulative count 98464)
99.219% <= 13.479 milliseconds (cumulative count 99222)
99.609% <= 13.791 milliseconds (cumulative count 99615)
99.805% <= 14.103 milliseconds (cumulative count 99805)
99.902% <= 14.503 milliseconds (cumulative count 99903)
99.951% <= 14.911 milliseconds (cumulative count 99952)
99.976% <= 15.415 milliseconds (cumulative count 99976)
99.988% <= 16.463 milliseconds (cumulative count 99988)
99.994% <= 17.151 milliseconds (cumulative count 99995)
99.997% <= 17.519 milliseconds (cumulative count 99997)
99.998% <= 18.143 milliseconds (cumulative count 99999)
99.999% <= 18.527 milliseconds (cumulative count 100000)
100.000% <= 18.527 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.001% <= 0.503 milliseconds (cumulative count 1)
0.002% <= 0.703 milliseconds (cumulative count 2)
0.003% <= 0.903 milliseconds (cumulative count 3)
0.004% <= 1.103 milliseconds (cumulative count 4)
0.005% <= 1.407 milliseconds (cumulative count 5)
0.006% <= 1.607 milliseconds (cumulative count 6)
0.008% <= 1.807 milliseconds (cumulative count 8)
0.009% <= 1.903 milliseconds (cumulative count 9)
0.010% <= 2.007 milliseconds (cumulative count 10)
0.013% <= 2.103 milliseconds (cumulative count 13)
0.415% <= 3.103 milliseconds (cumulative count 415)
4.111% <= 4.103 milliseconds (cumulative count 4111)
30.255% <= 5.103 milliseconds (cumulative count 30255)
44.100% <= 6.103 milliseconds (cumulative count 44100)
50.288% <= 7.103 milliseconds (cumulative count 50288)
57.583% <= 8.103 milliseconds (cumulative count 57583)
69.941% <= 9.103 milliseconds (cumulative count 69941)
81.810% <= 10.103 milliseconds (cumulative count 81810)
88.370% <= 11.103 milliseconds (cumulative count 88370)
93.845% <= 12.103 milliseconds (cumulative count 93845)
98.300% <= 13.103 milliseconds (cumulative count 98300)
99.805% <= 14.103 milliseconds (cumulative count 99805)
99.963% <= 15.103 milliseconds (cumulative count 99963)
99.986% <= 16.103 milliseconds (cumulative count 99986)
99.993% <= 17.103 milliseconds (cumulative count 99993)
99.998% <= 18.111 milliseconds (cumulative count 99998)
100.000% <= 19.103 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 3324.69 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        7.425     0.440     7.055    12.335    13.383    18.527
====== MSET (10 keys) ======                                                   
  100000 requests completed in 1.51 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1
  host configuration "save": 3600 1 300 100 60 10000
  host configuration "appendonly": no
  multi-thread: no

Latency by percentile distribution:
0.000% <= 0.263 milliseconds (cumulative count 1)
50.000% <= 0.599 milliseconds (cumulative count 50247)
75.000% <= 0.711 milliseconds (cumulative count 76103)
87.500% <= 0.799 milliseconds (cumulative count 88351)
93.750% <= 0.855 milliseconds (cumulative count 94099)
96.875% <= 0.895 milliseconds (cumulative count 96960)
98.438% <= 0.951 milliseconds (cumulative count 98500)
99.219% <= 1.031 milliseconds (cumulative count 99242)
99.609% <= 1.119 milliseconds (cumulative count 99628)
99.805% <= 1.215 milliseconds (cumulative count 99811)
99.902% <= 1.351 milliseconds (cumulative count 99906)
99.951% <= 1.463 milliseconds (cumulative count 99952)
99.976% <= 1.551 milliseconds (cumulative count 99982)
99.988% <= 1.575 milliseconds (cumulative count 99989)
99.994% <= 1.599 milliseconds (cumulative count 99994)
99.997% <= 1.703 milliseconds (cumulative count 99997)
99.998% <= 1.743 milliseconds (cumulative count 99999)
99.999% <= 1.775 milliseconds (cumulative count 100000)
100.000% <= 1.775 milliseconds (cumulative count 100000)

Cumulative distribution of latencies:
0.000% <= 0.103 milliseconds (cumulative count 0)
0.138% <= 0.303 milliseconds (cumulative count 138)
5.375% <= 0.407 milliseconds (cumulative count 5375)
23.633% <= 0.503 milliseconds (cumulative count 23633)
52.575% <= 0.607 milliseconds (cumulative count 52575)
74.733% <= 0.703 milliseconds (cumulative count 74733)
89.266% <= 0.807 milliseconds (cumulative count 89266)
97.333% <= 0.903 milliseconds (cumulative count 97333)
99.083% <= 1.007 milliseconds (cumulative count 99083)
99.581% <= 1.103 milliseconds (cumulative count 99581)
99.798% <= 1.207 milliseconds (cumulative count 99798)
99.883% <= 1.303 milliseconds (cumulative count 99883)
99.933% <= 1.407 milliseconds (cumulative count 99933)
99.963% <= 1.503 milliseconds (cumulative count 99963)
99.995% <= 1.607 milliseconds (cumulative count 99995)
99.997% <= 1.703 milliseconds (cumulative count 99997)
100.000% <= 1.807 milliseconds (cumulative count 100000)

Summary:
  throughput summary: 66401.06 requests per second
  latency summary (msec):
          avg       min       p50       p95       p99       max
        0.615     0.256     0.599     0.871     0.999     1.775
```

It basically does a lot of operations and finds the 99the percentile. I wonder
if the place from where the benchmark is executed matters. Hmm. Like, network
latency between the benchmark client and server, hmm, as everything seems to be
related to time and latency. Hmm. Okay, that's a good overview - lot of commands
and one can also choose which command tests to run, how many parallel clients,
how many requests / commands etc. I was just running with default configuration.

Now, let's move on to - redis-check-aof

---

redis-check-aof

```bash
$ redis-check-aof --help
Cannot open file: --help

$ redis-check-aof 
Usage: redis-check-aof [--fix] <file.aof>

$ man redis-check-aof
No manual entry for redis-check-aof
```

I'm not able to find the help for this command, hmm

https://duckduckgo.com/?t=ffab&q=redis-check-aof&ia=web

https://redis.io/topics/persistence

Apparently it's related to some persistence model. Redis has two models of saving data - RDB and AOF. One is mostly for backup (RDB) and the other is to not lose any data at all (AOF). At least that's what I understood and looks like the `redis-check-aof` is to check for issues in AOF files and fix them

https://www.systutorials.com/docs/linux/man/1-redis-check-aof/

https://www.mankier.com/1/redis-check-aof

I guess `redis-check-rdb` does something similar

https://duckduckgo.com/?q=redis-check-rdb&t=ffab&ia=web

https://www.systutorials.com/docs/linux/man/1-redis-check-rdb/

https://www.mankier.com/1/redis-check-rdb

---

redis-cli

It's the command line interface tool which acts as the redis client for a redis
server

---

redis-server

It's the redis server itself

https://www.systutorials.com/docs/linux/man/1-redis-server/

---

redis-sentinel

https://www.systutorials.com/docs/linux/man/1-redis-server/

Apparently it's a symbolic link to the redis-server with --sentinel option.
That's pretty interesting! :D


