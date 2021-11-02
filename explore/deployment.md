
If I deploy a Redis myself or get a DBaaS service to deploy Redis for me, I think I would ask the following questions

- Does my Redis use jemalloc or libc as memory allocator? As I hear jemalloc is pretty good
- Does my Redis have authentication (basic requirepass) and authorization (ACL with different passwords for each user and access control for each user) enabled?
- What network interfaces does the Redis server bind to and if all of them are necessary or some of them are unnecessary?
- Does my Redis have SSL/TLS support? Where all communication to and from the Redis server is encrypted
- Does my Redis have firewall to secure the Redis to only open necessary ports? Redis specific ports, maybe SSH ports
- If SSH is enabled and SSH port is accessible in my Redis server, how secure is it? Is SSH guard enabled? And what crypto keys are being used for the authentication? RSA? ED25519? DSA? ECDSA? How big (bits) are the keys? 2048? 4096? Something else?
- What's the latency of using the Redis instance?
- What's the throughput on the number of operations per second for my Redis?

While deploying, I would think about the following configurations to provide
- Is my Redis gonna run as a cache (not persistent) / data store (persistent)?
- What's the max memory eviction policy of my Redis?
