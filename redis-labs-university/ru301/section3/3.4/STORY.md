
```bash
$ touch sentinel1.conf
$ vi sentinel1.conf
$ cat sentinel1.conf
port 5000
sentinel monitor myprimary 127.0.0.1 6379 2
sentinel down-after-milliseconds myprimary 5000
sentinel failover-timeout myprimary 60000
sentinel auth-pass myprimary a_strong_password
```

Most of the things are already done as part of 3.2, so, skipping. It was done as part of reading sentinel docs - https://redis.io/topics/sentinel#a-quick-tutorial
