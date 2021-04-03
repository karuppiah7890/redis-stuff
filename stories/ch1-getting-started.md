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
