# CRC16

CRC16 in the context of Redis Cluster

https://en.wikipedia.org/wiki/Cyclic_redundancy_check

CRC stands for Cyclic Redundancy Check

There are many CRC-16 I guess, looking at https://en.wikipedia.org/wiki/Cyclic_redundancy_check

From the Appendix in Redis docs about Redis Cluster, https://redis.io/topics/cluster-spec#appendix-a-crc16-reference-implementation-in-ansi-c , looks like CRC-16 refers to CRC-16-CCITT in https://en.wikipedia.org/wiki/Cyclic_redundancy_check 

Let's look at what this CRC and CRC16 means and how it's calculated in terms of math and computer science

I just read some stuff and a calculation

https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Computation

https://en.wikipedia.org/wiki/Cyclic_redundancy_check#Specification

We are looking for "Normal" CRC representation which is mentioned as `0x1021` for `CRC-16-CCITT`
