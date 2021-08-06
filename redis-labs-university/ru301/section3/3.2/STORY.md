I was trying out the primary and replica redis servers locally but this time with redis config files and also with password protected redis instances

Primary Server -

```bash
karuppiahn-a01:3.2 karuppiahn$ touch primary.conf
karuppiahn-a01:3.2 karuppiahn$ vi primary.conf
karuppiahn-a01:3.2 karuppiahn$ cat primary.conf
# Create a strong password here
requirepass a_strong_password

# Enable AOF file persistence
appendonly yes

# Choose a name for the AOF file
appendfilename "primary.aof"

karuppiahn-a01:3.2 karuppiahn$ redis-server primary.conf
22633:C 06 Aug 2021 15:37:23.539 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
22633:C 06 Aug 2021 15:37:23.539 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=22633, just started
22633:C 06 Aug 2021 15:37:23.539 # Configuration loaded
22633:M 06 Aug 2021 15:37:23.540 * Increased maximum number of open files to 10032 (it was originally set to 256).
22633:M 06 Aug 2021 15:37:23.540 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 22633
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

22633:M 06 Aug 2021 15:37:23.541 # Server initialized
22633:M 06 Aug 2021 15:37:23.541 * Ready to accept connections
22633:M 06 Aug 2021 15:38:35.180 * Replica 127.0.0.1:6380 asks for synchronization
22633:M 06 Aug 2021 15:38:35.180 * Full resync requested by replica 127.0.0.1:6380
22633:M 06 Aug 2021 15:38:35.180 * Replication backlog created, my new replication IDs are 'fc0057728f174be2eb3eb313dffcf54e3b0a4fd2' and '0000000000000000000000000000000000000000'
22633:M 06 Aug 2021 15:38:35.180 * Starting BGSAVE for SYNC with target: disk
22633:M 06 Aug 2021 15:38:35.181 * Background saving started by pid 23025
23025:C 06 Aug 2021 15:38:35.182 * DB saved on disk
22633:M 06 Aug 2021 15:38:35.239 * Background saving terminated with success
22633:M 06 Aug 2021 15:38:35.239 * Synchronization with replica 127.0.0.1:6380 succeeded
```

Replica Server -

```bash
karuppiahn-a01:3.2 karuppiahn$ touch replica.conf
karuppiahn-a01:3.2 karuppiahn$ vi replica.conf
karuppiahn-a01:3.2 karuppiahn$ cat replica.conf
# Port on which the replica should run
port 6380

# Address of the primary instance
replicaof 127.0.0.1 6379

# AUTH password of the primary instance
masterauth a_strong_password

# AUTH password for the replica instance
requirepass a_strong_password

karuppiahn-a01:3.2 karuppiahn$ redis-server replica.conf
23024:C 06 Aug 2021 15:38:35.177 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
23024:C 06 Aug 2021 15:38:35.177 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=23024, just started
23024:C 06 Aug 2021 15:38:35.177 # Configuration loaded
23024:S 06 Aug 2021 15:38:35.178 * Increased maximum number of open files to 10032 (it was originally set to 2560).
23024:S 06 Aug 2021 15:38:35.178 * monotonic clock: POSIX clock_gettime
                _._
           _.-``__ ''-._
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 23024
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

23024:S 06 Aug 2021 15:38:35.179 # Server initialized
23024:S 06 Aug 2021 15:38:35.179 * Ready to accept connections
23024:S 06 Aug 2021 15:38:35.180 * Connecting to MASTER 127.0.0.1:6379
23024:S 06 Aug 2021 15:38:35.180 * MASTER <-> REPLICA sync started
23024:S 06 Aug 2021 15:38:35.180 * Non blocking connect for SYNC fired the event.
23024:S 06 Aug 2021 15:38:35.180 * Master replied to PING, replication can continue...
23024:S 06 Aug 2021 15:38:35.180 * Partial resynchronization not possible (no cached master)
23024:S 06 Aug 2021 15:38:35.181 * Full resync from master: fc0057728f174be2eb3eb313dffcf54e3b0a4fd2:0
23024:S 06 Aug 2021 15:38:35.239 * MASTER <-> REPLICA sync: receiving 175 bytes from master to disk
23024:S 06 Aug 2021 15:38:35.239 * MASTER <-> REPLICA sync: Flushing old data
23024:S 06 Aug 2021 15:38:35.239 * MASTER <-> REPLICA sync: Loading DB in memory
23024:S 06 Aug 2021 15:38:35.240 * Loading RDB produced by version 6.2.5
23024:S 06 Aug 2021 15:38:35.240 * RDB age 0 seconds
23024:S 06 Aug 2021 15:38:35.240 * RDB memory usage when created 2.06 Mb
23024:S 06 Aug 2021 15:38:35.240 * MASTER <-> REPLICA sync: Finished with success
```

CLI connected to Primary Server

```bash
karuppiahn-a01:3.2 karuppiahn$ redis-cli
127.0.0.1:6379> keys *
(error) NOAUTH Authentication required.
127.0.0.1:6379> AUTH a_strong_password
OK
127.0.0.1:6379> keys *
(empty array)
127.0.0.1:6379> SET foo bar
OK
127.0.0.1:6379>
```

CLI connected to Replica Server

```bash
karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6380
127.0.0.1:6380> keys *
(error) NOAUTH Authentication required.
127.0.0.1:6380> AUTH a_strong_password
OK
127.0.0.1:6380> keys *
(empty array)
127.0.0.1:6380> MONITOR
OK
1628244587.497337 [0 127.0.0.1:6379] "ping"
1628244588.749726 [0 127.0.0.1:6379] "SELECT" "0"
1628244588.749745 [0 127.0.0.1:6379] "SET" "foo" "bar"
1628244597.770320 [0 127.0.0.1:6379] "ping"
1628244607.990974 [0 127.0.0.1:6379] "ping"
1628244618.325424 [0 127.0.0.1:6379] "ping"
1628244628.602624 [0 127.0.0.1:6379] "ping"
1628244638.822113 [0 127.0.0.1:6379] "ping"
1628244649.066471 [0 127.0.0.1:6379] "ping"
1628244659.311005 [0 127.0.0.1:6379] "ping"
1628244669.555879 [0 127.0.0.1:6379] "ping"
1628244679.774088 [0 127.0.0.1:6379] "ping"
1628244690.012922 [0 127.0.0.1:6379] "ping"
1628244700.279124 [0 127.0.0.1:6379] "ping"
1628244710.530603 [0 127.0.0.1:6379] "ping"
1628244720.772291 [0 127.0.0.1:6379] "ping"
```

Interesting to see the cool `MONITOR` command. Previously I didn't know what it does and it simply gave `OK` I think and I never understood it. Now I do. I guess I should have just read the redis docs for the command

https://redis.io/commands/monitor

It seems not all commands are logged by the `MONITOR` command

https://redis.io/commands/monitor#commands-not-logged-by-monitor

And of course it looks like it comes at a cost. I always hear this about debugging modes / debugging stuff, at least that's my experience, specifically with Redis

https://redis.io/commands/monitor#cost-of-running-monitor

I noticed an interesting command called `HELLO`

https://redis.io/commands/hello

In primary server CLI it's output looked like this

```
127.0.0.1:6379> HELLO
 1) "server"
 2) "redis"
 3) "version"
 4) "6.2.5"
 5) "proto"
 6) (integer) 2
 7) "id"
 8) (integer) 4
 9) "mode"
10) "standalone"
11) "role"
12) "master"
13) "modules"
14) (empty array)
127.0.0.1:6379>
```

Looks like the primary server sends a lot of ping `PING` commands to the replica to check the replica's health

```bash
karuppiahn-a01:3.2 karuppiahn$ redis-cli -p 6380
127.0.0.1:6380> keys *
(error) NOAUTH Authentication required.
127.0.0.1:6380> AUTH a_strong_password
OK
127.0.0.1:6380> keys *
(empty array)
127.0.0.1:6380> MONITOR
OK
1628244587.497337 [0 127.0.0.1:6379] "ping"
1628244588.749726 [0 127.0.0.1:6379] "SELECT" "0"
1628244588.749745 [0 127.0.0.1:6379] "SET" "foo" "bar"
1628244597.770320 [0 127.0.0.1:6379] "ping"
1628244607.990974 [0 127.0.0.1:6379] "ping"
1628244618.325424 [0 127.0.0.1:6379] "ping"
1628244628.602624 [0 127.0.0.1:6379] "ping"
1628244638.822113 [0 127.0.0.1:6379] "ping"
1628244649.066471 [0 127.0.0.1:6379] "ping"
1628244659.311005 [0 127.0.0.1:6379] "ping"
1628244669.555879 [0 127.0.0.1:6379] "ping"
1628244679.774088 [0 127.0.0.1:6379] "ping"
1628244690.012922 [0 127.0.0.1:6379] "ping"
1628244700.279124 [0 127.0.0.1:6379] "ping"
1628244710.530603 [0 127.0.0.1:6379] "ping"
1628244720.772291 [0 127.0.0.1:6379] "ping"
1628244731.000638 [0 127.0.0.1:6379] "ping"
1628244741.261418 [0 127.0.0.1:6379] "ping"
1628244751.503620 [0 127.0.0.1:6379] "ping"
1628244761.762126 [0 127.0.0.1:6379] "ping"
1628244772.008404 [0 127.0.0.1:6379] "ping"
1628244782.261176 [0 127.0.0.1:6379] "ping"
1628244792.544273 [0 127.0.0.1:6379] "ping"
1628244802.859767 [0 127.0.0.1:6379] "ping"
1628244813.160848 [0 127.0.0.1:6379] "ping"
1628244823.521182 [0 127.0.0.1:6379] "ping"
1628244833.748019 [0 127.0.0.1:6379] "ping"
1628244843.980255 [0 127.0.0.1:6379] "ping"
1628244854.204261 [0 127.0.0.1:6379] "ping"
1628244864.461197 [0 127.0.0.1:6379] "ping"
1628244874.771124 [0 127.0.0.1:6379] "ping"
1628244885.169562 [0 127.0.0.1:6379] "ping"
1628244895.465584 [0 127.0.0.1:6379] "ping"
1628244905.726207 [0 127.0.0.1:6379] "ping"
1628244915.961821 [0 127.0.0.1:6379] "ping"
1628244926.215558 [0 127.0.0.1:6379] "ping"
1628244936.498430 [0 127.0.0.1:6379] "ping"
1628244946.858004 [0 127.0.0.1:6379] "ping"
1628244957.112669 [0 127.0.0.1:6379] "ping"
1628244967.416021 [0 127.0.0.1:6379] "ping"
1628244977.625968 [0 127.0.0.1:6379] "ping"
1628244987.919665 [0 127.0.0.1:6379] "ping"
1628244998.158272 [0 127.0.0.1:6379] "ping"
1628245008.407778 [0 127.0.0.1:6379] "ping"
1628245018.618130 [0 127.0.0.1:6379] "ping"
1628245028.854773 [0 127.0.0.1:6379] "ping"
1628245039.094933 [0 127.0.0.1:6379] "ping"
1628245049.348538 [0 127.0.0.1:6379] "ping"
1628245059.562401 [0 127.0.0.1:6379] "ping"
1628245069.834051 [0 127.0.0.1:6379] "ping"
1628245080.093614 [0 127.0.0.1:6379] "ping"
1628245090.300899 [0 127.0.0.1:6379] "ping"
1628245100.550010 [0 127.0.0.1:6379] "ping"
1628245110.763597 [0 127.0.0.1:6379] "ping"
1628245121.061017 [0 127.0.0.1:6379] "ping"
^C
karuppiahn-a01:3.2 karuppiahn$
```
