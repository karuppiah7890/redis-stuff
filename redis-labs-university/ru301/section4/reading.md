Found two Redis Cluster topics under 

https://redis.io/documentation [TODO]

https://redis.io/topics/cluster-tutorial [TODO]

https://redis.io/topics/cluster-spec [TODO]

---

Questions [TODO]
- What's consistent hashing? I have heard of it in the context of sharding
- Why does hashslots help in the case of redis?

---

I was reading https://redis.io/topics/cluster-spec

I read and skimmed through - https://redis.io/topics/cluster-spec#redis-cluster-goals , https://redis.io/topics/cluster-spec#implemented-subset , https://redis.io/topics/cluster-spec#clients-and-servers-roles-in-the-redis-cluster-protocol , https://redis.io/topics/cluster-spec#write-safety

It was interesting to see some stuff

Looks like Redis Cluster is a totally different beast. It's not exactly anything like standalone redis / redis HA

I mean, whatever works in standalone Redis may not work in Redis Cluster. But looks like many things have been implemented still, looking at https://redis.io/topics/cluster-spec#implemented-subset . Gotta check how operations like UNION work on sets when it's done on keys across shards. I think it won't work, looking at the docs :P

I need to checkout hash tags at some point [TODO] I think I did hear about it in this one talk - https://www.youtube.com/watch?v=LLxWu27qQTI

I realized why I didn't notice PINGs from other primary shards when I was running `MONITOR` in one of the shards. Apparently Redis Cluster uses a "TCP bus and a binary protocol, called the Redis Cluster Bus" [TODO] Not sure how to look at the pings that are sent among the shards. I mean, it's not Redis protocol I guess, not the standalone one. Hmm. Maybe in observability it may come up ;)

Redis Cluster seems to do a lot of things
- Store the data of the client
- Stores the cluster information / state - I guess stuff like the nodes present in the cluster?
- Mapping keys to nodes - I guess it's more of mapping hash slots to nodes, and for finding hash slot from key, node just needs to run CRC16 and do some calculation. So, keys -> hash slot -> node / shard
- Auto discover other nodes - through existing nodes I guess?
- Detect non-working / not-working / failed nodes - by monitoring / sending pings I guess?
- Promote slaves to master - failover stuff

I was reading https://redis.io/topics/cluster-spec#availability and a few things went a little over my head. I couldn't get the math about the probability

I need to start creating a visualization for all the scenarios I'm checking out for Redis HA and Redis Cluster, to understand what all they are saying! :) [TODO]

Looking at https://redis.io/topics/cluster-spec#availability , looks like there's a thing called replicas migration in Redis Cluster. Interesting thing. Looks like the replica of one shard can suddenly be changed to a replica of another shard, hmm. I'm assuming this can be done when one primary shard has more than one replica shard, and another primary shard has 0 replica shards. Primary shards which have 0 replica shards are called as orphaned primaries / orphaned masters according to the doc. So, move a replica shard pointing to (/replicating from) a primary shard that has too many (more than 1) replica shards to a primary shard that has no (0) replica shards. I wonder how they do that, hmm. There's probably some redis-cli command for it ;)

```bash
redis-stuff $ redis-cli --cluster help
Cluster Manager Commands:
  create         host1:port1 ... hostN:portN
                 --cluster-replicas <arg>
  check          host:port
                 --cluster-search-multiple-owners
  info           host:port
  fix            host:port
                 --cluster-search-multiple-owners
                 --cluster-fix-with-unreachable-masters
  reshard        host:port
                 --cluster-from <arg>
                 --cluster-to <arg>
                 --cluster-slots <arg>
                 --cluster-yes
                 --cluster-timeout <arg>
                 --cluster-pipeline <arg>
                 --cluster-replace
  rebalance      host:port
                 --cluster-weight <node1=w1...nodeN=wN>
                 --cluster-use-empty-masters
                 --cluster-timeout <arg>
                 --cluster-simulate
                 --cluster-pipeline <arg>
                 --cluster-threshold <arg>
                 --cluster-replace
  add-node       new_host:new_port existing_host:existing_port
                 --cluster-slave
                 --cluster-master-id <arg>
  del-node       host:port node_id
  call           host:port command arg arg .. arg
                 --cluster-only-masters
                 --cluster-only-replicas
  set-timeout    host:port milliseconds
  import         host:port
                 --cluster-from <arg>
                 --cluster-from-user <arg>
                 --cluster-from-pass <arg>
                 --cluster-from-askpass
                 --cluster-copy
                 --cluster-replace
  backup         host:port backup_directory
  help           

For check, fix, reshard, del-node, set-timeout you can specify the host and port of any working node in the cluster.

Cluster Manager Options:
  --cluster-yes  Automatic yes to cluster commands prompts

redis-stuff $ 
```

There IS something called `rebalance`. I don't know what it does, hmm. Anyways, let's move on to the next section for now ;)

Next is https://redis.io/topics/cluster-spec#performance
