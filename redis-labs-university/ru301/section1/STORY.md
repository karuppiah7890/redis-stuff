There's a GitHub repo for this

https://github.com/redislabs-training/exercises-scaling-redis

I just finished watching the introduction, it's pretty interesting to know some differences between open source redis and enterprise redis

Looks like there's actually an enterprise redis and an enterprise redis cloud or aka redis cloud. I guess enterprise redis is a self hosted but paid software, unlike open source redis and enterprise redis cloud / redis cloud is more of a SaaS / Database as a Service offering for a managed service - managed Redis service - managed Redis as a Service

Looking at the Redis Server overview - apparently Enterprise Redis can actually make use of all the CPU cores in a single machine, unlike open source Redis which is single threaded and uses only one core, hmm

And some interesting general things to think about when it comes to databases

In a basic interaction between a databases client and a database server, some basic things that happen are

- Server is listening for connections
- Client connects to the server
- Client sends command(s) to the server. This can be any kind of command - generically a read / write. Or one or many of CRUD - Created, Read, Update, Delete
- Server reads the command - parses the command
- Server understands how to execute the command over the data it has
- Server executes the command
- Depending upon the execution - a failure or success happens
- Server sends the response back to the client

The command could also be an invalid one - in multiple ways, like
- Invalid syntax - invalid command name, invalid number of command arguments, invalid type for command arguments, invalid value for command arguments and what not
- Invalid operation based on the data, or say if the databases was a readonly, but the command was a write command, then depending on the database, it will error out or not

Some errors can be caught early - while reading / parsing the command - and looking for invalid syntax. Some errors are harder to catch and only happen when executing

This is a basic interaction between client and server. To scale this, one has to scale a lot of things. More like, one could scale a lot of things

First, for many clients to be able to connect to the server, the server has to have that many open ports / sockets so that there can be communication between the client and the server. So, for example in Linux, one has to check the maximum limit for open files, using something like

```bash
$ ulimit -n
256
```

The server usually uses only one port / socket for listening, and other random ports / sockets for the client communication once the connection is accepted. So, this is pretty important

From what I remember, to communicate in a network, a system needs many things. One among them is a - socket address - is a mix of IP address + port address

After the connectivity, that is, the networking problem - the listening and handling many client connections, the next thing is reading and parsing the command. The server needs lots of power (?), or maybe just enough power (like, CPU?) to parse the command. From the redis university RU301 video, it says that reading from the socket is really expensive and the same goes for writing to the socket. So it's mentioned that it's better to keep all that functionality in a different thread

I have also seen that the command execution is tricky - some databases use query engines and what not, and have a plan to execute the query / command. So, that requires some power too

And then the actual execution of the command also needs some power, not to mention it also needs to read the data from the data storage. In redis it's the RAM so it's fast. Some databases use Disk, I know one that uses S3 - Simple Storage Service, so it's gonna be totally different there. So that Input/Output operations also requires quite some power - CPU and/ other power? IO power?

---

I was checking Redis Configuration. All configurations that can be modified at runtime can be obtained using `CONFIG GET *` it seems! :D

```bash
127.0.0.1:6379> CONFIG GET *
  1) "rdbchecksum"
  2) "yes"
  3) "daemonize"
  4) "no"
  5) "io-threads-do-reads"
  6) "no"
  7) "lua-replicate-commands"
  8) "yes"
  9) "always-show-logo"
 10) "no"
 11) "protected-mode"
 12) "yes"
 13) "rdbcompression"
 14) "yes"
 15) "rdb-del-sync-files"
 16) "no"
 17) "activerehashing"
 18) "yes"
 19) "stop-writes-on-bgsave-error"
 20) "yes"
 21) "set-proc-title"
 22) "yes"
 23) "dynamic-hz"
 24) "yes"
 25) "lazyfree-lazy-eviction"
 26) "no"
 27) "lazyfree-lazy-expire"
 28) "no"
 29) "lazyfree-lazy-server-del"
 30) "no"
 31) "lazyfree-lazy-user-del"
 32) "no"
 33) "lazyfree-lazy-user-flush"
 34) "no"
 35) "repl-disable-tcp-nodelay"
 36) "no"
 37) "repl-diskless-sync"
 38) "no"
 39) "gopher-enabled"
 40) "no"
 41) "aof-rewrite-incremental-fsync"
 42) "yes"
 43) "no-appendfsync-on-rewrite"
 44) "no"
 45) "cluster-require-full-coverage"
 46) "yes"
 47) "rdb-save-incremental-fsync"
 48) "yes"
 49) "aof-load-truncated"
 50) "yes"
 51) "aof-use-rdb-preamble"
 52) "yes"
 53) "cluster-replica-no-failover"
 54) "no"
 55) "cluster-slave-no-failover"
 56) "no"
 57) "replica-lazy-flush"
 58) "no"
 59) "slave-lazy-flush"
 60) "no"
 61) "replica-serve-stale-data"
 62) "yes"
 63) "slave-serve-stale-data"
 64) "yes"
 65) "replica-read-only"
 66) "yes"
 67) "slave-read-only"
 68) "yes"
 69) "replica-ignore-maxmemory"
 70) "yes"
 71) "slave-ignore-maxmemory"
 72) "yes"
 73) "jemalloc-bg-thread"
 74) "yes"
 75) "activedefrag"
 76) "no"
 77) "syslog-enabled"
 78) "no"
 79) "cluster-enabled"
 80) "no"
 81) "appendonly"
 82) "no"
 83) "cluster-allow-reads-when-down"
 84) "no"
 85) "crash-log-enabled"
 86) "yes"
 87) "crash-memcheck-enabled"
 88) "yes"
 89) "use-exit-on-panic"
 90) "no"
 91) "disable-thp"
 92) "yes"
 93) "cluster-allow-replica-migration"
 94) "yes"
 95) "replica-announced"
 96) "yes"
 97) "aclfile"
 98) ""
 99) "unixsocket"
100) ""
101) "pidfile"
102) ""
103) "replica-announce-ip"
104) ""
105) "slave-announce-ip"
106) ""
107) "masteruser"
108) ""
109) "cluster-announce-ip"
110) ""
111) "syslog-ident"
112) "redis"
113) "dbfilename"
114) "dump.rdb"
115) "appendfilename"
116) "appendonly.aof"
117) "server_cpulist"
118) ""
119) "bio_cpulist"
120) ""
121) "aof_rewrite_cpulist"
122) ""
123) "bgsave_cpulist"
124) ""
125) "ignore-warnings"
126) ""
127) "proc-title-template"
128) "{title} {listen-addr} {server-mode}"
129) "masterauth"
130) ""
131) "requirepass"
132) ""
133) "supervised"
134) "no"
135) "syslog-facility"
136) "local0"
137) "repl-diskless-load"
138) "disabled"
139) "loglevel"
140) "notice"
141) "maxmemory-policy"
142) "noeviction"
143) "appendfsync"
144) "everysec"
145) "oom-score-adj"
146) "no"
147) "acl-pubsub-default"
148) "allchannels"
149) "sanitize-dump-payload"
150) "no"
151) "databases"
152) "16"
153) "port"
154) "6379"
155) "io-threads"
156) "1"
157) "auto-aof-rewrite-percentage"
158) "100"
159) "cluster-replica-validity-factor"
160) "10"
161) "cluster-slave-validity-factor"
162) "10"
163) "list-max-ziplist-size"
164) "-2"
165) "tcp-keepalive"
166) "300"
167) "cluster-migration-barrier"
168) "1"
169) "active-defrag-cycle-min"
170) "1"
171) "active-defrag-cycle-max"
172) "25"
173) "active-defrag-threshold-lower"
174) "10"
175) "active-defrag-threshold-upper"
176) "100"
177) "lfu-log-factor"
178) "10"
179) "lfu-decay-time"
180) "1"
181) "replica-priority"
182) "100"
183) "slave-priority"
184) "100"
185) "repl-diskless-sync-delay"
186) "5"
187) "maxmemory-samples"
188) "5"
189) "maxmemory-eviction-tenacity"
190) "10"
191) "timeout"
192) "0"
193) "replica-announce-port"
194) "0"
195) "slave-announce-port"
196) "0"
197) "tcp-backlog"
198) "511"
199) "cluster-announce-bus-port"
200) "0"
201) "cluster-announce-port"
202) "0"
203) "cluster-announce-tls-port"
204) "0"
205) "repl-timeout"
206) "60"
207) "repl-ping-replica-period"
208) "10"
209) "repl-ping-slave-period"
210) "10"
211) "list-compress-depth"
212) "0"
213) "rdb-key-save-delay"
214) "0"
215) "key-load-delay"
216) "0"
217) "active-expire-effort"
218) "1"
219) "hz"
220) "10"
221) "min-replicas-to-write"
222) "0"
223) "min-slaves-to-write"
224) "0"
225) "min-replicas-max-lag"
226) "10"
227) "min-slaves-max-lag"
228) "10"
229) "maxclients"
230) "10000"
231) "active-defrag-max-scan-fields"
232) "1000"
233) "slowlog-max-len"
234) "128"
235) "acllog-max-len"
236) "128"
237) "lua-time-limit"
238) "5000"
239) "cluster-node-timeout"
240) "15000"
241) "slowlog-log-slower-than"
242) "10000"
243) "latency-monitor-threshold"
244) "0"
245) "proto-max-bulk-len"
246) "536870912"
247) "stream-node-max-entries"
248) "100"
249) "repl-backlog-size"
250) "1048576"
251) "maxmemory"
252) "0"
253) "hash-max-ziplist-entries"
254) "512"
255) "set-max-intset-entries"
256) "512"
257) "zset-max-ziplist-entries"
258) "128"
259) "active-defrag-ignore-bytes"
260) "104857600"
261) "hash-max-ziplist-value"
262) "64"
263) "stream-node-max-bytes"
264) "4096"
265) "zset-max-ziplist-value"
266) "64"
267) "hll-sparse-max-bytes"
268) "3000"
269) "tracking-table-max-keys"
270) "1000000"
271) "client-query-buffer-limit"
272) "1073741824"
273) "repl-backlog-ttl"
274) "3600"
275) "auto-aof-rewrite-min-size"
276) "67108864"
277) "tls-port"
278) "0"
279) "tls-session-cache-size"
280) "20480"
281) "tls-session-cache-timeout"
282) "300"
283) "tls-cluster"
284) "no"
285) "tls-replication"
286) "no"
287) "tls-auth-clients"
288) "yes"
289) "tls-prefer-server-ciphers"
290) "no"
291) "tls-session-caching"
292) "yes"
293) "tls-cert-file"
294) ""
295) "tls-key-file"
296) ""
297) "tls-key-file-pass"
298) ""
299) "tls-client-cert-file"
300) ""
301) "tls-client-key-file"
302) ""
303) "tls-client-key-file-pass"
304) ""
305) "tls-dh-params-file"
306) ""
307) "tls-ca-cert-file"
308) ""
309) "tls-ca-cert-dir"
310) ""
311) "tls-protocols"
312) ""
313) "tls-ciphers"
314) ""
315) "tls-ciphersuites"
316) ""
317) "logfile"
318) ""
319) "watchdog-period"
320) "0"
321) "dir"
322) "/Users/karuppiahn"
323) "save"
324) "3600 1 300 100 60 10000"
325) "client-output-buffer-limit"
326) "normal 0 0 0 slave 268435456 67108864 60 pubsub 33554432 8388608 60"
327) "unixsocketperm"
328) "0"
329) "slaveof"
330) ""
331) "notify-keyspace-events"
332) ""
333) "bind"
334) ""
335) "oom-score-adj-values"
336) "0 200 800"
127.0.0.1:6379> keys *
1) "foo"
127.0.0.1:6379> 
```

https://redis.io/commands/get

Also, I just noticed that all the examples on redis.io docs are all interactive examples!!!! :D Wow!!!!

And oops, I put the wrong docs link!

https://redis.io/commands/config-get

---

I was trying to checkout the redis wire protocol - RESP - REdis Serialization Protocol

```bash
Last login: Wed Aug  4 21:14:43 on ttys002
karuppiahn-a01:~ karuppiahn$ telnet 6379
Trying 0.0.24.235...
telnet: connect to address 0.0.24.235: No route to host
telnet: Unable to connect to remote host
karuppiahn-a01:~ karuppiahn$ telnet localhost 6379
Trying ::1...
Connected to localhost.
Escape character is '^]'.

keys *
*0
^C^C^]
telnet> keys *
?Invalid command
telnet> ^[[A
?Invalid command
telnet> keys
?Invalid command
telnet> help
Commands may be abbreviated.  Commands are:

close   	close current connection
logout  	forcibly logout remote user and close the connection
display 	display operating parameters
mode    	try to enter line or character mode ('mode ?' for more)
telnet  	connect to a site
open    	connect to a site
quit    	exit telnet
send    	transmit special characters ('send ?' for more)
set     	set operating parameters ('set ?' for more)
unset   	unset operating parameters ('unset ?' for more)
status  	print status information
toggle  	toggle operating parameters ('toggle ?' for more)
slc     	change state of special charaters ('slc ?' for more)
auth    	turn on (off) authentication ('auth ?' for more)
z       	suspend telnet
!       	invoke a subshell
environ 	change environment variables ('environ ?' for more)
?       	print help information
telnet> Connection closed.
karuppiahn-a01:~ karuppiahn$ mc
-bash: mc: command not found
karuppiahn-a01:~ karuppiahn$ nc
usage: nc [-46AacCDdEFhklMnOortUuvz] [-K tc] [-b boundif] [-i interval] [-p source_port]
	  [--apple-recv-anyif] [--apple-awdl-unres]
	  [--apple-boundif ifbound]
	  [--apple-no-cellular] [--apple-no-expensive]
	  [--apple-no-flowadv] [--apple-tcp-timeout conntimo]
	  [--apple-tcp-keepalive keepidle] [--apple-tcp-keepintvl keepintvl]
	  [--apple-tcp-keepcnt keepcnt] [--apple-tclass tclass]
	  [--tcp-adp-rtimo num_probes] [--apple-initcoproc-allow]
	  [--apple-tcp-adp-wtimo num_probes]
	  [--setsockopt-later] [--apple-no-connectx]
	  [--apple-delegate-pid pid] [--apple-delegate-uuid uuid]
	  [--apple-kao] [--apple-ext-bk-idle]
	  [--apple-netsvctype svc] [---apple-nowakefromsleep]
	  [--apple-notify-ack] [--apple-sockev]
	  [--apple-tos tos] [--apple-tos-cmsg]
	  [-s source_ip_address] [-w timeout] [-X proxy_version]
	  [-x proxy_address[:port]] [hostname] [port[s]]
karuppiahn-a01:~ karuppiahn$ nc localhost 6379
keys *
*0
GET blah
$-1
SET foo bar
+OK
karuppiahn-a01:~ karuppiahn$ nc localhost 6379
keys *
*1
$3
foo
GET foo
$3
bar
^C
karuppiahn-a01:~ karuppiahn$ 
```

---

It is interesting to see the usual core concepts of Database clients - connection pooling for managing connections

There's also the notion of pipelining which is explained in client performance improvements to avoid a lot of waiting for each of the replies and instead wait just once after sending in all the requests in a pipeline fashion

---

I'm checking out initial tuning now for tuning performance. First thing is around max clients configuration for maximum number of clients

I just modified it in my redis server to see how it works

`maxclients` is the config

```bash
127.0.0.1:6379> CONFIG SET maxclients 1
OK
127.0.0.1:6379> 
```

In a new terminal

```bash
karuppiahn-a01:~ karuppiahn$ redis-cli
127.0.0.1:6379> keys *
(error) ERR max number of clients reached
127.0.0.1:6379> 
```

Also, one cannot set the `maxclients` config value to 0 🤷

```bash
127.0.0.1:6379> CONFIG SET maxclients 0
(error) ERR Invalid argument '0' for CONFIG SET 'maxclients' - argument must be between 1 and 4294967295 inclusive
127.0.0.1:6379> 
```

Interesting! :) :D

Of course negative values have been taken care of too!

```bash
127.0.0.1:6379> CONFIG SET maxclients -1
(error) ERR Invalid argument '-1' for CONFIG SET 'maxclients' - argument must be between 1 and 4294967295 inclusive
127.0.0.1:6379> 
```

And of course invalid datatype values too

```bash
127.0.0.1:6379> CONFIG SET maxclients blah
(error) ERR Invalid argument 'blah' for CONFIG SET 'maxclients' - argument couldn't be parsed into an integer
127.0.0.1:6379> 
```

Interesting that the `maxclients` configuration can be set at runtime using `CONFIG SET`

---

The next configuration I'm reading about is about max memory `maxmemory` which is also a configuration that can be set at runtime in a dynamic fashion to set the max memory that can be used by Redis server

```bash
127.0.0.1:6379> CONFIG GET maxmemory
1) "maxmemory"
2) "0"

127.0.0.1:6379> CONFIG GET blah
(empty array)
127.0.0.1:6379> 
```

---

The next configuration I read about, I didn't exactly get it. It's something about "tcp backlog", something part of the `listen` call for the server to listen I guess? Apparently it has be a big value, bigger than the default value, in case the server is going to get a lot of connections. There's also mention of how the Linux or OS level configuration also has to be tuned to ensure that we get the desired effect. For me, I'm currently running on MacOS, not sure what's the equivalent configuration for the OS in MacOS and how and if it can be changed. Surely I won't run Redis in Mac for production, lol. Anyways, I'll probably come back to this later and read more on it

---

I read the next few sections about tuning performance, I didn't get them all

One was pretty straight forward - scaling reads in a ready-heavy application by having read replicas and also serve stale data from read replicas and also ensure no writes happen on the read-only read replicas

There's something about transparent huge pages at Kernel memory level

Then there's something about Kernel network stack

Then there's file descriptor limits, which I thought about earlier ;) `ulimit`

Finally something about RPS - Receive Packet Steering and CPU preferences, where Redis runs in a particular set of CPU cores while the network handling process / code runs on other cores

---

Now I'm doing the homework questions.

I'm gonna read more about pipelining to understand it better since I don't think I understand it yet

https://redis.io/topics/pipelining

```bash
$ (printf "PING\r\nPING\r\nPING\r\n"; sleep 1) | nc localhost 6379
+PONG
+PONG
+PONG
```

I tried out the ruby code example

```bash

$ ruby redis-labs-university/ru301/week1/
STORY.md               pipelining-example.rb  

$ ruby redis-labs-university/ru301/week1/pipelining-example.rb 
Traceback (most recent call last):
	2: from redis-labs-university/ru301/week1/pipelining-example.rb:2:in \`<main>\'
	1: from /System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/core_ext/kernel_require.rb:54:in \`require\'
/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/2.6.0/rubygems/core_ext/kernel_require.rb:54:in \`require\': cannot load such file -- redis (LoadError)

$ cd redis-labs-university/ru301/week1

$ gem install redis
Fetching redis-4.4.0.gem
ERROR:  While executing gem ... (Gem::FilePermissionError)
    You don\'t have write permissions for the /Library/Ruby/Gems/2.6.0 directory.

$ sudo gem install redis
Password:
Fetching redis-4.4.0.gem
Successfully installed redis-4.4.0
Parsing documentation for redis-4.4.0
Installing ri documentation for redis-4.4.0
Done installing documentation for redis after 0 seconds
1 gem installed

$ ruby pipelining-example.rb 
without pipelining 0.407188 seconds
with pipelining 0.121079 seconds
```


