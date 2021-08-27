I reading the 5.3 section content and checking out some new commands mentioned. For example SLOWLOG

https://redis.io/commands/slowlog

And config parameters `slowlog-log-slower-than` and `slowlog-max-len`

It's interesting to see what all the SLOWLOG command and internal slowlog feature provides!

I might try it sometime. Maybe even now! Hmm

```bash
Last login: Fri Aug 27 20:39:18 on ttys000
reredis-stuff $ redis-cli
127.0.0.1:6379> CONFIG GET slowlog-log-slower-than
1) "slowlog-log-slower-than"
2) "10000"
127.0.0.1:6379> CONFIG SET slowlog-log-slower-than 0
OK
127.0.0.1:6379> SLOWLOG len
(integer) 1
127.0.0.1:6379> SLOWLOG len
(integer) 2
127.0.0.1:6379> SLOWLOG len
(integer) 3
127.0.0.1:6379> SLOWLOG len
(integer) 4
127.0.0.1:6379> SLOWLOG get
1) 1) (integer) 4
   2) (integer) 1630080116
   3) (integer) 1
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
2) 1) (integer) 3
   2) (integer) 1630080115
   3) (integer) 1
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
3) 1) (integer) 2
   2) (integer) 1630080115
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
4) 1) (integer) 1
   2) (integer) 1630080113
   3) (integer) 1
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
5) 1) (integer) 0
   2) (integer) 1630080108
   3) (integer) 28
   4) 1) "CONFIG"
      2) "SET"
      3) "slowlog-log-slower-than"
      4) "0"
   5) "127.0.0.1:55319"
   6) ""
127.0.0.1:6379> SLOWLOG get 1
1) 1) (integer) 5
   2) (integer) 1630080120
   3) (integer) 13
   4) 1) "SLOWLOG"
      2) "get"
   5) "127.0.0.1:55319"
   6) ""
127.0.0.1:6379> SLOWLOG get 2
1) 1) (integer) 6
   2) (integer) 1630080122
   3) (integer) 41
   4) 1) "SLOWLOG"
      2) "get"
      3) "1"
   5) "127.0.0.1:55319"
   6) ""
2) 1) (integer) 5
   2) (integer) 1630080120
   3) (integer) 13
   4) 1) "SLOWLOG"
      2) "get"
   5) "127.0.0.1:55319"
   6) ""
127.0.0.1:6379> SLOWLOG get 2
1) 1) (integer) 7
   2) (integer) 1630080124
   3) (integer) 10
   4) 1) "SLOWLOG"
      2) "get"
      3) "2"
   5) "127.0.0.1:55319"
   6) ""
2) 1) (integer) 6
   2) (integer) 1630080122
   3) (integer) 41
   4) 1) "SLOWLOG"
      2) "get"
      3) "1"
   5) "127.0.0.1:55319"
   6) ""
127.0.0.1:6379> SLOWLOG reset
OK
127.0.0.1:6379> SLOWLOG len
(integer) 1
127.0.0.1:6379> SLOWLOG len
(integer) 2
127.0.0.1:6379> SLOWLOG get
1) 1) (integer) 11
   2) (integer) 1630080139
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
2) 1) (integer) 10
   2) (integer) 1630080137
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
3) 1) (integer) 9
   2) (integer) 1630080135
   3) (integer) 16
   4) 1) "SLOWLOG"
      2) "reset"
   5) "127.0.0.1:55319"
   6) ""
127.0.0.1:6379> 
```

Interesting to see `SLOWLOG` commands themselves getting logged, haha

```bash
127.0.0.1:6379> CLIENT GETNAME
(nil)
127.0.0.1:6379> CLIENT SETNAME 
(error) ERR Unknown subcommand or wrong number of arguments for 'SETNAME'. Try CLIENT HELP.
127.0.0.1:6379> CLIENT SETNAME "karuppiah"
OK
127.0.0.1:6379> SLOWLOG len
(integer) 7
127.0.0.1:6379> SLOWLOG get
1) 1) (integer) 16
   2) (integer) 1630080213
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) "karuppiah"
2) 1) (integer) 15
   2) (integer) 1630080208
   3) (integer) 1
   4) 1) "CLIENT"
      2) "SETNAME"
      3) "karuppiah"
   5) "127.0.0.1:55319"
   6) "karuppiah"
3) 1) (integer) 14
   2) (integer) 1630080205
   3) (integer) 25
   4) 1) "CLIENT"
      2) "SETNAME"
   5) "127.0.0.1:55319"
   6) ""
4) 1) (integer) 13
   2) (integer) 1630080195
   3) (integer) 1
   4) 1) "CLIENT"
      2) "GETNAME"
   5) "127.0.0.1:55319"
   6) ""
5) 1) (integer) 12
   2) (integer) 1630080143
   3) (integer) 11
   4) 1) "SLOWLOG"
      2) "get"
   5) "127.0.0.1:55319"
   6) ""
6) 1) (integer) 11
   2) (integer) 1630080139
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
7) 1) (integer) 10
   2) (integer) 1630080137
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) ""
8) 1) (integer) 9
   2) (integer) 1630080135
   3) (integer) 16
   4) 1) "SLOWLOG"
      2) "reset"
   5) "127.0.0.1:55319"
   6) ""
127.0.0.1:6379> SLOWLOG get 2
1) 1) (integer) 17
   2) (integer) 1630080215
   3) (integer) 23
   4) 1) "SLOWLOG"
      2) "get"
   5) "127.0.0.1:55319"
   6) "karuppiah"
2) 1) (integer) 16
   2) (integer) 1630080213
   3) (integer) 2
   4) 1) "SLOWLOG"
      2) "len"
   5) "127.0.0.1:55319"
   6) "karuppiah"
127.0.0.1:6379> 
```

---

Cool, now, next section is around scanning keys

Big keys analysis

```bash
redis-stuff $ redis-cli --bigkeys

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).


-------- summary -------

Sampled 0 keys in the keyspace!
Total key length in bytes is 0 (avg len 0.00)


0 hashs with 0 fields (00.00% of keys, avg size 0.00)
0 lists with 0 items (00.00% of keys, avg size 0.00)
0 strings with 0 bytes (00.00% of keys, avg size 0.00)
0 streams with 0 entries (00.00% of keys, avg size 0.00)
0 sets with 0 members (00.00% of keys, avg size 0.00)
0 zsets with 0 members (00.00% of keys, avg size 0.00)
redis-stuff $ 
```

Cool, I created some big keys ;)

```bash
127.0.0.1:6379> keys *
1) "blah"
2) "something"
127.0.0.1:6379> LLEN something
(integer) 445
127.0.0.1:6379> SCARD blah
(integer) 7
127.0.0.1:6379> 
redis-stuff $ redis-cli --bigkeys

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Biggest list   found so far '"something"' with 445 items
[00.00%] Biggest set    found so far '"blah"' with 7 members

-------- summary -------

Sampled 2 keys in the keyspace!
Total key length in bytes is 13 (avg len 6.50)

Biggest   list found '"something"' has 445 items
Biggest    set found '"blah"' has 7 members

1 lists with 445 items (50.00% of keys, avg size 445.00)
0 hashs with 0 fields (00.00% of keys, avg size 0.00)
0 strings with 0 bytes (00.00% of keys, avg size 0.00)
0 streams with 0 entries (00.00% of keys, avg size 0.00)
1 sets with 7 members (50.00% of keys, avg size 7.00)
0 zsets with 0 members (00.00% of keys, avg size 0.00)
redis-stuff $ redis-cli --memkeys

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Biggest list   found so far '"something"' with 1029 bytes
[00.00%] Biggest set    found so far '"blah"' with 78 bytes

-------- summary -------

Sampled 2 keys in the keyspace!
Total key length in bytes is 13 (avg len 6.50)

Biggest   list found '"something"' has 1029 bytes
Biggest    set found '"blah"' has 78 bytes

1 lists with 1029 bytes (50.00% of keys, avg size 1029.00)
0 hashs with 0 bytes (00.00% of keys, avg size 0.00)
0 strings with 0 bytes (00.00% of keys, avg size 0.00)
0 streams with 0 bytes (00.00% of keys, avg size 0.00)
1 sets with 78 bytes (50.00% of keys, avg size 78.00)
0 zsets with 0 bytes (00.00% of keys, avg size 0.00)
redis-stuff $ 
```

The commands I ran can be found in slow log using slowlog command ;) :D

```bash
redis-stuff $ redis-cli
127.0.0.1:6379> SLOWLOG get
 1) 1) (integer) 58
    2) (integer) 1630080469
    3) (integer) 691
    4) 1) "COMMAND"
    5) "127.0.0.1:55375"
    6) ""
 2) 1) (integer) 57
    2) (integer) 1630080444
    3) (integer) 0
    4) 1) "MEMORY"
       2) "USAGE"
       3) "blah"
    5) "127.0.0.1:55372"
    6) ""
 3) 1) (integer) 56
    2) (integer) 1630080444
    3) (integer) 2
    4) 1) "MEMORY"
       2) "USAGE"
       3) "something"
    5) "127.0.0.1:55372"
    6) ""
 4) 1) (integer) 55
    2) (integer) 1630080444
    3) (integer) 1
    4) 1) "TYPE"
       2) "blah"
    5) "127.0.0.1:55372"
    6) ""
 5) 1) (integer) 54
    2) (integer) 1630080444
    3) (integer) 1
    4) 1) "TYPE"
       2) "something"
    5) "127.0.0.1:55372"
    6) ""
 6) 1) (integer) 53
    2) (integer) 1630080444
    3) (integer) 6
    4) 1) "SCAN"
       2) "0"
    5) "127.0.0.1:55372"
    6) ""
 7) 1) (integer) 52
    2) (integer) 1630080444
    3) (integer) 1
    4) 1) "DBSIZE"
    5) "127.0.0.1:55372"
    6) ""
 8) 1) (integer) 51
    2) (integer) 1630080436
    3) (integer) 1
    4) 1) "SCARD"
       2) "blah"
    5) "127.0.0.1:55371"
    6) ""
 9) 1) (integer) 50
    2) (integer) 1630080436
    3) (integer) 2
    4) 1) "LLEN"
       2) "something"
    5) "127.0.0.1:55371"
    6) ""
10) 1) (integer) 49
    2) (integer) 1630080436
    3) (integer) 1
    4) 1) "TYPE"
       2) "blah"
    5) "127.0.0.1:55371"
    6) ""
127.0.0.1:6379> SLOWLOG GET -1
 1) 1) (integer) 59
    2) (integer) 1630080478
    3) (integer) 24
    4) 1) "SLOWLOG"
       2) "get"
    5) "127.0.0.1:55375"
    6) ""
 2) 1) (integer) 58
    2) (integer) 1630080469
    3) (integer) 691
    4) 1) "COMMAND"
    5) "127.0.0.1:55375"
    6) ""
 3) 1) (integer) 57
    2) (integer) 1630080444
    3) (integer) 0
    4) 1) "MEMORY"
       2) "USAGE"
       3) "blah"
    5) "127.0.0.1:55372"
    6) ""
 4) 1) (integer) 56
    2) (integer) 1630080444
    3) (integer) 2
    4) 1) "MEMORY"
       2) "USAGE"
       3) "something"
    5) "127.0.0.1:55372"
    6) ""
 5) 1) (integer) 55
    2) (integer) 1630080444
    3) (integer) 1
    4) 1) "TYPE"
       2) "blah"
    5) "127.0.0.1:55372"
    6) ""
 6) 1) (integer) 54
    2) (integer) 1630080444
    3) (integer) 1
    4) 1) "TYPE"
       2) "something"
    5) "127.0.0.1:55372"
    6) ""
 7) 1) (integer) 53
    2) (integer) 1630080444
    3) (integer) 6
    4) 1) "SCAN"
       2) "0"
    5) "127.0.0.1:55372"
    6) ""
 8) 1) (integer) 52
    2) (integer) 1630080444
    3) (integer) 1
    4) 1) "DBSIZE"
    5) "127.0.0.1:55372"
    6) ""
 9) 1) (integer) 51
    2) (integer) 1630080436
    3) (integer) 1
    4) 1) "SCARD"
       2) "blah"
    5) "127.0.0.1:55371"
    6) ""
10) 1) (integer) 50
    2) (integer) 1630080436
    3) (integer) 2
    4) 1) "LLEN"
       2) "something"
    5) "127.0.0.1:55371"
    6) ""
11) 1) (integer) 49
    2) (integer) 1630080436
    3) (integer) 1
    4) 1) "TYPE"
       2) "blah"
    5) "127.0.0.1:55371"
    6) ""
12) 1) (integer) 48
    2) (integer) 1630080436
    3) (integer) 2
    4) 1) "TYPE"
       2) "something"
    5) "127.0.0.1:55371"
    6) ""
13) 1) (integer) 47
    2) (integer) 1630080436
    3) (integer) 4
    4) 1) "SCAN"
       2) "0"
    5) "127.0.0.1:55371"
    6) ""
14) 1) (integer) 46
    2) (integer) 1630080436
    3) (integer) 1
    4) 1) "DBSIZE"
    5) "127.0.0.1:55371"
    6) ""
15) 1) (integer) 45
    2) (integer) 1630080433
    3) (integer) 3
    4) 1) "SCARD"
       2) "blah"
    5) "127.0.0.1:55337"
    6) ""
16) 1) (integer) 44
    2) (integer) 1630080425
    3) (integer) 3
    4) 1) "LLEN"
       2) "something"
    5) "127.0.0.1:55337"
    6) ""
17) 1) (integer) 43
    2) (integer) 1630080420
    3) (integer) 26
    4) 1) "keys"
       2) "*"
    5) "127.0.0.1:55337"
    6) ""
18) 1) (integer) 42
    2) (integer) 1630080414
    3) (integer) 11
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
19) 1) (integer) 41
    2) (integer) 1630080414
    3) (integer) 15
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
20) 1) (integer) 40
    2) (integer) 1630080413
    3) (integer) 15
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
21) 1) (integer) 39
    2) (integer) 1630080412
    3) (integer) 21
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
22) 1) (integer) 38
    2) (integer) 1630080412
    3) (integer) 14
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
23) 1) (integer) 37
    2) (integer) 1630080411
    3) (integer) 14
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
24) 1) (integer) 36
    2) (integer) 1630080410
    3) (integer) 11
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
25) 1) (integer) 35
    2) (integer) 1630080410
    3) (integer) 12
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
26) 1) (integer) 34
    2) (integer) 1630080409
    3) (integer) 22
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
27) 1) (integer) 33
    2) (integer) 1630080400
    3) (integer) 11
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
28) 1) (integer) 32
    2) (integer) 1630080399
    3) (integer) 17
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
29) 1) (integer) 31
    2) (integer) 1630080398
    3) (integer) 23
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
30) 1) (integer) 30
    2) (integer) 1630080392
    3) (integer) 14
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
       12) "10"
       13) "10"
       14) "10"
       15) "10"
       16) "10"
       17) "10"
       18) "10"
       19) "10"
       20) "10"
       21) "10"
       22) "10"
       23) "10"
       24) "10"
       25) "10"
       26) "10"
       27) "10"
       28) "10"
       29) "10"
       30) "10"
       31) "10"
       32) "... (3 more arguments)"
    5) "127.0.0.1:55337"
    6) ""
31) 1) (integer) 29
    2) (integer) 1630080360
    3) (integer) 5
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
    5) "127.0.0.1:55337"
    6) ""
32) 1) (integer) 28
    2) (integer) 1630080359
    3) (integer) 10
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
    5) "127.0.0.1:55337"
    6) ""
33) 1) (integer) 27
    2) (integer) 1630080359
    3) (integer) 9
    4)  1) "RPUSH"
        2) "something"
        3) "10"
        4) "10"
        5) "10"
        6) "10"
        7) "10"
        8) "10"
        9) "10"
       10) "10"
       11) "10"
    5) "127.0.0.1:55337"
    6) ""
34) 1) (integer) 26
    2) (integer) 1630080348
    3) (integer) 5
    4) 1) "RPUSH"
       2) "something"
       3) "10"
    5) "127.0.0.1:55337"
    6) ""
35) 1) (integer) 25
    2) (integer) 1630080347
    3) (integer) 125
    4) 1) "RPUSH"
       2) "something"
       3) "10"
    5) "127.0.0.1:55337"
    6) ""
36) 1) (integer) 24
    2) (integer) 1630080338
    3) (integer) 6
    4) 1) "SADD"
       2) "blah"
       3) "2"
       4) "3"
       5) "5"
       6) "6"
       7) "7"
       8) "8"
    5) "127.0.0.1:55337"
    6) ""
37) 1) (integer) 23
    2) (integer) 1630080331
    3) (integer) 3
    4) 1) "SADD"
       2) "blah"
       3) "1"
    5) "127.0.0.1:55337"
    6) ""
38) 1) (integer) 22
    2) (integer) 1630080330
    3) (integer) 150
    4) 1) "SADD"
       2) "blah"
       3) "1"
    5) "127.0.0.1:55337"
    6) ""
39) 1) (integer) 21
    2) (integer) 1630080322
    3) (integer) 688
    4) 1) "COMMAND"
    5) "127.0.0.1:55337"
    6) ""
40) 1) (integer) 20
    2) (integer) 1630080277
    3) (integer) 12
    4) 1) "SCAN"
       2) "0"
    5) "127.0.0.1:55334"
    6) ""
41) 1) (integer) 19
    2) (integer) 1630080277
    3) (integer) 21
    4) 1) "DBSIZE"
    5) "127.0.0.1:55334"
    6) ""
42) 1) (integer) 18
    2) (integer) 1630080220
    3) (integer) 7
    4) 1) "SLOWLOG"
       2) "get"
       3) "2"
    5) "127.0.0.1:55319"
    6) "karuppiah"
43) 1) (integer) 17
    2) (integer) 1630080215
    3) (integer) 23
    4) 1) "SLOWLOG"
       2) "get"
    5) "127.0.0.1:55319"
    6) "karuppiah"
44) 1) (integer) 16
    2) (integer) 1630080213
    3) (integer) 2
    4) 1) "SLOWLOG"
       2) "len"
    5) "127.0.0.1:55319"
    6) "karuppiah"
45) 1) (integer) 15
    2) (integer) 1630080208
    3) (integer) 1
    4) 1) "CLIENT"
       2) "SETNAME"
       3) "karuppiah"
    5) "127.0.0.1:55319"
    6) "karuppiah"
46) 1) (integer) 14
    2) (integer) 1630080205
    3) (integer) 25
    4) 1) "CLIENT"
       2) "SETNAME"
    5) "127.0.0.1:55319"
    6) ""
47) 1) (integer) 13
    2) (integer) 1630080195
    3) (integer) 1
    4) 1) "CLIENT"
       2) "GETNAME"
    5) "127.0.0.1:55319"
    6) ""
48) 1) (integer) 12
    2) (integer) 1630080143
    3) (integer) 11
    4) 1) "SLOWLOG"
       2) "get"
    5) "127.0.0.1:55319"
    6) ""
49) 1) (integer) 11
    2) (integer) 1630080139
    3) (integer) 2
    4) 1) "SLOWLOG"
       2) "len"
    5) "127.0.0.1:55319"
    6) ""
50) 1) (integer) 10
    2) (integer) 1630080137
    3) (integer) 2
    4) 1) "SLOWLOG"
       2) "len"
    5) "127.0.0.1:55319"
    6) ""
51) 1) (integer) 9
    2) (integer) 1630080135
    3) (integer) 16
    4) 1) "SLOWLOG"
       2) "reset"
    5) "127.0.0.1:55319"
    6) ""
127.0.0.1:6379> 
```

In `--memkeys`, it says

```bash
[00.00%] Biggest list   found so far '"something"' with 1029 bytes
[00.00%] Biggest set    found so far '"blah"' with 78 bytes

-------- summary -------

Sampled 2 keys in the keyspace!
Total key length in bytes is 13 (avg len 6.50)

Biggest   list found '"something"' has 1029 bytes
Biggest    set found '"blah"' has 78 bytes
```

Interesting to see the total key length in bytes, which seems to be basically the size needed to store the keys, not the values. The keys here are `something` and `blah` and the total character length in both the strings is 13, 1 byte for each character and you get 13 bytes. Hmm

The value size is the one mentioning biggest list and set I guess. More bytes, not just 13. It's 1029 bytes and 78 bytes.

---

I just tried `MONITOR` command

```bash
redis-stuff $ redis-cli
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> ping
PONG
127.0.0.1:6379> 
```

```bash
127.0.0.1:6379> MONITOR
OK
1630080726.963840 [0 127.0.0.1:55400] "COMMAND"
1630080727.960505 [0 127.0.0.1:55400] "ping"
1630080731.308710 [0 127.0.0.1:55400] "ping"
^C
```

I had tried it before too, the interesting thing that I hadn't noticed before was the `COMMAND` in the output. Not sure why it came up only once. Maybe it meant to say that the upcoming stuff is gonna be commands? I don't know

I just tried the `--hotkeys` option

```bash
redis-stuff $ redis-cli --hotkeys

# Scanning the entire keyspace to find hot keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

Error: ERR An LFU maxmemory policy is not selected, access frequency not tracked. Please note that when switching between policies at runtime LRU and LFU data will take some time to adjust.
redis-stuff $ 
```

Not sure what the LFU maxmemory policy is. If I had to guess...with the word `frequency` being mentioned and having know LRU from college days - "Least Recently Used". So, LFU - Least Frequently Used?

I just set one of the give maxmemory policy as mentioned in the exercise, it said either `volatile-lfu` or `allkeys-lfu`

```bash
redis-stuff $ redis-cli
127.0.0.1:6379> CONFIG GET maxmemory-policy
1) "maxmemory-policy"
2) "noeviction"
127.0.0.1:6379> CONFIG SET maxmemory-policy volatile-lfu
OK
127.0.0.1:6379> 
redis-stuff $ redis-cli --hotkeys

# Scanning the entire keyspace to find hot keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).


-------- summary -------

Sampled 2 keys in the keyspace!
redis-stuff $ redis-cli
127.0.0.1:6379> get something
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> SCARD something
(error) WRONGTYPE Operation against a key holding the wrong kind of value
127.0.0.1:6379> llen something
(integer) 445
127.0.0.1:6379> llen something
(integer) 445
127.0.0.1:6379> llen something
(integer) 445
127.0.0.1:6379> llen something
(integer) 445
127.0.0.1:6379> llen something
(integer) 445
127.0.0.1:6379> llen something
(integer) 445
127.0.0.1:6379> 
redis-stuff $ redis-cli --hotkeys

# Scanning the entire keyspace to find hot keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Hot key '"something"' found so far with counter 7

-------- summary -------

Sampled 2 keys in the keyspace!
hot key found with counter: 7	keyname: "something"
redis-stuff $ 
```

I just confirmed that my guess about "hot keys" is right. Hot keys are keys which are Hot :P Hot keys are keys which are accessed very frequently, hmm, or more like, keys which are accessed a lot. Not sure about the frequency part. Gotta check [TODO]

---

Now I'm checking about logging

https://duckduckgo.com/?t=ffab&q=redis+conf&ia=web

https://duckduckgo.com/?t=ffab&q=redis+default+conf&ia=web

https://redis.io/topics/config

https://raw.githubusercontent.com/redis/redis/6.0/redis.conf

The config I wrote was - `redis.conf`

```
logfile "redis.log"
```

The log is in `redis.log` file now
