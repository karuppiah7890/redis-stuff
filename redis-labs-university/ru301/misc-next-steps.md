# Misc Next Steps

Read about Kernel level and other low level stuff related to Networking

- Round Trip Time (RTT) and relation to Latency and Pipelining that I read an overview about
- Linux fsync
- Linux file descriptors and how it relates to Redis
    - Linux Kernel settings for file descriptors
    - Excerpt -

```
File descriptor limits

If you do not set the correct number of file descriptors for the Redis user, you will see errors indicating that “Redis can’t set maximum open files..” You can increase the file descriptor limit at the OS level.

Here's an example on Ubuntu using systemd:

/etc/systemd/system/redis.service
[Service] 
... 
User=redis 
Group=redis 
...
LimitNOFILE=65536 
...

You will then need to reload the daemon and restart the redis service.
```

- Linux file I/O
- Linux `listen` call TCP backlog argument - `listen(int s, int backlog)`, the second parameter `backlog` that is, and how it relates to Redis which uses `listen` too. Excerpt -

```
The Redis server uses the value of tcp-backlog to specify the size of the complete connection queue.

Redis passes this configuration as the second parameter of the listen(int s, int backlog) call.

If you have many connections, you will need to set this higher than the default of 511. You can update this in Redis config file:


# TCP listen() backlog. 
# 
# In high requests-per-second environments you need an high backlog in order 
# to avoid slow clients connections issues. Note that the Linux kernel 
# will silently truncate it to the value of /proc/sys/net/core/somaxconn so 
# make sure to raise both the value of somaxconn and tcp_max_syn_backlog 
# in order to get the desired effect.
tcp-backlog 65536


As the comment in redis.conf indicates, the value of somaxconn and tcp_max_syn_backlog may need to be increased at the OS level as well.
```

- Linux `/proc/sys/net/core/somaxconn` , `somaxconn`
- Linux `tcp_max_syn_backlog`
- Linux `/sys/kernel/mm/transparent_hugepage/enabled` and how it relates to Redis. Excerpt -

```
Kernel memory

Under high load, occasional performance dips can occur due to memory allocation. This is something Salvatore, the creator of Redis, blogged about in the past. The performance issue is related to transparent hugepages, which you can disable at the OS level if needed.

$ echo 'never' > /sys/kernel/mm/transparent_hugepage/enabled
```

- Linux Network Kernel Parameters and how it relates to Redis. Excerpt -

```
Kernel network stack

If you plan on handling a large number of connections in a high performance environment, we recommend tuning the following kernel parameters:

vm.swappiness=0                       # turn off swapping
net.ipv4.tcp_sack=1                   # enable selective acknowledgements
net.ipv4.tcp_timestamps=1             # needed for selective acknowledgements
net.ipv4.tcp_window_scaling=1         # scale the network window
net.ipv4.tcp_congestion_control=cubic # better congestion algorithm
net.ipv4.tcp_syncookies=1             # enable syn cookies
net.ipv4.tcp_tw_recycle=1             # recycle sockets quickly
net.ipv4.tcp_max_syn_backlog=NUMBER   # backlog setting
net.core.somaxconn=NUMBER             # up the number of connections per port
net.core.rmem_max=NUMBER              # up the receive buffer size
net.core.wmem_max=NUMBER              # up the buffer size for all connections
```

- Linux RPS - Receive Packet Steering and how it relates to Redis. Excerpt -

```
Enabling RPS (Receive Packet Steering) and CPU preferences

One way we can improve performance is to prevent Redis from running on the same CPUs as those handling any network traffic. This can be accomplished by enabling RPS for our network interfaces and creating some CPU affinity for our Redis process.

Here is an example. First we can enable RPS on CPUs 0-1:

$ echo '3' > /sys/class/net/eth1/queues/rx-0/rps_cpus

Then we can set the CPU affinity for redis to CPUs 2-8:

# config is set to write pid to /var/run/redis.pid
$ taskset -pc 2-8 `cat /var/run/redis.pid`
pid 8946's current affinity list: 0-8
pid 8946's new affinity list: 2-8
```
