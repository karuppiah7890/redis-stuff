I was just checking out the homework for Section 5

It was interesting to recall some latency monitoring stuff and I recalled well. The options used exact wording that I remember seeing in the learning section

```markdown
Redis' Latency Monitoring feature allows you to investigate latency issues. Which of the following components make up the Latency Monitor?
Pick one or more answers
- [X] Latency hooks that sample different latency sensitive code paths.
- [ ] A modified Redis Stream data type that can store latency spikes split by different events.
- [X] A reporting engine to fetch raw data from the time series.
- [X] Analysis engine to provide human readable reports and hints according to the measurements.

Explanation

Redis has a feature called Latency Monitoring which allows you to dig into possible latency issues. Latency monitoring is composed of the following conceptual parts:

- Latency hooks that sample different latency sensitive code paths.
- Time series recording of latency spikes split by different events.
- A reporting engine to fetch raw data from the time series.
- Analysis engine to provide human readable reports and hints according to the measurements.
```

---

I just learned what `keyspace_hits` and `keyspace_misses` is about

```
keyspace_hits: Number of successful lookup of keys in the main dictionary
keyspace_misses: Number of failed lookup of keys in the main dictionary
```

Found it defined here https://redis.io/commands/info :)

```bash
5.3 $ redis-cli info stats | grep keyspace
keyspace_hits:0
keyspace_misses:0
5.3 $ redis-cli info stats | grep keyspace
keyspace_hits:0
keyspace_misses:0
5.3 $ redis-cli info stats | grep keyspace
keyspace_hits:1
keyspace_misses:0
5.3 $ redis-cli info stats | grep keyspace
keyspace_hits:1
keyspace_misses:1
5.3 $ redis-cli info stats | grep keyspace
keyspace_hits:1
keyspace_misses:2
5.3 $ redis-cli info stats | grep keyspace
keyspace_hits:3
keyspace_misses:2
5.3 $ 
```

```bash
redis-stuff $ redis-cli
127.0.0.1:6379> get blah
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> get bloo
(nil)
127.0.0.1:6379> get bloo
(nil)
127.0.0.1:6379> type blah
set
127.0.0.1:6379> scard blah
(integer) 7
127.0.0.1:6379> 
```

The current question is about using Redis as a cache

"When using Redis as a cache, which INFO command can be used to work out the cache hit to miss ratio?"

I think we have to use `INFO stats` and grep for `keyspace`, basically - `$ redis-cli INFO stats | grep keyspace`

because, for cache, the hit and miss ratio would be about how many times the cache was accessed and the data that one was looking for was present and how many times the data wasn't present, which is the same defintion of `keyspace_hits` and `keyspace_misses` as they talk about `lookup hit` and `lookup miss`

The only weird thing is, even `get blah` is counted as a hit, weird thing, though `get blah` returned error as it's not a valid operation

Also, not sure what the `main dictionary` in the definition is supposed to mean. I mean, what's the `main` in it is what I'm wondering, gotta check [TODO]

I did notice the keyspace thingy before too, but it didn't talk much about details, the previous section (5.1 section) said

```
Some of the data returned by INFO are going to be static.  For example the Redis version which won't change until an update is made.  Other data is dynamic, for example keyspace_hits ÷ keyspace_misses. The latter could be taken to compute a hit ratio and observed as a long term metric
```

Anyways, now it's more clear as to what it's doing


