Interesting to see Sentinels section

I have never used it before actually

I read previously that it monitors primary instances. Actually just one primary. If there are many primaries, then that's more of an active-active thing I guess, where "multi master" concepts would come in

Apparently the Redis Sentinel is a Redis Instance started in sentinel mode. I kind of read this before too, but what I didn't get is, or more like what I don't get now is - how come there's a separate `redis-sentinel` if Sentinel is simply a Redis server / Redis instance which is what `redis-sever` is. Hmm. I mean, it would just be a configuration to say what mode, right?

The role command also spoke about `sentinel` mode https://redis.io/commands/role apart from `master` and `slave`. Hmm

I do have to read https://redis.io/topics/sentinel which I haven't read yet. My bad

I was already jumping to the practical steps of running redis sentinel in 3.4, maybe I'll first read this https://redis.io/topics/sentinel a bit first, for better clarity

Also, there seems to be a lot of quorum - or majority, among the sentinels. I mean, first there's a quorum to agree that the primary is down - makes sense, because maybe there's some networking issue like network partition etc where one sentinel feels that the primary is down, while others know that primary is up and running as their network has no issues. It's hard to say that a system is down, so maybe it makes sense for all the sentinels to agree that a primary is down before doing an automatic failover which is quite a process and no one wants to simply do failovers when the primary is in fact very healthy and that it's just some sentinel issue - where from it's point of view the primary is / seems to be down for some reason. But yeah, if all sentinels see that the primary is down due to some reason even though primary is up, I guess it will trigger a failover. I don't know if that kind of weird situation is possible. But yeah, to trigger failover, the sentinel should atleast be able to connect to the replicas even if there's some issue connecting to / reaching the primary

Apart from the first quorum on deciding if the primary is down or not, there's a second quorum! A second quorum to elect a leader who will do the failover by choosing a replica that has the latest data

Not sure how the replica is chosen and who chooses it - is it the leader, or if it's a quorum etc

But yeah, the leader does the reconfiguring of the replica to a primary is what the redis university RU301 section 3.3 says, which is basically the failover, by doing `replicaof no one` command execution

The leader will also reconfigure the other replicas to follow the new primary it seems! Interesting

All of it is automated, nice

About the clients connecting to the redis, initially they would have connected to the old primary, now to connect to the new primary they need to know that a new primary is available, apparently some client libraries have the feature of supporting sentinels. I think client libraries query the sentinel to understand who is the primary at any given point, especially when connectivity to the primary is failing or not working, and then probably connect to the new primary. I'm just guessing, I gotta confirm this. But this is interesting! Previously I have seen some systems where a proxy is used to transparently change the primary and proxy takes care of always routing to the primary no matter what and clients connect to the proxy. The only problem is that the clients have to try to reconnect to the proxy when there's an error. I have also seen that the proxy automatically stops connections to old primary and opens new connections to the new primary, in this case clients will lose their connection and will have to retry to connect to the proxy. I noticed that proxy model in Stolon for PostgreSQL HA https://github.com/sorintlab/stolon

Anyways, here there's no proxy etc, clients have to simply be aware of the HA system and find the new primary and connect to it!

Now, basically, looks like the sentinel needs to know about the primary - to check it and see if it's up and running and also know about the replicas to be able to reconfigure them when primary changes. I'm reading more now in https://redis.io/topics/sentinel and I just read that it's aware of the primary and the replicas, which makes sense for the above mentioned reasons

I can see some interesting examples and ideas in

https://redis.io/topics/sentinel

I'm now reading example 4 https://redis.io/topics/sentinel#example-4-sentinel-client-side-with-less-than-three-clients

I was trying out the quick tutorial in the page https://redis.io/topics/sentinel

And things didn't seem to work. Also, a similar tutorial / hands-on is what is present in section 3.4 too, so I was checking that and I think I know why things didn't work exactly as expected. Oh wait, no I don't know why things didn't work. Right. Or maybe I do, hmm

So, what I tried was -

run the primary and replica I had created in section 3.2

Primary

```bash
karuppiahn-a01:3.3 karuppiahn$ cd ..
karuppiahn-a01:section3 karuppiahn$ ls
3.2	3.3	3.4
karuppiahn-a01:section3 karuppiahn$ cd 3.2
karuppiahn-a01:3.2 karuppiahn$ ls
STORY.md	dump.rdb	primary.aof	primary.conf	replica.conf
karuppiahn-a01:3.2 karuppiahn$ redis-server primary.conf
5609:C 09 Aug 2021 07:39:40.384 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
5609:C 09 Aug 2021 07:39:40.384 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=5609, just started
5609:C 09 Aug 2021 07:39:40.384 # Configuration loaded
5609:M 09 Aug 2021 07:39:40.385 * Increased maximum number of open files to 10032 (it was originally set to 256).
5609:M 09 Aug 2021 07:39:40.385 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 5609
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

5609:M 09 Aug 2021 07:39:40.386 # Server initialized
5609:M 09 Aug 2021 07:39:40.387 * DB loaded from append only file: 0.001 seconds
5609:M 09 Aug 2021 07:39:40.387 * Ready to accept connections
5609:M 09 Aug 2021 07:39:46.129 * Replica 127.0.0.1:6380 asks for synchronization
5609:M 09 Aug 2021 07:39:46.129 * Partial resynchronization not accepted: Replication ID mismatch (Replica asked for 'fc0057728f174be2eb3eb313dffcf54e3b0a4fd2', my replication IDs are '71a4b7fd10b45e690e371e4de49796085d8abc51' and '0000000000000000000000000000000000000000')
5609:M 09 Aug 2021 07:39:46.129 * Replication backlog created, my new replication IDs are '4553c4a6ead1713efb54071bf1748b2617ec4fbf' and '0000000000000000000000000000000000000000'
5609:M 09 Aug 2021 07:39:46.129 * Starting BGSAVE for SYNC with target: disk
5609:M 09 Aug 2021 07:39:46.129 * Background saving started by pid 5934
5934:C 09 Aug 2021 07:39:46.130 * DB saved on disk
5609:M 09 Aug 2021 07:39:46.206 * Background saving terminated with success
5609:M 09 Aug 2021 07:39:46.207 * Synchronization with replica 127.0.0.1:6380 succeeded
```

Replica -

```bash
Last login: Mon Aug  9 07:38:43 on ttys001
karuppiahn-a01:3.2 karuppiahn$ redis-server replica.conf
5933:C 09 Aug 2021 07:39:46.124 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
5933:C 09 Aug 2021 07:39:46.124 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=5933, just started
5933:C 09 Aug 2021 07:39:46.124 # Configuration loaded
5933:S 09 Aug 2021 07:39:46.125 * Increased maximum number of open files to 10032 (it was originally set to 256).
5933:S 09 Aug 2021 07:39:46.126 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 5933
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

5933:S 09 Aug 2021 07:39:46.127 # Server initialized
5933:S 09 Aug 2021 07:39:46.127 * Loading RDB produced by version 6.2.5
5933:S 09 Aug 2021 07:39:46.127 * RDB age 206415 seconds
5933:S 09 Aug 2021 07:39:46.128 * RDB memory usage when created 2.00 Mb
5933:S 09 Aug 2021 07:39:46.128 * DB loaded from disk: 0.001 seconds
5933:S 09 Aug 2021 07:39:46.128 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
5933:S 09 Aug 2021 07:39:46.128 * Ready to accept connections
5933:S 09 Aug 2021 07:39:46.128 * Connecting to MASTER 127.0.0.1:6379
5933:S 09 Aug 2021 07:39:46.128 * MASTER <-> REPLICA sync started
5933:S 09 Aug 2021 07:39:46.128 * Non blocking connect for SYNC fired the event.
5933:S 09 Aug 2021 07:39:46.128 * Master replied to PING, replication can continue...
5933:S 09 Aug 2021 07:39:46.128 * Trying a partial resynchronization (request fc0057728f174be2eb3eb313dffcf54e3b0a4fd2:8399).
5933:S 09 Aug 2021 07:39:46.129 * Full resync from master: 4553c4a6ead1713efb54071bf1748b2617ec4fbf:0
5933:S 09 Aug 2021 07:39:46.129 * Discarding previously cached master state.
5933:S 09 Aug 2021 07:39:46.207 * MASTER <-> REPLICA sync: receiving 189 bytes from master to disk
5933:S 09 Aug 2021 07:39:46.207 * MASTER <-> REPLICA sync: Flushing old data
5933:S 09 Aug 2021 07:39:46.207 * MASTER <-> REPLICA sync: Loading DB in memory
5933:S 09 Aug 2021 07:39:46.208 * Loading RDB produced by version 6.2.5
5933:S 09 Aug 2021 07:39:46.208 * RDB age 0 seconds
5933:S 09 Aug 2021 07:39:46.208 * RDB memory usage when created 2.06 Mb
5933:S 09 Aug 2021 07:39:46.208 * MASTER <-> REPLICA sync: Finished with success
```

And then I checked the redis-cli for Primary

```bash
127.0.0.1:6379> role
(error) NOAUTH Authentication required.
127.0.0.1:6379> auth a_strong_password
OK
127.0.0.1:6379> role
1) "master"
2) (integer) 28
3) 1) 1) "127.0.0.1"
      2) "6380"
      3) "28"
127.0.0.1:6379> role
1) "master"
2) (integer) 42
3) 1) 1) "127.0.0.1"
      2) "6380"
      3) "28"
127.0.0.1:6379> role
1) "master"
2) (integer) 42
3) 1) 1) "127.0.0.1"
      2) "6380"
      3) "42"
127.0.0.1:6379>
```

I ran sentinels then after creating configs

```bash
karuppiahn-a01:3.3 karuppiahn$ vi sentinel1.conf
karuppiahn-a01:3.3 karuppiahn$ vi sentinel2.conf
karuppiahn-a01:3.3 karuppiahn$ vi sentinel3.conf
karuppiahn-a01:3.3 karuppiahn$ cat sentinel1.conf
port 5000
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1

karuppiahn-a01:3.3 karuppiahn$ cat sentinel2.conf
port 5001
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1

karuppiahn-a01:3.3 karuppiahn$ cat sentinel3.conf
port 5002
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1

karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel1.conf
6618:X 09 Aug 2021 07:41:42.731 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
6618:X 09 Aug 2021 07:41:42.731 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=6618, just started
6618:X 09 Aug 2021 07:41:42.731 # Configuration loaded
6618:X 09 Aug 2021 07:41:42.732 * Increased maximum number of open files to 10032 (it was originally set to 256).
6618:X 09 Aug 2021 07:41:42.732 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5000
 |    `-._   `._    /     _.-'    |     PID: 6618
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

6618:X 09 Aug 2021 07:41:42.735 # Sentinel ID is abe94391011010eb7a991a301c9129fac5ec0409
6618:X 09 Aug 2021 07:41:42.735 # +monitor master mymaster 127.0.0.1 6379 quorum 2
6618:X 09 Aug 2021 07:41:47.784 # +sdown master mymaster 127.0.0.1 6379
```

```bash
Last login: Mon Aug  9 07:40:19 on ttys004
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel2.conf
6953:X 09 Aug 2021 07:41:49.330 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
6953:X 09 Aug 2021 07:41:49.330 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=6953, just started
6953:X 09 Aug 2021 07:41:49.330 # Configuration loaded
6953:X 09 Aug 2021 07:41:49.331 * Increased maximum number of open files to 10032 (it was originally set to 256).
6953:X 09 Aug 2021 07:41:49.331 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5001
 |    `-._   `._    /     _.-'    |     PID: 6953
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

6953:X 09 Aug 2021 07:41:49.334 # Sentinel ID is 89345ea44224358e6c356a1202bcf8515ce58f77
6953:X 09 Aug 2021 07:41:49.334 # +monitor master mymaster 127.0.0.1 6379 quorum 2
6953:X 09 Aug 2021 07:41:54.362 # +sdown master mymaster 127.0.0.1 6379
```

```bash
Last login: Mon Aug  9 07:41:45 on ttys005
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel3.conf
7293:X 09 Aug 2021 07:41:54.568 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
7293:X 09 Aug 2021 07:41:54.568 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=7293, just started
7293:X 09 Aug 2021 07:41:54.568 # Configuration loaded
7293:X 09 Aug 2021 07:41:54.569 * Increased maximum number of open files to 10032 (it was originally set to 256).
7293:X 09 Aug 2021 07:41:54.569 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5002
 |    `-._   `._    /     _.-'    |     PID: 7293
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

7293:X 09 Aug 2021 07:41:54.571 # Sentinel ID is 3708e850553a9e459c3231cd5cd500674c04e22f
7293:X 09 Aug 2021 07:41:54.571 # +monitor master mymaster 127.0.0.1 6379 quorum 2
7293:X 09 Aug 2021 07:41:59.582 # +sdown master mymaster 127.0.0.1 6379
```

```bash
Last login: Mon Aug  9 07:41:50 on ttys006
rekaruppiahn-a01:3.3 karuppiahn$ redis-cli -p 5000
127.0.0.1:5000> SENTINEL MASTER MYMASTER
(error) ERR No such master with that name
127.0.0.1:5000> SENTINEL MASTER myMaster
(error) ERR No such master with that name
127.0.0.1:5000> SENTINEL MASTER mymaster
 1) "name"
 2) "mymaster"
 3) "ip"
 4) "127.0.0.1"
 5) "port"
 6) "6379"
 7) "runid"
 8) ""
 9) "flags"
10) "s_down,master,disconnected"
11) "link-pending-commands"
12) "0"
13) "link-refcount"
14) "1"
15) "last-ping-sent"
16) "76703"
17) "last-ok-ping-reply"
18) "76703"
19) "last-ping-reply"
20) "820"
21) "s-down-time"
22) "71650"
23) "down-after-milliseconds"
24) "5000"
25) "info-refresh"
26) "0"
27) "role-reported"
28) "master"
29) "role-reported-time"
30) "76703"
31) "config-epoch"
32) "0"
33) "num-slaves"
34) "0"
35) "num-other-sentinels"
36) "0"
37) "quorum"
38) "2"
39) "failover-timeout"
40) "60000"
41) "parallel-syncs"
42) "1"
127.0.0.1:5000> SENTINEL MASTER mymaster
 1) "name"
 2) "mymaster"
 3) "ip"
 4) "127.0.0.1"
 5) "port"
 6) "6379"
 7) "runid"
 8) ""
 9) "flags"
10) "s_down,master,disconnected"
11) "link-pending-commands"
12) "0"
13) "link-refcount"
14) "1"
15) "last-ping-sent"
16) "145187"
17) "last-ok-ping-reply"
18) "145187"
19) "last-ping-reply"
20) "37"
21) "s-down-time"
22) "140134"
23) "down-after-milliseconds"
24) "5000"
25) "info-refresh"
26) "0"
27) "role-reported"
28) "master"
29) "role-reported-time"
30) "145187"
31) "config-epoch"
32) "0"
33) "num-slaves"
34) "0"
35) "num-other-sentinels"
36) "0"
37) "quorum"
38) "2"
39) "failover-timeout"
40) "60000"
41) "parallel-syncs"
42) "1"
127.0.0.1:5000>
```

It says 0 for `num-other-sentinels`. It hasn't discovered other sentinels.

Actually, I have no idea how it can discover if there are other sentinels if I don't give any input, that the sentinels are running in my localhost at ports 5000, 5001, 5002. Hmm

The thing is, when I saw section 3.4 I thought maybe I missed the `--sentinel` but that flag is only for using `redis-server` as sentinel or more like running `redis-server` in sentinel mode. But I am using `redis-sentinel` itself, hmm

The one thing that seems like a problem is that my primary and replica have passwords. In section 3.4 I can see password being mentioned in the sentinel config. Maybe that's the reason? Maybe sentinels discover themselves through the master? Hmm, weird, but interesting. Let's see

Now I changed the sentinel configs

```bash
karuppiahn-a01:3.3 karuppiahn$ vi sentinel1.conf
karuppiahn-a01:3.3 karuppiahn$ cat sentinel1.conf
port 5000
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel auth-pass mymaster a_strong_password

# Generated by CONFIG REWRITE
protected-mode no
user default on nopass ~* &* +@all
dir "/Users/karuppiahn/projects/github.com/karuppiah7890/redis-stuff/redis-labs-university/ru301/section3/3.3"
sentinel myid abe94391011010eb7a991a301c9129fac5ec0409
sentinel config-epoch mymaster 0
sentinel leader-epoch mymaster 0
sentinel current-epoch 0
karuppiahn-a01:3.3 karuppiahn$ cat sentinel2.conf
port 5001
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel auth-pass mymaster a_strong_password

# Generated by CONFIG REWRITE
protected-mode no
user default on nopass ~* &* +@all
dir "/Users/karuppiahn/projects/github.com/karuppiah7890/redis-stuff/redis-labs-university/ru301/section3/3.3"
sentinel myid 89345ea44224358e6c356a1202bcf8515ce58f77
sentinel config-epoch mymaster 0
sentinel leader-epoch mymaster 0
sentinel current-epoch 0
karuppiahn-a01:3.3 karuppiahn$ cat sentinel3.conf
port 5002
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel auth-pass mymaster a_strong_password

# Generated by CONFIG REWRITE
protected-mode no
user default on nopass ~* &* +@all
dir "/Users/karuppiahn/projects/github.com/karuppiah7890/redis-stuff/redis-labs-university/ru301/section3/3.3"
sentinel myid 3708e850553a9e459c3231cd5cd500674c04e22f
sentinel config-epoch mymaster 0
sentinel leader-epoch mymaster 0
sentinel current-epoch 0
karuppiahn-a01:3.3 karuppiahn$
```

Woah. Yes. It worked.

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel1.conf
10129:X 09 Aug 2021 07:54:45.543 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10129:X 09 Aug 2021 07:54:45.543 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10129, just started
10129:X 09 Aug 2021 07:54:45.543 # Configuration loaded
10129:X 09 Aug 2021 07:54:45.544 * Increased maximum number of open files to 10032 (it was originally set to 256).
10129:X 09 Aug 2021 07:54:45.544 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5000
 |    `-._   `._    /     _.-'    |     PID: 10129
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10129:X 09 Aug 2021 07:54:45.545 # Sentinel ID is abe94391011010eb7a991a301c9129fac5ec0409
10129:X 09 Aug 2021 07:54:45.545 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10129:X 09 Aug 2021 07:54:45.546 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 07:55:00.373 * +sentinel sentinel 89345ea44224358e6c356a1202bcf8515ce58f77 127.0.0.1 5001 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 07:55:02.940 * +sentinel sentinel 3708e850553a9e459c3231cd5cd500674c04e22f 127.0.0.1 5002 @ mymaster 127.0.0.1 6379
```

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel2.conf
10144:X 09 Aug 2021 07:54:58.352 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10144:X 09 Aug 2021 07:54:58.352 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10144, just started
10144:X 09 Aug 2021 07:54:58.352 # Configuration loaded
10144:X 09 Aug 2021 07:54:58.353 * Increased maximum number of open files to 10032 (it was originally set to 256).
10144:X 09 Aug 2021 07:54:58.353 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5001
 |    `-._   `._    /     _.-'    |     PID: 10144
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10144:X 09 Aug 2021 07:54:58.354 # Sentinel ID is 89345ea44224358e6c356a1202bcf8515ce58f77
10144:X 09 Aug 2021 07:54:58.354 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10144:X 09 Aug 2021 07:54:58.355 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 07:54:59.887 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 07:55:02.940 * +sentinel sentinel 3708e850553a9e459c3231cd5cd500674c04e22f 127.0.0.1 5002 @ mymaster 127.0.0.1 6379
```

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel3.conf
10145:X 09 Aug 2021 07:55:00.935 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10145:X 09 Aug 2021 07:55:00.935 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10145, just started
10145:X 09 Aug 2021 07:55:00.935 # Configuration loaded
10145:X 09 Aug 2021 07:55:00.936 * Increased maximum number of open files to 10032 (it was originally set to 256).
10145:X 09 Aug 2021 07:55:00.936 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5002
 |    `-._   `._    /     _.-'    |     PID: 10145
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10145:X 09 Aug 2021 07:55:00.937 # Sentinel ID is 3708e850553a9e459c3231cd5cd500674c04e22f
10145:X 09 Aug 2021 07:55:00.937 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10145:X 09 Aug 2021 07:55:00.938 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 07:55:01.929 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 07:55:02.382 * +sentinel sentinel 89345ea44224358e6c356a1202bcf8515ce58f77 127.0.0.1 5001 @ mymaster 127.0.0.1 6379
```

```bash
127.0.0.1:5000> SENTINEL MASTER mymaster
 1) "name"
 2) "mymaster"
 3) "ip"
 4) "127.0.0.1"
 5) "port"
 6) "6379"
 7) "runid"
 8) "61de20ae8ff8e44c5a24bd492dbf9d6c4fe9a9f5"
 9) "flags"
10) "master"
11) "link-pending-commands"
12) "0"
13) "link-refcount"
14) "1"
15) "last-ping-sent"
16) "0"
17) "last-ok-ping-reply"
18) "402"
19) "last-ping-reply"
20) "402"
21) "down-after-milliseconds"
22) "5000"
23) "info-refresh"
24) "1132"
25) "role-reported"
26) "master"
27) "role-reported-time"
28) "91516"
29) "config-epoch"
30) "0"
31) "num-slaves"
32) "1"
33) "num-other-sentinels"
34) "2"
35) "quorum"
36) "2"
37) "failover-timeout"
38) "60000"
39) "parallel-syncs"
40) "1"
127.0.0.1:5000>
```

Previously `num-slaves` was 0 and now it's 1. `num-other-sentinels` is 2!! :D `runid` is NOT empty, previously it was empty!!

Also now we can see the logs - `10145:X 09 Aug 2021 07:55:01.929 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379`

Apparently those are events. And one can subscribe to it!! :O

I think previously sentinel detected that master was down. Also, since quorum was 2, it couldn't probably do anything I guess? Since quorum is for failure detection and just one sentinel can't detect a failure and call it out to start off a leader election to go on to doing failover. Also it's impossible in this case when sentinel can't even login to master and reach it, to get replica information by scraping `INFO`

Also, previously `flags` was `s_down,master,disconnected`. Now the value of `flags` is `master`! Oh. Previously there was also a field called `s-down-time`. Oh. I guess all this meant that the master was disconnected / down, huh. It's interesting.

It's also interesting that the Seninels discover each other through the master. Hmm. But yeah, it makes sense, probably for an initial discovery, or discovery at any normal time, where I mean that in a normal time, the master is up and running and the sentinels can monitor the master. If the master is down just when the sentinels start to monitor them, it's more of a setup issue. But once the setup is good - with sentinels, master and replicas up and running, then if there's some issue with master, then sentinels can do their work of failure detection and then failover

From sentinel redis-cli -

```bash
127.0.0.1:5000> SENTINEL master mymaster
 1) "name"
 2) "mymaster"
 3) "ip"
 4) "127.0.0.1"
 5) "port"
 6) "6379"
 7) "runid"
 8) "61de20ae8ff8e44c5a24bd492dbf9d6c4fe9a9f5"
 9) "flags"
10) "master"
11) "link-pending-commands"
12) "0"
13) "link-refcount"
14) "1"
15) "last-ping-sent"
16) "0"
17) "last-ok-ping-reply"
18) "460"
19) "last-ping-reply"
20) "460"
21) "down-after-milliseconds"
22) "5000"
23) "info-refresh"
24) "5363"
25) "role-reported"
26) "master"
27) "role-reported-time"
28) "1299573"
29) "config-epoch"
30) "0"
31) "num-slaves"
32) "1"
33) "num-other-sentinels"
34) "2"
35) "quorum"
36) "2"
37) "failover-timeout"
38) "60000"
39) "parallel-syncs"
40) "1"
127.0.0.1:5000> SENTINEL replicas mymaster
1)  1) "name"
    2) "127.0.0.1:6380"
    3) "ip"
    4) "127.0.0.1"
    5) "port"
    6) "6380"
    7) "runid"
    8) "a3cdfd270ddf65064edc1fc10594fa129d4c347c"
    9) "flags"
   10) "slave"
   11) "link-pending-commands"
   12) "0"
   13) "link-refcount"
   14) "1"
   15) "last-ping-sent"
   16) "0"
   17) "last-ok-ping-reply"
   18) "826"
   19) "last-ping-reply"
   20) "826"
   21) "down-after-milliseconds"
   22) "5000"
   23) "info-refresh"
   24) "6770"
   25) "role-reported"
   26) "slave"
   27) "role-reported-time"
   28) "1300977"
   29) "master-link-down-time"
   30) "0"
   31) "master-link-status"
   32) "ok"
   33) "master-host"
   34) "127.0.0.1"
   35) "master-port"
   36) "6379"
   37) "slave-priority"
   38) "100"
   39) "slave-repl-offset"
   40) "128079"
   41) "replica-announced"
   42) "1"
127.0.0.1:5000> SENTINEL sentinels mymaster
1)  1) "name"
    2) "3708e850553a9e459c3231cd5cd500674c04e22f"
    3) "ip"
    4) "127.0.0.1"
    5) "port"
    6) "5002"
    7) "runid"
    8) "3708e850553a9e459c3231cd5cd500674c04e22f"
    9) "flags"
   10) "sentinel"
   11) "link-pending-commands"
   12) "0"
   13) "link-refcount"
   14) "1"
   15) "last-ping-sent"
   16) "0"
   17) "last-ok-ping-reply"
   18) "200"
   19) "last-ping-reply"
   20) "200"
   21) "down-after-milliseconds"
   22) "5000"
   23) "last-hello-message"
   24) "357"
   25) "voted-leader"
   26) "?"
   27) "voted-leader-epoch"
   28) "0"
2)  1) "name"
    2) "89345ea44224358e6c356a1202bcf8515ce58f77"
    3) "ip"
    4) "127.0.0.1"
    5) "port"
    6) "5001"
    7) "runid"
    8) "89345ea44224358e6c356a1202bcf8515ce58f77"
    9) "flags"
   10) "sentinel"
   11) "link-pending-commands"
   12) "0"
   13) "link-refcount"
   14) "1"
   15) "last-ping-sent"
   16) "0"
   17) "last-ok-ping-reply"
   18) "200"
   19) "last-ping-reply"
   20) "200"
   21) "down-after-milliseconds"
   22) "5000"
   23) "last-hello-message"
   24) "253"
   25) "voted-leader"
   26) "?"
   27) "voted-leader-epoch"
   28) "0"
127.0.0.1:5000>
```

Both `SENTINEL master mymaster` and `SENTINEL MASTER mymaster` worked, hmm ! It's case insesitive when it comes to the command and the argument here, the first argument alone. Surely the second argument is case sensitive, which I checked earlier

So, now we know how to find the master information from the sentinel and also the replica and other sentinel information, given a master name!

```bash
127.0.0.1:5000> SENTINEL get-master-addr-by-name mymaster
1) "127.0.0.1"
2) "6379"
127.0.0.1:5000>
```

I tried to simulate a failover

Apparently one can do some sort of sleep like operation in redis, the doc shows how to

Some failed attempts -

```bash
karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6379 DEBUG sleep 30
(error) NOAUTH Authentication required.
karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6379 DEBUG sleep 30
karuppiahn-a01:3.2 karuppiahn$ redis-cli -h | rg -i auth
redis-cli 6.2.5

Usage: redis-cli [OPTIONS] [cmd [arg [arg ...]]]
  -h <hostname>      Server hostname (default: 127.0.0.1).
  -p <port>          Server port (default: 6379).
  -s <socket>        Server socket (overrides hostname and port).
  -a <password>      Password to use when connecting to the server.
                     You can also use the REDISCLI_AUTH environment
                     variable to pass this password more safely
                     (if both are used, this argument takes precedence).
  --user <username>  Used to send ACL style 'AUTH username pass'. Needs -a.
  --pass <password>  Alias of -a for consistency with the new --user option.
  --askpass          Force user to input password with mask from STDIN.
                     If this argument is used, '-a' and REDISCLI_AUTH
                     environment variable will be ignored.
  -u <uri>           Server URI.
  -r <repeat>        Execute specified command N times.
  -i <interval>      When -r is used, waits <interval> seconds per command.
                     It is possible to specify sub-second times like -i 0.1.
  -n <db>            Database number.
  -3                 Start session in RESP3 protocol mode.
  -x                 Read last argument from STDIN.
  -d <delimiter>     Delimiter between response bulks for raw formatting (default: \n).
  -D <delimiter>     Delimiter between responses for raw formatting (default: \n).
  -c                 Enable cluster mode (follow -ASK and -MOVED redirections).
  -e                 Return exit error code when command execution fails.
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
  --raw              Use raw formatting for replies (default when STDOUT is
                     not a tty).
  --no-raw           Force formatted output even when STDOUT is not a tty.
  --quoted-input     Force input to be handled as quoted strings.
  --csv              Output in CSV format.
  --show-pushes <yn> Whether to print RESP3 PUSH messages.  Enabled by default when
                     STDOUT is a tty but can be overriden with --show-pushes no.
  --stat             Print rolling stats about server: mem, clients, ...
  --latency          Enter a special mode continuously sampling latency.
                     If you use this mode in an interactive session it runs
                     forever displaying real-time stats. Otherwise if --raw or
                     --csv is specified, or if you redirect the output to a non
                     TTY, it samples the latency for 1 second (you can use
                     -i to change the interval), then produces a single output
                     and exits.
  --latency-history  Like --latency but tracking latency changes over time.
                     Default time interval is 15 sec. Change it using -i.
  --latency-dist     Shows latency as a spectrum, requires xterm 256 colors.
                     Default time interval is 1 sec. Change it using -i.
  --lru-test <keys>  Simulate a cache workload with an 80-20 distribution.
  --replica          Simulate a replica showing commands received from the master.
  --rdb <filename>   Transfer an RDB dump from remote server to local file.
                     Use filename of "-" to write to stdout.
  --pipe             Transfer raw Redis protocol from stdin to server.
  --pipe-timeout <n> In --pipe mode, abort with error if after sending all data.
                     no reply is received within <n> seconds.
                     Default timeout: 30. Use 0 to wait forever.
  --bigkeys          Sample Redis keys looking for keys with many elements (complexity).
  --memkeys          Sample Redis keys looking for keys consuming a lot of memory.
  --memkeys-samples <n> Sample Redis keys looking for keys consuming a lot of memory.
                     And define number of key elements to sample
  --hotkeys          Sample Redis keys looking for hot keys.
                     only works when maxmemory-policy is *lfu.
  --scan             List all keys using the SCAN command.
  --pattern <pat>    Keys pattern when using the --scan, --bigkeys or --hotkeys
                     options (default: *).
  --quoted-pattern <pat> Same as --pattern, but the specified string can be
                         quoted, in order to pass an otherwise non binary-safe string.
  --intrinsic-latency <sec> Run a test to measure intrinsic system latency.
                     The test will run for the specified amount of seconds.
  --eval <file>      Send an EVAL command using the Lua script at <file>.
  --ldb              Used with --eval enable the Redis Lua debugger.
  --ldb-sync-mode    Like --ldb but uses the synchronous Lua debugger, in
                     this mode the server is blocked and script changes are
                     not rolled back from the server memory.
  --cluster <command> [args...] [opts...]
                     Cluster Manager command and arguments (see below).
  --verbose          Verbose mode.
  --no-auth-warning  Don't show warning message when using password on command
                     line interface.
  --help             Output this help and exit.
  --version          Output version and exit.

Cluster Manager Commands:
  Use --cluster help to list all available cluster manager commands.

Examples:
  cat /etc/passwd | redis-cli -x set mypasswd
  redis-cli get mypasswd
  redis-cli -r 100 lpush mylist x
  redis-cli -r 100 -i 1 info | grep used_memory_human:
  redis-cli --quoted-input set '"null-\x00-separated"' value
  redis-cli --eval myscript.lua key1 key2 , arg1 arg2 arg3
  redis-cli --scan --pattern '*:12345*'

  (Note: when using --eval the comma separates KEYS[] from ARGV[] items)

When no command is given, redis-cli starts in interactive mode.
Type "help" in interactive mode for information on available commands
and settings.

karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6379 DEBUG sleep 30 --password a_strong_password
(error) NOAUTH Authentication required.
karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6379 --password a_strong_password DEBUG sleep 30
Unrecognized option or bad number of args for: '--password'
```

Passing attempt -

```bash
karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6379 -a a_strong_password DEBUG sleep 30
Warning: Using a password with '-a' or '-u' option on the command line interface may not be safe.

OK
karuppiahn-a01:3.2 karuppiahn$
```

The failover happened. I mean, failure was detected, sentinels tried to do the failover, but the old master couldn't become a replica for some reason. I don't know. The logs of sentinel and master are below -

Sentinel 1

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel1.conf
10129:X 09 Aug 2021 07:54:45.543 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10129:X 09 Aug 2021 07:54:45.543 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10129, just started
10129:X 09 Aug 2021 07:54:45.543 # Configuration loaded
10129:X 09 Aug 2021 07:54:45.544 * Increased maximum number of open files to 10032 (it was originally set to 256).
10129:X 09 Aug 2021 07:54:45.544 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5000
 |    `-._   `._    /     _.-'    |     PID: 10129
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10129:X 09 Aug 2021 07:54:45.545 # Sentinel ID is abe94391011010eb7a991a301c9129fac5ec0409
10129:X 09 Aug 2021 07:54:45.545 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10129:X 09 Aug 2021 07:54:45.546 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 07:55:00.373 * +sentinel sentinel 89345ea44224358e6c356a1202bcf8515ce58f77 127.0.0.1 5001 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 07:55:02.940 * +sentinel sentinel 3708e850553a9e459c3231cd5cd500674c04e22f 127.0.0.1 5002 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:13:09.083 # +tilt #tilt mode entered
10129:X 09 Aug 2021 08:13:39.108 # -tilt #tilt mode exited
10129:X 09 Aug 2021 08:21:59.777 # +sdown master mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:21:59.847 # +odown master mymaster 127.0.0.1 6379 #quorum 3/2
10129:X 09 Aug 2021 08:21:59.847 # +new-epoch 1
10129:X 09 Aug 2021 08:21:59.847 # +try-failover master mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:21:59.849 # +vote-for-leader abe94391011010eb7a991a301c9129fac5ec0409 1
10129:X 09 Aug 2021 08:21:59.853 # 89345ea44224358e6c356a1202bcf8515ce58f77 voted for abe94391011010eb7a991a301c9129fac5ec0409 1
10129:X 09 Aug 2021 08:21:59.853 # 3708e850553a9e459c3231cd5cd500674c04e22f voted for abe94391011010eb7a991a301c9129fac5ec0409 1
10129:X 09 Aug 2021 08:21:59.908 # +elected-leader master mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:21:59.908 # +failover-state-select-slave master mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:21:59.971 # +selected-slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:21:59.971 * +failover-state-send-slaveof-noone slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:22:00.033 * +failover-state-wait-promotion slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:22:00.898 # +promoted-slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:22:00.898 # +failover-state-reconf-slaves master mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:22:00.977 # +failover-end master mymaster 127.0.0.1 6379
10129:X 09 Aug 2021 08:22:00.977 # +switch-master mymaster 127.0.0.1 6379 127.0.0.1 6380
10129:X 09 Aug 2021 08:22:00.977 * +slave slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10129:X 09 Aug 2021 08:22:06.057 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10129:X 09 Aug 2021 08:22:24.548 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10129:X 09 Aug 2021 08:22:34.518 * +convert-to-slave slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10129:X 09 Aug 2021 08:23:54.479 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
```

Sentinel 2

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel2.conf
10144:X 09 Aug 2021 07:54:58.352 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10144:X 09 Aug 2021 07:54:58.352 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10144, just started
10144:X 09 Aug 2021 07:54:58.352 # Configuration loaded
10144:X 09 Aug 2021 07:54:58.353 * Increased maximum number of open files to 10032 (it was originally set to 256).
10144:X 09 Aug 2021 07:54:58.353 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5001
 |    `-._   `._    /     _.-'    |     PID: 10144
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10144:X 09 Aug 2021 07:54:58.354 # Sentinel ID is 89345ea44224358e6c356a1202bcf8515ce58f77
10144:X 09 Aug 2021 07:54:58.354 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10144:X 09 Aug 2021 07:54:58.355 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 07:54:59.887 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 07:55:02.940 * +sentinel sentinel 3708e850553a9e459c3231cd5cd500674c04e22f 127.0.0.1 5002 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 08:13:09.083 # +tilt #tilt mode entered
10144:X 09 Aug 2021 08:13:39.162 # -tilt #tilt mode exited
10144:X 09 Aug 2021 08:21:59.765 # +sdown master mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 08:21:59.851 # +new-epoch 1
10144:X 09 Aug 2021 08:21:59.852 # +vote-for-leader abe94391011010eb7a991a301c9129fac5ec0409 1
10144:X 09 Aug 2021 08:21:59.856 # +odown master mymaster 127.0.0.1 6379 #quorum 2/2
10144:X 09 Aug 2021 08:21:59.856 # Next failover delay: I will not start a failover before Mon Aug  9 08:24:00 2021
10144:X 09 Aug 2021 08:22:00.980 # +config-update-from sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 08:22:00.980 # +switch-master mymaster 127.0.0.1 6379 127.0.0.1 6380
10144:X 09 Aug 2021 08:22:00.980 * +slave slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:22:05.996 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:22:24.519 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:23:54.457 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
```

Sentinel 3

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel3.conf
10145:X 09 Aug 2021 07:55:00.935 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10145:X 09 Aug 2021 07:55:00.935 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10145, just started
10145:X 09 Aug 2021 07:55:00.935 # Configuration loaded
10145:X 09 Aug 2021 07:55:00.936 * Increased maximum number of open files to 10032 (it was originally set to 256).
10145:X 09 Aug 2021 07:55:00.936 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5002
 |    `-._   `._    /     _.-'    |     PID: 10145
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10145:X 09 Aug 2021 07:55:00.937 # Sentinel ID is 3708e850553a9e459c3231cd5cd500674c04e22f
10145:X 09 Aug 2021 07:55:00.937 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10145:X 09 Aug 2021 07:55:00.938 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 07:55:01.929 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 07:55:02.382 * +sentinel sentinel 89345ea44224358e6c356a1202bcf8515ce58f77 127.0.0.1 5001 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 08:13:09.083 # +tilt #tilt mode entered
10145:X 09 Aug 2021 08:13:39.110 # -tilt #tilt mode exited
10145:X 09 Aug 2021 08:21:59.735 # +sdown master mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 08:21:59.851 # +new-epoch 1
10145:X 09 Aug 2021 08:21:59.852 # +vote-for-leader abe94391011010eb7a991a301c9129fac5ec0409 1
10145:X 09 Aug 2021 08:22:00.820 # +odown master mymaster 127.0.0.1 6379 #quorum 3/2
10145:X 09 Aug 2021 08:22:00.820 # Next failover delay: I will not start a failover before Mon Aug  9 08:24:00 2021
10145:X 09 Aug 2021 08:22:00.980 # +config-update-from sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 08:22:00.980 # +switch-master mymaster 127.0.0.1 6379 127.0.0.1 6380
10145:X 09 Aug 2021 08:22:00.980 * +slave slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:22:06.016 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:22:24.481 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:23:54.503 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
```

Old master / primary logs are in an adjacent file - old-primary.log

Old Replica / new master / new primary logs -

```bash
Last login: Mon Aug  9 07:38:43 on ttys001
karuppiahn-a01:3.2 karuppiahn$ redis-server replica.conf
5933:C 09 Aug 2021 07:39:46.124 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
5933:C 09 Aug 2021 07:39:46.124 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=5933, just started
5933:C 09 Aug 2021 07:39:46.124 # Configuration loaded
5933:S 09 Aug 2021 07:39:46.125 * Increased maximum number of open files to 10032 (it was originally set to 256).
5933:S 09 Aug 2021 07:39:46.126 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 5933
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

5933:S 09 Aug 2021 07:39:46.127 # Server initialized
5933:S 09 Aug 2021 07:39:46.127 * Loading RDB produced by version 6.2.5
5933:S 09 Aug 2021 07:39:46.127 * RDB age 206415 seconds
5933:S 09 Aug 2021 07:39:46.128 * RDB memory usage when created 2.00 Mb
5933:S 09 Aug 2021 07:39:46.128 * DB loaded from disk: 0.001 seconds
5933:S 09 Aug 2021 07:39:46.128 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
5933:S 09 Aug 2021 07:39:46.128 * Ready to accept connections
5933:S 09 Aug 2021 07:39:46.128 * Connecting to MASTER 127.0.0.1:6379
5933:S 09 Aug 2021 07:39:46.128 * MASTER <-> REPLICA sync started
5933:S 09 Aug 2021 07:39:46.128 * Non blocking connect for SYNC fired the event.
5933:S 09 Aug 2021 07:39:46.128 * Master replied to PING, replication can continue...
5933:S 09 Aug 2021 07:39:46.128 * Trying a partial resynchronization (request fc0057728f174be2eb3eb313dffcf54e3b0a4fd2:8399).
5933:S 09 Aug 2021 07:39:46.129 * Full resync from master: 4553c4a6ead1713efb54071bf1748b2617ec4fbf:0
5933:S 09 Aug 2021 07:39:46.129 * Discarding previously cached master state.
5933:S 09 Aug 2021 07:39:46.207 * MASTER <-> REPLICA sync: receiving 189 bytes from master to disk
5933:S 09 Aug 2021 07:39:46.207 * MASTER <-> REPLICA sync: Flushing old data
5933:S 09 Aug 2021 07:39:46.207 * MASTER <-> REPLICA sync: Loading DB in memory
5933:S 09 Aug 2021 07:39:46.208 * Loading RDB produced by version 6.2.5
5933:S 09 Aug 2021 07:39:46.208 * RDB age 0 seconds
5933:S 09 Aug 2021 07:39:46.208 * RDB memory usage when created 2.06 Mb
5933:S 09 Aug 2021 07:39:46.208 * MASTER <-> REPLICA sync: Finished with success
5933:S 09 Aug 2021 08:13:09.286 # Connection with master lost.
5933:S 09 Aug 2021 08:13:09.286 * Caching the disconnected master state.
5933:S 09 Aug 2021 08:13:09.286 * Reconnecting to MASTER 127.0.0.1:6379
5933:S 09 Aug 2021 08:13:09.287 * MASTER <-> REPLICA sync started
5933:S 09 Aug 2021 08:13:09.287 * Non blocking connect for SYNC fired the event.
5933:S 09 Aug 2021 08:13:09.288 * Master replied to PING, replication can continue...
5933:S 09 Aug 2021 08:13:09.288 * Trying a partial resynchronization (request 4553c4a6ead1713efb54071bf1748b2617ec4fbf:90986).
5933:S 09 Aug 2021 08:13:09.289 * Successful partial resynchronization with master.
5933:S 09 Aug 2021 08:13:09.289 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
5933:M 09 Aug 2021 08:22:00.034 # Connection with master lost.
5933:M 09 Aug 2021 08:22:00.034 * Caching the disconnected master state.
5933:M 09 Aug 2021 08:22:00.034 * Discarding previously cached master state.
5933:M 09 Aug 2021 08:22:00.034 # Setting secondary replication ID to 4553c4a6ead1713efb54071bf1748b2617ec4fbf, valid up to offset: 193472. New replication ID is fb0b12019c270fcf79173c6f4b27c392dccd66cc
5933:M 09 Aug 2021 08:22:00.034 * MASTER MODE enabled (user request from 'id=5 addr=127.0.0.1:51836 laddr=127.0.0.1:6380 fd=9 name=sentinel-abe94391-cmd age=1635 idle=1 flags=x db=0 sub=0 psub=0 multi=4 qbuf=188 qbuf-free=65342 argv-mem=4 obl=45 oll=0 omem=0 tot-mem=82980 events=r cmd=exec user=default redir=-1')
5933:M 09 Aug 2021 08:22:00.037 # CONFIG REWRITE executed with success.
```

Note the `MASTER MODE enabled` log

I was checking the old primary log. It's crazy. I think the reason for the old primary not becoming replica could be because of the password - still checking. Also, I had to stop the old primary at some point. It was so crazy, lot of logs and what not. It kept putting out tons of logs.

Currently the sentinel configuration files look like this after the failover -

```bash
karuppiahn-a01:3.3 karuppiahn$ cat sentinel1.conf
port 5000
sentinel monitor mymaster 127.0.0.1 6380 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel auth-pass mymaster a_strong_password

# Generated by CONFIG REWRITE
protected-mode no
user default on nopass sanitize-payload ~* &* +@all
dir "/Users/karuppiahn/projects/github.com/karuppiah7890/redis-stuff/redis-labs-university/ru301/section3/3.3"
sentinel myid abe94391011010eb7a991a301c9129fac5ec0409
sentinel config-epoch mymaster 1
sentinel leader-epoch mymaster 1
sentinel current-epoch 1
sentinel known-replica mymaster 127.0.0.1 6379
sentinel known-sentinel mymaster 127.0.0.1 5002 3708e850553a9e459c3231cd5cd500674c04e22f
sentinel known-sentinel mymaster 127.0.0.1 5001 89345ea44224358e6c356a1202bcf8515ce58f77
karuppiahn-a01:3.3 karuppiahn$ cat sentinel2.conf
port 5001
sentinel monitor mymaster 127.0.0.1 6380 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel auth-pass mymaster a_strong_password

# Generated by CONFIG REWRITE
protected-mode no
user default on nopass sanitize-payload ~* &* +@all
dir "/Users/karuppiahn/projects/github.com/karuppiah7890/redis-stuff/redis-labs-university/ru301/section3/3.3"
sentinel myid 89345ea44224358e6c356a1202bcf8515ce58f77
sentinel config-epoch mymaster 1
sentinel leader-epoch mymaster 1
sentinel current-epoch 1
sentinel known-replica mymaster 127.0.0.1 6379
sentinel known-sentinel mymaster 127.0.0.1 5000 abe94391011010eb7a991a301c9129fac5ec0409
sentinel known-sentinel mymaster 127.0.0.1 5002 3708e850553a9e459c3231cd5cd500674c04e22f
karuppiahn-a01:3.3 karuppiahn$ cat sentinel3.conf
port 5002
sentinel monitor mymaster 127.0.0.1 6380 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel auth-pass mymaster a_strong_password

# Generated by CONFIG REWRITE
protected-mode no
user default on nopass sanitize-payload ~* &* +@all
dir "/Users/karuppiahn/projects/github.com/karuppiah7890/redis-stuff/redis-labs-university/ru301/section3/3.3"
sentinel myid 3708e850553a9e459c3231cd5cd500674c04e22f
sentinel config-epoch mymaster 1
sentinel leader-epoch mymaster 1
sentinel current-epoch 1
sentinel known-replica mymaster 127.0.0.1 6379
sentinel known-sentinel mymaster 127.0.0.1 5001 89345ea44224358e6c356a1202bcf8515ce58f77
sentinel known-sentinel mymaster 127.0.0.1 5000 abe94391011010eb7a991a301c9129fac5ec0409
karuppiahn-a01:3.3 karuppiahn$
```

About the old primary logs, I think it's safe to say that it's simply a repetition of the last few lines of this log, at least most of the logs are the same. I just checked. Same error repeating over and over and over again

```bash
karuppiahn-a01:3.2 karuppiahn$ redis-server primary.conf
5609:C 09 Aug 2021 07:39:40.384 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
5609:C 09 Aug 2021 07:39:40.384 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=5609, just started
5609:C 09 Aug 2021 07:39:40.384 # Configuration loaded
5609:M 09 Aug 2021 07:39:40.385 * Increased maximum number of open files to 10032 (it was originally set to 256).
5609:M 09 Aug 2021 07:39:40.385 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 5609
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

5609:M 09 Aug 2021 07:39:40.386 # Server initialized
5609:M 09 Aug 2021 07:39:40.387 * DB loaded from append only file: 0.001 seconds
5609:M 09 Aug 2021 07:39:40.387 * Ready to accept connections
5609:M 09 Aug 2021 07:39:46.129 * Replica 127.0.0.1:6380 asks for synchronization
5609:M 09 Aug 2021 07:39:46.129 * Partial resynchronization not accepted: Replication ID mismatch (Replica asked for 'fc0057728f174be2eb3eb313dffcf54e3b0a4fd2', my replication IDs are '71a4b7fd10b45e690e371e4de49796085d8abc51' and '0000000000000000000000000000000000000000')
5609:M 09 Aug 2021 07:39:46.129 * Replication backlog created, my new replication IDs are '4553c4a6ead1713efb54071bf1748b2617ec4fbf' and '0000000000000000000000000000000000000000'
5609:M 09 Aug 2021 07:39:46.129 * Starting BGSAVE for SYNC with target: disk
5609:M 09 Aug 2021 07:39:46.129 * Background saving started by pid 5934
5934:C 09 Aug 2021 07:39:46.130 * DB saved on disk
5609:M 09 Aug 2021 07:39:46.206 * Background saving terminated with success
5609:M 09 Aug 2021 07:39:46.207 * Synchronization with replica 127.0.0.1:6380 succeeded
5609:M 09 Aug 2021 08:13:09.286 # Disconnecting timedout replica (streaming sync): 127.0.0.1:6380
5609:M 09 Aug 2021 08:13:09.286 # Connection with replica 127.0.0.1:6380 lost.
5609:M 09 Aug 2021 08:13:09.288 * Replica 127.0.0.1:6380 asks for synchronization
5609:M 09 Aug 2021 08:13:09.288 * Partial resynchronization request from 127.0.0.1:6380 accepted. Sending 0 bytes of backlog starting from offset 90986.
5609:M 09 Aug 2021 08:22:24.468 # Connection with replica client id #2082 lost.
5609:S 09 Aug 2021 08:22:34.518 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
5609:S 09 Aug 2021 08:22:34.518 * Connecting to MASTER 127.0.0.1:6380
5609:S 09 Aug 2021 08:22:34.518 * MASTER <-> REPLICA sync started
5609:S 09 Aug 2021 08:22:34.519 * REPLICAOF 127.0.0.1:6380 enabled (user request from 'id=2102 addr=127.0.0.1:51994 laddr=127.0.0.1:6379 fd=33 name=sentinel-abe94391-cmd age=10 idle=0 flags=x db=0 sub=0 psub=0 multi=4 qbuf=196 qbuf-free=65334 argv-mem=4 obl=45 oll=0 omem=0 tot-mem=82980 events=r cmd=exec user=default redir=-1')
5609:S 09 Aug 2021 08:22:34.521 # CONFIG REWRITE executed with success.
5609:S 09 Aug 2021 08:22:34.522 * Non blocking connect for SYNC fired the event.
5609:S 09 Aug 2021 08:22:34.522 * Master replied to PING, replication can continue...
5609:S 09 Aug 2021 08:22:34.522 * (Non critical) Master does not understand REPLCONF listening-port: -NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.522 * (Non critical) Master does not understand REPLCONF capa: -NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.522 * Trying a partial resynchronization (request 4553c4a6ead1713efb54071bf1748b2617ec4fbf:254456).
5609:S 09 Aug 2021 08:22:34.522 # Unexpected reply to PSYNC from master: -NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.522 * Discarding previously cached master state.
5609:S 09 Aug 2021 08:22:34.522 * Retrying with SYNC...
5609:S 09 Aug 2021 08:22:34.523 # MASTER aborted replication with an error: NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.523 * Reconnecting to MASTER 127.0.0.1:6380 after failure
5609:S 09 Aug 2021 08:22:34.523 * MASTER <-> REPLICA sync started
5609:S 09 Aug 2021 08:22:34.523 * Non blocking connect for SYNC fired the event.
5609:S 09 Aug 2021 08:22:34.523 * Master replied to PING, replication can continue...
5609:S 09 Aug 2021 08:22:34.523 * (Non critical) Master does not understand REPLCONF listening-port: -NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.523 * (Non critical) Master does not understand REPLCONF capa: -NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.523 * Partial resynchronization not possible (no cached master)
5609:S 09 Aug 2021 08:22:34.524 # Unexpected reply to PSYNC from master: -NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.524 * Retrying with SYNC...
5609:S 09 Aug 2021 08:22:34.524 # MASTER aborted replication with an error: NOAUTH Authentication required.
5609:S 09 Aug 2021 08:22:34.524 * Reconnecting to MASTER 127.0.0.1:6380 after failure
```

It simply says `NOAUTH Authentication required` everywhere. Weird part is how it says `Master replied to PING, replication can continue...`. I see that even for `PING` command the auth is required

Not sure how to fix this kind of issue. I mean, I setup replica with auth, yes. For sentinel, I didn't give any replica information. Sentinel is supposed to scrape replica information from the monitored masters. It should have known about the auth somewhere. Hmm.

Section 3.4 also says the same thing. Hmm. I mean, it doesn't any new information apart from what we know and have done till now

Once I killed the replica process too, the sentinels showed some extra logs, also when I started killing sentinels too

Sentinel 2 logs -

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel2.conf
10144:X 09 Aug 2021 07:54:58.352 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10144:X 09 Aug 2021 07:54:58.352 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10144, just started
10144:X 09 Aug 2021 07:54:58.352 # Configuration loaded
10144:X 09 Aug 2021 07:54:58.353 * Increased maximum number of open files to 10032 (it was originally set to 256).
10144:X 09 Aug 2021 07:54:58.353 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5001
 |    `-._   `._    /     _.-'    |     PID: 10144
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10144:X 09 Aug 2021 07:54:58.354 # Sentinel ID is 89345ea44224358e6c356a1202bcf8515ce58f77
10144:X 09 Aug 2021 07:54:58.354 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10144:X 09 Aug 2021 07:54:58.355 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 07:54:59.887 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 07:55:02.940 * +sentinel sentinel 3708e850553a9e459c3231cd5cd500674c04e22f 127.0.0.1 5002 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 08:13:09.083 # +tilt #tilt mode entered
10144:X 09 Aug 2021 08:13:39.162 # -tilt #tilt mode exited
10144:X 09 Aug 2021 08:21:59.765 # +sdown master mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 08:21:59.851 # +new-epoch 1
10144:X 09 Aug 2021 08:21:59.852 # +vote-for-leader abe94391011010eb7a991a301c9129fac5ec0409 1
10144:X 09 Aug 2021 08:21:59.856 # +odown master mymaster 127.0.0.1 6379 #quorum 2/2
10144:X 09 Aug 2021 08:21:59.856 # Next failover delay: I will not start a failover before Mon Aug  9 08:24:00 2021
10144:X 09 Aug 2021 08:22:00.980 # +config-update-from sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10144:X 09 Aug 2021 08:22:00.980 # +switch-master mymaster 127.0.0.1 6379 127.0.0.1 6380
10144:X 09 Aug 2021 08:22:00.980 * +slave slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:22:05.996 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:22:24.519 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:23:54.457 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:43:14.415 # +tilt #tilt mode entered
10144:X 09 Aug 2021 08:43:44.439 # -tilt #tilt mode exited
10144:X 09 Aug 2021 08:45:13.369 * +reboot slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:45:13.423 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 08:45:19.444 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 09:42:51.088 # +sdown master mymaster 127.0.0.1 6380
10144:X 09 Aug 2021 09:42:51.120 # +new-epoch 2
10144:X 09 Aug 2021 09:42:51.121 # +vote-for-leader 3708e850553a9e459c3231cd5cd500674c04e22f 2
10144:X 09 Aug 2021 09:42:51.172 # +odown master mymaster 127.0.0.1 6380 #quorum 3/2
10144:X 09 Aug 2021 09:42:51.172 # Next failover delay: I will not start a failover before Mon Aug  9 09:44:51 2021
10144:X 09 Aug 2021 09:43:26.974 # +sdown sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6380
^C10144:signal-handler (1628482417) Received SIGINT scheduling shutdown...
10144:X 09 Aug 2021 09:43:37.490 # User requested shutdown...
10144:X 09 Aug 2021 09:43:37.490 # Sentinel is now ready to exit, bye bye...
karuppiahn-a01:3.3 karuppiahn$
```

Sentinel 3 logs -

```bash
karuppiahn-a01:3.3 karuppiahn$ redis-sentinel sentinel3.conf
10145:X 09 Aug 2021 07:55:00.935 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
10145:X 09 Aug 2021 07:55:00.935 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=10145, just started
10145:X 09 Aug 2021 07:55:00.935 # Configuration loaded
10145:X 09 Aug 2021 07:55:00.936 * Increased maximum number of open files to 10032 (it was originally set to 256).
10145:X 09 Aug 2021 07:55:00.936 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in sentinel mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 5002
 |    `-._   `._    /     _.-'    |     PID: 10145
  `-._    `-._  `-./  _.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |           https://redis.io
  `-._    `-._`-.__.-'_.-'    _.-'
 |`-._`-._    `-.__.-'    _.-'_.-'|
 |    `-._`-._        _.-'_.-'    |
  `-._    `-._`-.__.-'_.-'    _.-'
      `-._    `-.__.-'    _.-'
          `-._        _.-'
              `-.__.-'

10145:X 09 Aug 2021 07:55:00.937 # Sentinel ID is 3708e850553a9e459c3231cd5cd500674c04e22f
10145:X 09 Aug 2021 07:55:00.937 # +monitor master mymaster 127.0.0.1 6379 quorum 2
10145:X 09 Aug 2021 07:55:00.938 * +slave slave 127.0.0.1:6380 127.0.0.1 6380 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 07:55:01.929 * +sentinel sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 07:55:02.382 * +sentinel sentinel 89345ea44224358e6c356a1202bcf8515ce58f77 127.0.0.1 5001 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 08:13:09.083 # +tilt #tilt mode entered
10145:X 09 Aug 2021 08:13:39.110 # -tilt #tilt mode exited
10145:X 09 Aug 2021 08:21:59.735 # +sdown master mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 08:21:59.851 # +new-epoch 1
10145:X 09 Aug 2021 08:21:59.852 # +vote-for-leader abe94391011010eb7a991a301c9129fac5ec0409 1
10145:X 09 Aug 2021 08:22:00.820 # +odown master mymaster 127.0.0.1 6379 #quorum 3/2
10145:X 09 Aug 2021 08:22:00.820 # Next failover delay: I will not start a failover before Mon Aug  9 08:24:00 2021
10145:X 09 Aug 2021 08:22:00.980 # +config-update-from sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6379
10145:X 09 Aug 2021 08:22:00.980 # +switch-master mymaster 127.0.0.1 6379 127.0.0.1 6380
10145:X 09 Aug 2021 08:22:00.980 * +slave slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:22:06.016 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:22:24.481 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:23:54.503 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:45:13.694 * +reboot slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:45:13.781 # -sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 08:45:19.739 # +sdown slave 127.0.0.1:6379 127.0.0.1 6379 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:42:51.064 # +sdown master mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:42:51.117 # +odown master mymaster 127.0.0.1 6380 #quorum 2/2
10145:X 09 Aug 2021 09:42:51.117 # +new-epoch 2
10145:X 09 Aug 2021 09:42:51.117 # +try-failover master mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:42:51.119 # +vote-for-leader 3708e850553a9e459c3231cd5cd500674c04e22f 2
10145:X 09 Aug 2021 09:42:51.121 # 89345ea44224358e6c356a1202bcf8515ce58f77 voted for 3708e850553a9e459c3231cd5cd500674c04e22f 2
10145:X 09 Aug 2021 09:42:51.121 # abe94391011010eb7a991a301c9129fac5ec0409 voted for 3708e850553a9e459c3231cd5cd500674c04e22f 2
10145:X 09 Aug 2021 09:42:51.193 # +elected-leader master mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:42:51.193 # +failover-state-select-slave master mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:42:51.249 # -failover-abort-no-good-slave master mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:42:51.309 # Next failover delay: I will not start a failover before Mon Aug  9 09:44:51 2021
10145:X 09 Aug 2021 09:43:26.905 # +sdown sentinel abe94391011010eb7a991a301c9129fac5ec0409 127.0.0.1 5000 @ mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:43:42.064 # -odown master mymaster 127.0.0.1 6380
10145:X 09 Aug 2021 09:43:42.583 # +sdown sentinel 89345ea44224358e6c356a1202bcf8515ce58f77 127.0.0.1 5001 @ mymaster 127.0.0.1 6380
^C10145:signal-handler (1628482423) Received SIGINT scheduling shutdown...
10145:X 09 Aug 2021 09:43:43.901 # User requested shutdown...
10145:X 09 Aug 2021 09:43:43.901 # Sentinel is now ready to exit, bye bye...
karuppiahn-a01:3.3 karuppiahn$
karuppiahn-a01:3.3 karuppiahn$
karuppiahn-a01:3.3 karuppiahn$
```

I'll probably have to get back to this and then see how failover works when the primary and replicas both have password protected Redis instances

---

Now I'm reading the remaining parts of the Sentinel docs https://redis.io/topics/sentinel after the tutorial, which is starting from the Sentinel API https://redis.io/topics/sentinel#sentinel-api

I finished reading and skimming through
- https://redis.io/topics/sentinel#sentinel-api
- https://redis.io/topics/sentinel#sentinel-commands
- https://redis.io/topics/sentinel#reconfiguring-sentinel-at-runtime
- https://redis.io/topics/sentinel#adding-or-removing-sentinels
- https://redis.io/topics/sentinel#removing-the-old-master-or-unreachable-replicas
- https://redis.io/topics/sentinel#pubsub-messages
- https://redis.io/topics/sentinel#handling-of--busy-state
- https://redis.io/topics/sentinel#replicas-priority
- https://redis.io/topics/sentinel#sentinel-and-redis-authentication
- https://redis.io/topics/sentinel#redis-access-control-list-authentication
- https://redis.io/topics/sentinel#redis-password-only-authentication
- https://redis.io/topics/sentinel#configuring-sentinel-instances-with-authentication
- https://redis.io/topics/sentinel#sentinel-access-control-list-authentication
- https://redis.io/topics/sentinel#sentinel-password-only-authentication
- https://redis.io/topics/sentinel#sentinel-clients-implementation

Next I'm planning to read https://redis.io/topics/sentinel#more-advanced-concepts and the other sections after it

In the mean time I also noticed a lot of stuff while reading all these sections that I had read

I understood what was probably going wrong with my setup of primary and replica where the failover didn't work - as in, the old primary didn't become a replica due to the authentication issue because of a configuration that I didn't use in it! I understood this when I was reading the section - https://redis.io/topics/sentinel#redis-password-only-authentication

I also found out some new topic pages! :)

https://redis.io/topics/sentinel-clients [TODO]

https://redis.io/topics/acl [TODO]

Which I plan to read :D

In the meanwhile, I also planned to contribute to the redis documentation to improve the references to sections within the Redis Sentinel Topic Doc

https://duckduckgo.com/?q=redis+docs+github&t=ffab&ia=web

https://github.com/redis/redis-doc

I created this issue - https://github.com/redis/redis-doc/issues/1625 to talk about it

Some more TODOs -
- Try out programs with Redis client libraries with Sentinel support to connect to Redis and interact with it [TODO]
    - Try out in different programming languages to understand how it looks like based on the language idiomatics
        - Golang
        - JavaScript with NodeJs runtime
        - Java
        - Kotlin (probably similar to Java?)
        - Python

- A sample program to try could be to send PING command or other commands to a HA redis setup with Sentinel and then failover the primary - either force failover using the Sentinel or kill the primary using `kill` command or `Ctrl + C` in the terminal

- Another sample program to try could be to listen to the Sentinel's channels - subscribe to them and listen to different kinds of events and messages. Maybe use `PSUBSCRIBE *` or just `SUBSCRIBE` to subscribe to individual channels

- Another idea is to - Create a visualization to see how Redis Sentinel works along with Redis Primary and Redis Replicas and what all it does and the sequence of actions it does. Animated visualization, along with still images

- Another visualization idea is to create a visualization to show the different example setups shown in https://redis.io/topics/sentinel page and show it can be problematic in different situations. Animated visualization, along with still images

All the visualization ideas are based on the visualization that I have in my head to understand the different things explained in the Sentinel doc
