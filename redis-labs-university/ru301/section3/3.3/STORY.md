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
