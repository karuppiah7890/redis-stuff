Interesting homework questions! I think I need to read some stuff before answering them.

I just answered one for now

`Why might you implement sharding of a Redis database?`

Even that was tricky because there was a tricky option! I mentioned about the tricky option in the discord channel like this -

In Section 4 Homework 4.1, in question `Why might you implement sharding of a Redis database?`, there's a tricky option `To allow parallel, multi-threaded writes to a normally single-threaded service` . Open Source Redis is single threaded, yes, and if we use sharding we do get multi threaded writes across servers / machines, one thread in each server / machine, and it can also be parallel. The option could at least put an extra word saying `To allow parallel, multi-threaded writes to a normally single-threaded service in a single machine` or something like that, or else it's a bit of an ambiguous option. Or maybe I'm missing something and understood something wrong, in which case I would like to understand the right explanation. Thanks in advance!

The answer to the question is - `To scale horizontally by splitting data across multiple servers `

---

Other questions -

`When is failover initiated in a Redis Cluster?`

Interesting options for answers!

- When a primary shard reports a failure to its replicas.
- When enough shards report that a given primary shard is not responding.
- When a primary shard falls out of sync with the other primary shards in the Cluster
- When the number of keys in the primary shards exceed 16,384, the number of slots in a hashslot 

I need to read more but just from the video I saw, and basic knowledge, I was wondering how `When a primary shard reports a failure to its replicas.` is just crazy, because how will a primary shard report a failure? And whose failure will it report? It's own? Some other process's failure? Another primary / replica? Why to the replica?

Also, if the primary shard goes down - process dies, how will it even report? So, that doesn't make sense even if this is talking about reporting "pings" though, PING is actually done by clients or other processes to a system, so, it's more like other processes send PING command to a system to check if it's up and running, something like a readiness / liveness probe (copying the term from Kubernetes :P), or just a probe / health endpoint maybe?

What about the other options? 

`When enough shards report that a given primary shard is not responding.` makes sense, I mean, other shards, the primaries (primary shards) monitor and notice that a given shard is not responding, then, well, it makes sense to think that the shard is down and hence do a failover

I was just trying to see if a shard gets `PING` commands from other shards using `MONITOR` command. But I don't see anything of that sort

```bash
$ redis-cli -p 7000
127.0.0.1:7000> MONITOR
OK
```

I mean, previously I have seen replicas where the `MONITOR` in replica showed PING commands from the primary / master Redis in the Redis HA setup. I'm wondering what happens in a cluster setup, hmm. No PINGs here, as of now

`When a primary shard falls out of sync with the other primary shards in the Cluster`, for a moment I was thinking what this meant, but later I realized that this is a crazy option. I mean, how can a primary shard fall out of sync with other primary shards? Sync happens only in a primary - replica setup, in a HA setup etc. How can sync happen among primary shards? Sync can happen among primary shard and it's corresponding replica shards, that's it

Primary shards are meant to have separate kinds of data - keys and corresponding values. They can't be in sync ever, so how can it even fall out of sync if it was never in sync, can't be in sync and can never be in sync? As it's not supposed to be in sync!

`When the number of keys in the primary shards exceed 16,384, the number of slots in a hashslot` - I'm wondering what this option is. I just realized this is another crazy option, haha. It's talking about number of keys in the primary shards - oh, all primary shards, and if that exceeds 16,384, which is the total number of hashslots, but this option says it's the number of slots in A hashslot. Pretty confusing option. Relating so many unrelated things. Hmm. Interesting confusing meh option. If Redis can't handle 16,384 keys, haha. Especially Redis cluster. Haha. Anyways, another meh option

I think I'll read more still before answering, but I think the most sensible and correct option is most probably `When enough shards report that a given primary shard is not responding.`

Also, I was just thinking about the `sync` option, it's assuming that sync is about synchronizing data, I don't know if it's talking about synchronizing metadata or any other meta stuff like configuration etc, going out of sync for that data due to some reason like network issues / network partition etc. But I don't think it's talking about all that. It's still a very very vaguely defined option I guess, hmm

---

`Why would you use hashslots instead of solely algorithmic sharding when scaling a Redis deployment?`

I remember listening to the Redis Cluster video talk about this. But I forgot. Hmm. I'm gonna go read more about this hashslot stuff and how it helps etc, and the pros and cons ;) :D :)

---

`How can we configure a Redis cluster to avoid a split-brain scenario?`

This was also mentioned in the Redis Cluster video

---

I think reading https://redis.io/topics/cluster-spec can help a lot! :D Especially to under Redis cluster and also answer the above questions with more ease and a lot better understanding :)

I was half way reading through the cluster spec. I still cam back and checked the videos and answered the questions

But I still need to learn the crux of it as I'm not able to intuitively understand the following

- Hashslots and consistent hashing relationship - ? I read about consistent hashing and it felt like there's a slight relationship. Or maybe there's none. I was just trying to understand in what ways hashslot helps. I understood to some extent that - while resharding we don't have to rehash a lot of keys like in the case of algorithm sharding where we use simple hash(key) mod N where N is the number of Redis shards, which can change during resharding - addition or removal of shards. Usually I think resharding would be addition, to scale up. And in case of hashslots, he N value becomes 16384, which is 2^14 actually, just saying. And whatever is the result of hash(key) mod 16384, it will be a value less than 16384, and it will be a hashslot number and it will be associated with a shard, with a mapping, that the cluster will remember. When resharding happens, the hash(key) mod 16834 still happens, but the mapping of hashslots to shards is changed - when adding new shards, some hashslots from existing shard / shards are moved to the new shard, of course along with the data (key and value) corresponding to that hashslot. Every key would be associated with a hashslot.

The only thing is, 16384 is the max number of shards we can have as we can't share the 16834 hashslots to more than 16384 shards. The hash(key) mod 16384 is always an integer value less than 16384 and it will just be one hashslot, and no decimal, so we can give a minimum of one hashslot to each shard when trying to create the biggest open source redis cluster, with 16384 primary shards

---

Split brain situation - I still didn't get how having odd number of primaries and two replicas per primary can help. That's what the video said though, and the Homework answer is that too. Not much reasoning in it though

The Homework "Show answer" did say

```
To prevent split-brain situations in Redis Cluster, always keep an odd number of shards in your cluster. If a network split should occur, a group of connected shards will do a count and see if they are in the bigger or the smaller fractioned group (also called majority or minority). If they are in the minority, they will not try to trigger a failover and will not accept any client write requests.
```

It says that if a partition is in a minority, it will NOT trigger a failover and will not accept any client write requests, hmm. I'm wondering how

I did try to get this math done in pen and paper

One thing about odd number of primary shards and two replicas for each primary shard is this -

Np = Number of Primary shards

Nr = Number of Replica shards

Total shards = Np + Nr

Nr = Number of Replica shards

and we know each primary has to have two replicas, so

Nr = 2 * Np

So

Total shards = Np + 2 * Np = 3 * Np

And we also know that Np is odd as we will have to have an odd number of primary shards

So, Total shards = 3 * odd number = which is again an odd number I believe

So, total shards is an odd number, that's all I have got to think about for now

When thinking about split brain situation, I was thinking about how there can be so many split brain situations

For example, for 3 primary shards and 6 replica shards (2 replica shards for each primary), then

Primary shards = P1, P2, P3
Replica shards = R1a, R1b, R2a, R2b, R3a, R3b

R1a and R1b are replicas of P1 primary shard and so on

Now, if we have two buckets or two parts of the brain - left and right, we can put the above 9 shards in so many ways in the two parts of the brain. I'm wondering what happens in each of those situations, hmm

And I'm wondering about configuration and default configuration behaviour and also non-configurable behavior etc, regarding the majority and mintority parts in a split brain situation, hmm


