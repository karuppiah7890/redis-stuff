I need to learn what's CRC16 / crc16 [TODO]

It's an interesting section. It talks about how Redis client libraries could do some stuff and how some good Redis client libraries follow that stuff, while others do not / may not

For example, relying on `MOVED` redirection isn't a great thing as that can slow down the access to the database because we might have to make two requests - one to one random shard and then if it doesn't have the key, it will give a `MOVED` error and then we will have to send another request to the right shard mentioned in the `MOVED` error. Since it's two requests possibly for a single key, what happens is, there's twice the latency or so. Basically more latency

An interesting optimization talks about how the Redis client library can cache the hashslot and shard information, for connecting to the right shard given a hashslot, and the client library can find the hashslot by doing whatever Redis does - CRC16 and using the value of the total number of hashslots which is 16384 and doing the calculation to find out which hashslot the key falls under or is associated to and then find the shard from the cache

Of course if there's a cache there could be cache inconsistency / invalid cache. In this case that's possible as Redis cluster topology can change - what if someone adds or removes shards? And changes the hashslot allocation? The client's cache then becomes invalid. No problem I guess, because the cache will get `MOVED` error and that's how it knows that it's cache is invalid and can cache again by getting latest information from a shard

I guess it's pretty cool

I could look for libraries that don't support Redis Cluster and see if I can help ;) That could be a cool way to learn Redis Cluster client side stuff ;) Or I could still simply write a client library on my own :D [TODO] [IDEA]

I can see some examples of client libraries that already support Redis Cluster - meaning they are cluster aware, and I'm guessing they also have caching support for better speed

- Java: Jedis, Lettuce
- .NET: StackExchange.Redis
- Go: Radix, go-redis/redis
- Node.js: ioredis
- Python: redis-py

Full big list of client libraries of course is here - https://redis.io/clients


