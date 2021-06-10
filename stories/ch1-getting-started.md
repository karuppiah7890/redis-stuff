# Chapter 1 : Getting Started

I'm checking out redis just for fun. I tried it out long ago at work and in my
personal time. I think it has come a long way now. Last I worked with it, the
version was v5. Now there's v6

https://redis.io/

I also plan to maybe try my hand at creating a managed redis solution, an open
source one :D ;) Let's see how that goes! :)

Let me start by trying out the latest redis in my local!

https://redis.io/download

I might try the unstable redis later I guess. Or...maybe now? Hmm. Yeah, why not

https://github.com/redis/redis/archive/unstable.tar.gz

Looks like that was source code. I'll build that later. I guess I can use the
stable versions. I'll try both the tar ball and the docker image

https://download.redis.io/releases/redis-6.2.1.tar.gz

https://raw.githubusercontent.com/redis/redis/6.2/00-RELEASENOTES

https://hub.docker.com/_/redis/

Also, I got `redis` from `brew`. I already had it, I just had to upgrade it

```bash
$ brew upgrade redis
```

```bash
$ redis-cli --version
redis-cli 6.2.1

$ redis-server --version
Redis server v=6.2.1 sha=00000000:0 malloc=libc bits=64 build=cfaa1431404ef25b
```

There seem to be many redis related binaries

```bash
$ fd redis /usr/local/bin
/usr/local/bin/redis-benchmark
/usr/local/bin/redis-check-aof
/usr/local/bin/redis-check-rdb
/usr/local/bin/redis-cli
/usr/local/bin/redis-sentinel
/usr/local/bin/redis-server
```

I intend to explore them all ! :D

Now I'm running the redis server

```bash
$ redis-server 
29695:C 02 Apr 2021 17:04:40.234 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
29695:C 02 Apr 2021 17:04:40.234 # Redis version=6.2.1, bits=64, commit=00000000, modified=0, pid=29695, just started
29695:C 02 Apr 2021 17:04:40.234 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
29695:M 02 Apr 2021 17:04:40.235 * Increased maximum number of open files to 10032 (it was originally set to 256).
29695:M 02 Apr 2021 17:04:40.235 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.1 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 29695
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

29695:M 02 Apr 2021 17:04:40.236 # Server initialized
29695:M 02 Apr 2021 17:04:40.236 * Ready to accept connections
```

And the client

```bash
$ redis-cli 
127.0.0.1:6379> set foo bar
OK
127.0.0.1:6379> get food
(nil)
127.0.0.1:6379> get foo
"bar"
127.0.0.1:6379> 
```

After this I was able to shut down the server and was able to run it again and
still see the same data as the data was saved in a dump.rdb file

The shutdown looks like this -

```bash
$ redis-server 
32934:C 03 Apr 2021 14:58:01.695 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
32934:C 03 Apr 2021 14:58:01.695 # Redis version=6.2.1, bits=64, commit=00000000, modified=0, pid=32934, just started
32934:C 03 Apr 2021 14:58:01.695 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
32934:M 03 Apr 2021 14:58:01.697 * Increased maximum number of open files to 10032 (it was originally set to 256).
32934:M 03 Apr 2021 14:58:01.697 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.1 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 32934
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

32934:M 03 Apr 2021 14:58:01.702 # Server initialized
32934:M 03 Apr 2021 14:58:01.704 * Loading RDB produced by version 6.2.1
32934:M 03 Apr 2021 14:58:01.704 * RDB age 73769 seconds
32934:M 03 Apr 2021 14:58:01.704 * RDB memory usage when created 0.98 Mb
32934:M 03 Apr 2021 14:58:01.704 * DB loaded from disk: 0.001 seconds
32934:M 03 Apr 2021 14:58:01.704 * Ready to accept connections
^C32934:signal-handler (1617442107) Received SIGINT scheduling shutdown...
32934:M 03 Apr 2021 14:58:27.465 # User requested shutdown...
32934:M 03 Apr 2021 14:58:27.465 * Saving the final RDB snapshot before exiting.
32934:M 03 Apr 2021 14:58:27.473 * DB saved on disk
32934:M 03 Apr 2021 14:58:27.473 # Redis is now ready to exit, bye bye...
```

Notice how it shows that it's saving the final RDB snapshot before exiting and
shows that the DB is saved on disk

Now, let's move on to explore the different binaries. I'll check the different
features of the different data structures a bit later.
