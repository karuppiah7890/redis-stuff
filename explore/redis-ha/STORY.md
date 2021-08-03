# Redis HA - High Availability

I'm currently checking out this nice blog post that an ex-colleague (https://github.com/aswinkarthik) wrote based on the Redis HA setup we had in a previous project

https://aswinkarthik.dev/post/redis-ha-on-kubernetes/

https://redis.io/topics/replication

https://redis.io/topics/sentinel

https://github.com/thecasualcoder/kube-template

I'm reading the redis replication page

https://redis.io/topics/replication

Some replication related commands -

https://redis.io/commands/psync

https://redis.io/commands/sync

Looks like PSYNC is the latest thing

PSYNC allows partial synchronization is what I'm reading

"Actually SYNC is an old protocol no longer used by newer Redis instances, but is still there for backward compatibility: it does not allow partial resynchronizations, so now PSYNC is used instead."

I just tried doing a replication -

Primary Server -

```bash
karuppiahn-a01:~ karuppiahn$ redis-server 
16408:C 03 Aug 2021 14:53:07.109 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16408:C 03 Aug 2021 14:53:07.110 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=16408, just started
16408:C 03 Aug 2021 14:53:07.110 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
16408:M 03 Aug 2021 14:53:07.111 * Increased maximum number of open files to 10032 (it was originally set to 256).
16408:M 03 Aug 2021 14:53:07.111 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 16408
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16408:M 03 Aug 2021 14:53:07.112 # Server initialized
16408:M 03 Aug 2021 14:53:07.113 * Loading RDB produced by version 6.2.5
16408:M 03 Aug 2021 14:53:07.113 * RDB age 108 seconds
16408:M 03 Aug 2021 14:53:07.113 * RDB memory usage when created 0.98 Mb
16408:M 03 Aug 2021 14:53:07.113 * DB loaded from disk: 0.000 seconds
16408:M 03 Aug 2021 14:53:07.113 * Ready to accept connections
16408:M 03 Aug 2021 14:54:57.194 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 14:54:57.194 * Partial resynchronization not accepted: Replication ID mismatch (Replica asked for 'f8e5a3ce0cc56c1dae31edf595eff12c987d9de0', my replication IDs are '7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2' and '0000000000000000000000000000000000000000')
16408:M 03 Aug 2021 14:54:57.195 * Replication backlog created, my new replication IDs are '67e88ce14822ac26e68a80f6bb3055b302d300d7' and '0000000000000000000000000000000000000000'
16408:M 03 Aug 2021 14:54:57.195 * Starting BGSAVE for SYNC with target: disk
16408:M 03 Aug 2021 14:54:57.195 * Background saving started by pid 18242
18242:C 03 Aug 2021 14:54:57.197 * DB saved on disk
16408:M 03 Aug 2021 14:54:57.248 * Background saving terminated with success
16408:M 03 Aug 2021 14:54:57.248 * Synchronization with replica [::1]:6380 succeeded
```

Replica Server -

```bash
karuppiahn-a01:~ karuppiahn$ redis-server -p 6380

*** FATAL CONFIG FILE ERROR (Redis 6.2.5) ***
Reading the configuration file, at line 2
>>> '"-p" "6380"'
Bad directive or wrong number of arguments
karuppiahn-a01:~ karuppiahn$ redis-server -h
Usage: ./redis-server [/path/to/redis.conf] [options] [-]
       ./redis-server - (read config from stdin)
       ./redis-server -v or --version
       ./redis-server -h or --help
       ./redis-server --test-memory <megabytes>

Examples:
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --replicaof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose -
       ./redis-server /etc/myredis.conf --loglevel verbose

Sentinel mode:
       ./redis-server /etc/sentinel.conf --sentinel
karuppiahn-a01:~ karuppiahn$ redis-server --port 6380
16991:C 03 Aug 2021 14:53:34.008 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16991:C 03 Aug 2021 14:53:34.008 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=16991, just started
16991:C 03 Aug 2021 14:53:34.008 # Configuration loaded
16991:M 03 Aug 2021 14:53:34.009 * Increased maximum number of open files to 10032 (it was originally set to 2560).
16991:M 03 Aug 2021 14:53:34.009 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 16991
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16991:M 03 Aug 2021 14:53:34.010 # Server initialized
16991:M 03 Aug 2021 14:53:34.010 * Loading RDB produced by version 6.2.5
16991:M 03 Aug 2021 14:53:34.010 * RDB age 135 seconds
16991:M 03 Aug 2021 14:53:34.010 * RDB memory usage when created 0.98 Mb
16991:M 03 Aug 2021 14:53:34.010 * DB loaded from disk: 0.000 seconds
16991:M 03 Aug 2021 14:53:34.010 * Ready to accept connections
16991:S 03 Aug 2021 14:54:57.188 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
16991:S 03 Aug 2021 14:54:57.188 * Connecting to MASTER localhost:6379
16991:S 03 Aug 2021 14:54:57.194 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 14:54:57.194 * REPLICAOF localhost:6379 enabled (user request from 'id=3 addr=127.0.0.1:49694 laddr=127.0.0.1:6380 fd=8 name= age=57 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=44 qbuf-free=65486 argv-mem=22 obl=0 oll=0 omem=0 tot-mem=82998 events=r cmd=replicaof user=default redir=-1')
16991:S 03 Aug 2021 14:54:57.194 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 14:54:57.194 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 14:54:57.194 * Trying a partial resynchronization (request f8e5a3ce0cc56c1dae31edf595eff12c987d9de0:1).
16991:S 03 Aug 2021 14:54:57.195 * Full resync from master: 67e88ce14822ac26e68a80f6bb3055b302d300d7:0
16991:S 03 Aug 2021 14:54:57.195 * Discarding previously cached master state.
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: receiving 319 bytes from master to disk
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: Flushing old data
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: Loading DB in memory
16991:S 03 Aug 2021 14:54:57.249 * Loading RDB produced by version 6.2.5
16991:S 03 Aug 2021 14:54:57.249 * RDB age 0 seconds
16991:S 03 Aug 2021 14:54:57.249 * RDB memory usage when created 2.08 Mb
16991:S 03 Aug 2021 14:54:57.249 * MASTER <-> REPLICA sync: Finished with success
```

Replica CLI -

```bash
Last login: Tue Aug  3 14:53:07 on ttys002
rkaruppiahn-a01:~ karuppiahn$ redis-cli :6380
(error) ERR unknown command `:6380`, with args beginning with: 
karuppiahn-a01:~ karuppiahn$ redis-cli localhost:6380
(error) ERR unknown command `localhost:6380`, with args beginning with: 
karuppiahn-a01:~ karuppiahn$ redis-cli -c localhost:6380
(error) ERR unknown command `localhost:6380`, with args beginning with: 
karuppiahn-a01:~ karuppiahn$ redis-cli -h localhost:6380
Could not connect to Redis at localhost:6380:6379: nodename nor servname provided, or not known
not connected> 
karuppiahn-a01:~ karuppiahn$ redis-cli -h localhost -p 6380
localhost:6380> info
# Server
redis_version:6.2.5
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:915e5480613bc9b6
redis_mode:standalone
os:Darwin 20.6.0 x86_64
arch_bits:64
multiplexing_api:kqueue
atomicvar_api:c11-builtin
gcc_version:4.2.1
process_id:16991
process_supervised:no
run_id:19aec676d2af98d943d4919c1787a16d179c5ccf
tcp_port:6380
server_time_usec:1627982645914789
uptime_in_seconds:31
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:592693
executable:/Users/karuppiahn/redis-server
config_file:
io_threads_active:0

# Clients
connected_clients:1
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:32
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:1111536
used_memory_human:1.06M
used_memory_rss:3702784
used_memory_rss_human:3.53M
used_memory_peak:1169920
used_memory_peak_human:1.12M
used_memory_peak_perc:95.01%
used_memory_overhead:1043240
used_memory_startup:1025616
used_memory_dataset:68296
used_memory_dataset_perc:79.49%
allocator_allocated:1043936
allocator_active:3664896
allocator_resident:3664896
total_system_memory:34359738368
total_system_memory_human:32.00G
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:3.51
allocator_frag_bytes:2620960
allocator_rss_ratio:1.00
allocator_rss_bytes:0
rss_overhead_ratio:1.01
rss_overhead_bytes:37888
mem_fragmentation_ratio:3.55
mem_fragmentation_bytes:2658848
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:17440
mem_aof_buffer:0
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1627982614
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:-1
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:0
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:1
total_commands_processed:1
instantaneous_ops_per_sec:0
total_net_input_bytes:31
total_net_output_bytes:20324
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:0
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:0
total_forks:0
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:0
dump_payload_sanitizations:0
total_reads_processed:2
total_writes_processed:1
io_threaded_reads_processed:0
io_threaded_writes_processed:0

# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:f8e5a3ce0cc56c1dae31edf595eff12c987d9de0
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:0.019996
used_cpu_user:0.016798
used_cpu_sys_children:0.000000
used_cpu_user_children:0.000000

# Modules

# Errorstats

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=3,expires=0,avg_ttl=0
localhost:6380> info replication
# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:f8e5a3ce0cc56c1dae31edf595eff12c987d9de0
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0
localhost:6380> replicaof localhost 
(error) ERR wrong number of arguments for 'replicaof' command
localhost:6380> replicaof 
(error) ERR wrong number of arguments for 'replicaof' command
localhost:6380> replicaof localhost 6379
OK
localhost:6380> info replication
# Replication
role:slave
master_host:localhost
master_port:6379
master_link_status:up
master_last_io_seconds_ago:5
master_sync_in_progress:0
slave_repl_offset:14
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:14
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:14
localhost:6380> info 
# Server
redis_version:6.2.5
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:915e5480613bc9b6
redis_mode:standalone
os:Darwin 20.6.0 x86_64
arch_bits:64
multiplexing_api:kqueue
atomicvar_api:c11-builtin
gcc_version:4.2.1
process_id:16991
process_supervised:no
run_id:19aec676d2af98d943d4919c1787a16d179c5ccf
tcp_port:6380
server_time_usec:1627982708138379
uptime_in_seconds:94
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:592756
executable:/Users/karuppiahn/redis-server
config_file:
io_threads_active:0

# Clients
connected_clients:2
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:48
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:2178160
used_memory_human:2.08M
used_memory_rss:3895296
used_memory_rss_human:3.71M
used_memory_peak:2178160
used_memory_peak_human:2.08M
used_memory_peak_perc:100.09%
used_memory_overhead:2109256
used_memory_startup:1025616
used_memory_dataset:68904
used_memory_dataset_perc:5.98%
allocator_allocated:2110560
allocator_active:3857408
allocator_resident:3857408
total_system_memory:34359738368
total_system_memory_human:32.00G
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.83
allocator_frag_bytes:1746848
allocator_rss_ratio:1.00
allocator_rss_bytes:0
rss_overhead_ratio:1.01
rss_overhead_bytes:37888
mem_fragmentation_ratio:1.85
mem_fragmentation_bytes:1784736
mem_not_counted_for_evict:0
mem_replication_backlog:1048576
mem_clients_slaves:0
mem_clients_normal:34880
mem_aof_buffer:0
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1627982614
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:-1
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:0
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:1
total_commands_processed:6
instantaneous_ops_per_sec:0
total_net_input_bytes:539
total_net_output_bytes:25747
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.04
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:1
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:0
total_forks:0
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:2
dump_payload_sanitizations:0
total_reads_processed:9
total_writes_processed:18
io_threaded_reads_processed:0
io_threaded_writes_processed:0

# Replication
role:slave
master_host:localhost
master_port:6379
master_link_status:up
master_last_io_seconds_ago:8
master_sync_in_progress:0
slave_repl_offset:14
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:14
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:14

# CPU
used_cpu_sys:0.051537
used_cpu_user:0.037927
used_cpu_sys_children:0.000000
used_cpu_user_children:0.000000

# Modules

# Errorstats
errorstat_ERR:count=2

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=3,expires=0,avg_ttl=0
localhost:6380> 
```

Primary CLI -

```bash
Last login: Tue Aug  3 14:53:35 on ttys003
karuppiahn-a01:~ karuppiahn$ redis-cli -h localhost -p 6379
localhost:6379> 
karuppiahn-a01:~ karuppiahn$ redis-cli 
127.0.0.1:6379> info
# Server
redis_version:6.2.5
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:915e5480613bc9b6
redis_mode:standalone
os:Darwin 20.6.0 x86_64
arch_bits:64
multiplexing_api:kqueue
atomicvar_api:c11-builtin
gcc_version:4.2.1
process_id:16408
process_supervised:no
run_id:34621fa900d096d7c248d5c5fa30c609db617dcb
tcp_port:6379
server_time_usec:1627982672333786
uptime_in_seconds:85
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:592720
executable:/Users/karuppiahn/redis-server
config_file:
io_threads_active:0

# Clients
connected_clients:1
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:32
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:1111520
used_memory_human:1.06M
used_memory_rss:3784704
used_memory_rss_human:3.61M
used_memory_peak:1170080
used_memory_peak_human:1.12M
used_memory_peak_perc:95.00%
used_memory_overhead:1043192
used_memory_startup:1025568
used_memory_dataset:68328
used_memory_dataset_perc:79.50%
allocator_allocated:1043920
allocator_active:3746816
allocator_resident:3746816
total_system_memory:34359738368
total_system_memory_human:32.00G
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:3.59
allocator_frag_bytes:2702896
allocator_rss_ratio:1.00
allocator_rss_bytes:0
rss_overhead_ratio:1.01
rss_overhead_bytes:37888
mem_fragmentation_ratio:3.63
mem_fragmentation_bytes:2740784
mem_not_counted_for_evict:0
mem_replication_backlog:0
mem_clients_slaves:0
mem_clients_normal:17440
mem_aof_buffer:0
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1627982587
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:-1
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:0
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:5
total_commands_processed:2
instantaneous_ops_per_sec:0
total_net_input_bytes:113
total_net_output_bytes:40840
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:1
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:0
total_forks:0
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:3
dump_payload_sanitizations:0
total_reads_processed:10
total_writes_processed:5
io_threaded_reads_processed:0
io_threaded_writes_processed:0

# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:0.048297
used_cpu_user:0.034020
used_cpu_sys_children:0.000000
used_cpu_user_children:0.000000

# Modules

# Errorstats
errorstat_ERR:count=3

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=3,expires=0,avg_ttl=0
127.0.0.1:6379> info replication
# Replication
role:master
connected_slaves:0
master_failover_state:no-failover
master_replid:7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0
127.0.0.1:6379> info replication
# Replication
role:master
connected_slaves:1
slave0:ip=::1,port=6380,state=online,offset=28,lag=1
master_failover_state:no-failover
master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:28
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:28
127.0.0.1:6379> info
# Server
redis_version:6.2.5
redis_git_sha1:00000000
redis_git_dirty:0
redis_build_id:915e5480613bc9b6
redis_mode:standalone
os:Darwin 20.6.0 x86_64
arch_bits:64
multiplexing_api:kqueue
atomicvar_api:c11-builtin
gcc_version:4.2.1
process_id:16408
process_supervised:no
run_id:34621fa900d096d7c248d5c5fa30c609db617dcb
tcp_port:6379
server_time_usec:1627982714369498
uptime_in_seconds:127
uptime_in_days:0
hz:10
configured_hz:10
lru_clock:592762
executable:/Users/karuppiahn/redis-server
config_file:
io_threads_active:0

# Clients
connected_clients:1
cluster_connections:0
maxclients:10000
client_recent_max_input_buffer:48
client_recent_max_output_buffer:0
blocked_clients:0
tracking_clients:0
clients_in_timeout_table:0

# Memory
used_memory:2178080
used_memory_human:2.08M
used_memory_rss:3870720
used_memory_rss_human:3.69M
used_memory_peak:2178080
used_memory_peak_human:2.08M
used_memory_peak_perc:100.09%
used_memory_overhead:2109224
used_memory_startup:1025568
used_memory_dataset:68856
used_memory_dataset_perc:5.97%
allocator_allocated:2110480
allocator_active:3832832
allocator_resident:3832832
total_system_memory:34359738368
total_system_memory_human:32.00G
used_memory_lua:37888
used_memory_lua_human:37.00K
used_memory_scripts:0
used_memory_scripts_human:0B
number_of_cached_scripts:0
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
allocator_frag_ratio:1.82
allocator_frag_bytes:1722352
allocator_rss_ratio:1.00
allocator_rss_bytes:0
rss_overhead_ratio:1.01
rss_overhead_bytes:37888
mem_fragmentation_ratio:1.83
mem_fragmentation_bytes:1760240
mem_not_counted_for_evict:0
mem_replication_backlog:1048576
mem_clients_slaves:17456
mem_clients_normal:17440
mem_aof_buffer:0
mem_allocator:libc
active_defrag_running:0
lazyfree_pending_objects:0
lazyfreed_objects:0

# Persistence
loading:0
current_cow_size:0
current_cow_size_age:0
current_fork_perc:0.00
current_save_keys_processed:0
current_save_keys_total:0
rdb_changes_since_last_save:0
rdb_bgsave_in_progress:0
rdb_last_save_time:1627982697
rdb_last_bgsave_status:ok
rdb_last_bgsave_time_sec:0
rdb_current_bgsave_time_sec:-1
rdb_last_cow_size:0
aof_enabled:0
aof_rewrite_in_progress:0
aof_rewrite_scheduled:0
aof_last_rewrite_time_sec:-1
aof_current_rewrite_time_sec:-1
aof_last_bgrewrite_status:ok
aof_last_write_status:ok
aof_last_cow_size:0
module_fork_in_progress:0
module_fork_last_cow_size:0

# Stats
total_connections_received:6
total_commands_processed:26
instantaneous_ops_per_sec:1
total_net_input_bytes:975
total_net_output_bytes:46011
instantaneous_input_kbps:0.04
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:1
sync_partial_ok:0
sync_partial_err:1
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
expire_cycle_cpu_milliseconds:1
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:450
total_forks:1
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0
tracking_total_keys:0
tracking_total_items:0
tracking_total_prefixes:0
unexpected_error_replies:0
total_error_replies:3
dump_payload_sanitizations:0
total_reads_processed:34
total_writes_processed:13
io_threaded_reads_processed:0
io_threaded_writes_processed:0

# Replication
role:master
connected_slaves:1
slave0:ip=::1,port=6380,state=online,offset=28,lag=1
master_failover_state:no-failover
master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:28
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:28

# CPU
used_cpu_sys:0.069955
used_cpu_user:0.049052
used_cpu_sys_children:0.001415
used_cpu_user_children:0.000437

# Modules

# Errorstats
errorstat_ERR:count=3

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=3,expires=0,avg_ttl=0
127.0.0.1:6379> 
```

Quite some details in the CLI of the primary and replica

In the replica I can see the `offset`s

Replica CLI -

```bash
localhost:6380> info replication
# Replication
role:slave
master_host:localhost
master_port:6379
master_link_status:up
master_last_io_seconds_ago:8
master_sync_in_progress:0
slave_repl_offset:252
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:252
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:252
localhost:6380> 
```

It says `slave_repl_offset:252` and `master_repl_offset:252` for it's own offset and the primary's offset

There's the use of lot of master/slave language instead of primary/replica or leader/follower, hmm

And the offset values keep changing, though I never put any data in the primary! Atleast nothing after I just started the primary and replica servers

Let me try to do a write operatin in the replica CLI ;)

Replica CLI

```bash
localhost:6380> keys *
1) "bitmap"
2) "hw5-1"
3) "yosemite:attractions"
localhost:6380> set blah bloo
(error) READONLY You can't write against a read only replica.
localhost:6380> 
```

It errors out properly saying it's `READONLY` and that I can't write against a read only replica :)

Regarding replication ID apart from the offset, the replication ID is also mentioned in the `info` fields, under `replication` section

The fields I noticed with respect to replication ID are `master_replid` and `master_replid2`

We can notice how the replication ID has changed all the while but there's no second / secondary replication, only one main replication ID

From the commands -

```bash
master_replid:f8e5a3ce0cc56c1dae31edf595eff12c987d9de0
master_replid2:0000000000000000000000000000000000000000


master_replid:f8e5a3ce0cc56c1dae31edf595eff12c987d9de0
master_replid2:0000000000000000000000000000000000000000


master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000


master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000


master_replid:7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2
master_replid2:0000000000000000000000000000000000000000


master_replid:7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2
master_replid2:0000000000000000000000000000000000000000


master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000


master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000


master_replid:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_replid2:0000000000000000000000000000000000000000
```

The final replication ID is `67e88ce14822ac26e68a80f6bb3055b302d300d7`


Now after quite sometime the primary server logs looks like this -

```bash
karuppiahn-a01:~ karuppiahn$ redis-server 
16408:C 03 Aug 2021 14:53:07.109 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16408:C 03 Aug 2021 14:53:07.110 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=16408, just started
16408:C 03 Aug 2021 14:53:07.110 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
16408:M 03 Aug 2021 14:53:07.111 * Increased maximum number of open files to 10032 (it was originally set to 256).
16408:M 03 Aug 2021 14:53:07.111 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 16408
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16408:M 03 Aug 2021 14:53:07.112 # Server initialized
16408:M 03 Aug 2021 14:53:07.113 * Loading RDB produced by version 6.2.5
16408:M 03 Aug 2021 14:53:07.113 * RDB age 108 seconds
16408:M 03 Aug 2021 14:53:07.113 * RDB memory usage when created 0.98 Mb
16408:M 03 Aug 2021 14:53:07.113 * DB loaded from disk: 0.000 seconds
16408:M 03 Aug 2021 14:53:07.113 * Ready to accept connections
16408:M 03 Aug 2021 14:54:57.194 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 14:54:57.194 * Partial resynchronization not accepted: Replication ID mismatch (Replica asked for 'f8e5a3ce0cc56c1dae31edf595eff12c987d9de0', my replication IDs are '7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2' and '0000000000000000000000000000000000000000')
16408:M 03 Aug 2021 14:54:57.195 * Replication backlog created, my new replication IDs are '67e88ce14822ac26e68a80f6bb3055b302d300d7' and '0000000000000000000000000000000000000000'
16408:M 03 Aug 2021 14:54:57.195 * Starting BGSAVE for SYNC with target: disk
16408:M 03 Aug 2021 14:54:57.195 * Background saving started by pid 18242
18242:C 03 Aug 2021 14:54:57.197 * DB saved on disk
16408:M 03 Aug 2021 14:54:57.248 * Background saving terminated with success
16408:M 03 Aug 2021 14:54:57.248 * Synchronization with replica [::1]:6380 succeeded
16408:M 03 Aug 2021 15:36:05.794 # Disconnecting timedout replica (streaming sync): [::1]:6380
16408:M 03 Aug 2021 15:36:05.794 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 15:36:05.797 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 15:36:05.797 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 1527.
16408:M 03 Aug 2021 16:02:09.751 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 16:02:09.753 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 16:02:09.753 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 3501.
16408:M 03 Aug 2021 16:52:43.840 # Disconnecting timedout replica (streaming sync): [::1]:6380
16408:M 03 Aug 2021 16:52:43.840 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 16:52:43.843 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 16:52:43.843 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 5601.
16408:M 03 Aug 2021 20:04:24.156 # Disconnecting timedout replica (streaming sync): [::1]:6380
16408:M 03 Aug 2021 20:04:24.156 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 20:04:24.159 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 20:04:24.159 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 5685.

```

And after quite sometime the replica server logs looks like this -

```bash
karuppiahn-a01:~ karuppiahn$ redis-server -p 6380

*** FATAL CONFIG FILE ERROR (Redis 6.2.5) ***
Reading the configuration file, at line 2
>>> '"-p" "6380"'
Bad directive or wrong number of arguments
karuppiahn-a01:~ karuppiahn$ redis-server -h
Usage: ./redis-server [/path/to/redis.conf] [options] [-]
       ./redis-server - (read config from stdin)
       ./redis-server -v or --version
       ./redis-server -h or --help
       ./redis-server --test-memory <megabytes>

Examples:
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --replicaof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose -
       ./redis-server /etc/myredis.conf --loglevel verbose

Sentinel mode:
       ./redis-server /etc/sentinel.conf --sentinel
karuppiahn-a01:~ karuppiahn$ redis-server --port 6380
16991:C 03 Aug 2021 14:53:34.008 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16991:C 03 Aug 2021 14:53:34.008 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=16991, just started
16991:C 03 Aug 2021 14:53:34.008 # Configuration loaded
16991:M 03 Aug 2021 14:53:34.009 * Increased maximum number of open files to 10032 (it was originally set to 2560).
16991:M 03 Aug 2021 14:53:34.009 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 16991
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16991:M 03 Aug 2021 14:53:34.010 # Server initialized
16991:M 03 Aug 2021 14:53:34.010 * Loading RDB produced by version 6.2.5
16991:M 03 Aug 2021 14:53:34.010 * RDB age 135 seconds
16991:M 03 Aug 2021 14:53:34.010 * RDB memory usage when created 0.98 Mb
16991:M 03 Aug 2021 14:53:34.010 * DB loaded from disk: 0.000 seconds
16991:M 03 Aug 2021 14:53:34.010 * Ready to accept connections
16991:S 03 Aug 2021 14:54:57.188 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
16991:S 03 Aug 2021 14:54:57.188 * Connecting to MASTER localhost:6379
16991:S 03 Aug 2021 14:54:57.194 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 14:54:57.194 * REPLICAOF localhost:6379 enabled (user request from 'id=3 addr=127.0.0.1:49694 laddr=127.0.0.1:6380 fd=8 name= age=57 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=44 qbuf-free=65486 argv-mem=22 obl=0 oll=0 omem=0 tot-mem=82998 events=r cmd=replicaof user=default redir=-1')
16991:S 03 Aug 2021 14:54:57.194 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 14:54:57.194 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 14:54:57.194 * Trying a partial resynchronization (request f8e5a3ce0cc56c1dae31edf595eff12c987d9de0:1).
16991:S 03 Aug 2021 14:54:57.195 * Full resync from master: 67e88ce14822ac26e68a80f6bb3055b302d300d7:0
16991:S 03 Aug 2021 14:54:57.195 * Discarding previously cached master state.
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: receiving 319 bytes from master to disk
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: Flushing old data
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: Loading DB in memory
16991:S 03 Aug 2021 14:54:57.249 * Loading RDB produced by version 6.2.5
16991:S 03 Aug 2021 14:54:57.249 * RDB age 0 seconds
16991:S 03 Aug 2021 14:54:57.249 * RDB memory usage when created 2.08 Mb
16991:S 03 Aug 2021 14:54:57.249 * MASTER <-> REPLICA sync: Finished with success
16991:S 03 Aug 2021 15:36:05.794 # Connection with master lost.
16991:S 03 Aug 2021 15:36:05.794 * Caching the disconnected master state.
16991:S 03 Aug 2021 15:36:05.795 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 15:36:05.796 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 15:36:05.796 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 15:36:05.797 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 15:36:05.797 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:1527).
16991:S 03 Aug 2021 15:36:05.798 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 15:36:05.798 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 16:02:09.750 # MASTER timeout: no data nor PING received...
16991:S 03 Aug 2021 16:02:09.751 # Connection with master lost.
16991:S 03 Aug 2021 16:02:09.751 * Caching the disconnected master state.
16991:S 03 Aug 2021 16:02:09.751 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 16:02:09.752 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 16:02:09.752 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 16:02:09.753 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 16:02:09.753 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:3501).
16991:S 03 Aug 2021 16:02:09.753 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 16:02:09.754 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 16:52:43.840 # Connection with master lost.
16991:S 03 Aug 2021 16:52:43.840 * Caching the disconnected master state.
16991:S 03 Aug 2021 16:52:43.840 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 16:52:43.841 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 16:52:43.842 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 16:52:43.842 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 16:52:43.842 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:5601).
16991:S 03 Aug 2021 16:52:43.843 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 16:52:43.843 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 20:04:24.156 # Connection with master lost.
16991:S 03 Aug 2021 20:04:24.156 * Caching the disconnected master state.
16991:S 03 Aug 2021 20:04:24.156 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 20:04:24.158 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 20:04:24.158 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 20:04:24.159 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 20:04:24.159 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:5685).
16991:S 03 Aug 2021 20:04:24.159 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 20:04:24.159 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.

```

Also, when running `role` command, we see some role information

Replica CLI -

```bash
localhost:6380> role
1) "slave"
2) "localhost"
3) (integer) 6379
4) "connected"
5) (integer) 6552
localhost:6380> 
```

Primary CLI -

```bash
127.0.0.1:6379> role
1) "master"
2) (integer) 6552
3) 1) 1) "::1"
      2) "6380"
      3) "6552"
127.0.0.1:6379> 
```

https://redis.io/commands/role

https://redis.io/commands/info

I was reading more of the replication information

https://redis.io/topics/replication

I was also thinking about failovers. I was checking how to do a failover. I remember that long ago we used to do failover by
- Having a replica for the primary
- Stopping client connections to the primary redis
- Finally run `replicaof no one` in the replica to make it primary redis
- Open up client connections for the primary redis

This was mainly for migrating a standalone redis running in one kubernetes cluster to another kubernetes cluster, so we didn't make the old primary as a replica of the new primary. Instead the old primary was later marked for a planned decomissioning to remove all the resources related to the redis - disk, the redis itself, any DNS records etc

I just read about failover command

https://redis.io/commands/failover

There's mention of `CLIENT PAUSE WRITE` command - https://redis.io/commands/client-pause , https://redis.io/commands/wait

I finally read all of the things. It was pretty interesting to see the stuff that goes on behind the scenes, but it was complicated too - many possible cases - if conditions and what not about how the whole thing works and what all options are available and also mentions about what Redis versions support what

Now, after the failover, the logs look like this 

Old Primary which is now Replica -

```bash
karuppiahn-a01:~ karuppiahn$ redis-server 
16408:C 03 Aug 2021 14:53:07.109 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16408:C 03 Aug 2021 14:53:07.110 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=16408, just started
16408:C 03 Aug 2021 14:53:07.110 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
16408:M 03 Aug 2021 14:53:07.111 * Increased maximum number of open files to 10032 (it was originally set to 256).
16408:M 03 Aug 2021 14:53:07.111 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6379
 |    `-._   `._    /     _.-'    |     PID: 16408
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16408:M 03 Aug 2021 14:53:07.112 # Server initialized
16408:M 03 Aug 2021 14:53:07.113 * Loading RDB produced by version 6.2.5
16408:M 03 Aug 2021 14:53:07.113 * RDB age 108 seconds
16408:M 03 Aug 2021 14:53:07.113 * RDB memory usage when created 0.98 Mb
16408:M 03 Aug 2021 14:53:07.113 * DB loaded from disk: 0.000 seconds
16408:M 03 Aug 2021 14:53:07.113 * Ready to accept connections
16408:M 03 Aug 2021 14:54:57.194 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 14:54:57.194 * Partial resynchronization not accepted: Replication ID mismatch (Replica asked for 'f8e5a3ce0cc56c1dae31edf595eff12c987d9de0', my replication IDs are '7ca1484d1dfb11b477a9f46236e1b3c2f4e60eb2' and '0000000000000000000000000000000000000000')
16408:M 03 Aug 2021 14:54:57.195 * Replication backlog created, my new replication IDs are '67e88ce14822ac26e68a80f6bb3055b302d300d7' and '0000000000000000000000000000000000000000'
16408:M 03 Aug 2021 14:54:57.195 * Starting BGSAVE for SYNC with target: disk
16408:M 03 Aug 2021 14:54:57.195 * Background saving started by pid 18242
18242:C 03 Aug 2021 14:54:57.197 * DB saved on disk
16408:M 03 Aug 2021 14:54:57.248 * Background saving terminated with success
16408:M 03 Aug 2021 14:54:57.248 * Synchronization with replica [::1]:6380 succeeded
16408:M 03 Aug 2021 15:36:05.794 # Disconnecting timedout replica (streaming sync): [::1]:6380
16408:M 03 Aug 2021 15:36:05.794 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 15:36:05.797 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 15:36:05.797 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 1527.
16408:M 03 Aug 2021 16:02:09.751 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 16:02:09.753 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 16:02:09.753 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 3501.
16408:M 03 Aug 2021 16:52:43.840 # Disconnecting timedout replica (streaming sync): [::1]:6380
16408:M 03 Aug 2021 16:52:43.840 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 16:52:43.843 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 16:52:43.843 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 5601.
16408:M 03 Aug 2021 20:04:24.156 # Disconnecting timedout replica (streaming sync): [::1]:6380
16408:M 03 Aug 2021 20:04:24.156 # Connection with replica [::1]:6380 lost.
16408:M 03 Aug 2021 20:04:24.159 * Replica [::1]:6380 asks for synchronization
16408:M 03 Aug 2021 20:04:24.159 * Partial resynchronization request from [::1]:6380 accepted. Sending 0 bytes of backlog starting from offset 5685.
16408:M 03 Aug 2021 21:25:11.496 * 1 changes in 3600 seconds. Saving...
16408:M 03 Aug 2021 21:25:11.497 * Background saving started by pid 43786
43786:C 03 Aug 2021 21:25:11.499 * DB saved on disk
16408:M 03 Aug 2021 21:25:11.600 * Background saving terminated with success
16408:M 03 Aug 2021 21:37:58.439 * FAILOVER requested to any replica.
16408:M 03 Aug 2021 21:37:58.439 * Failover target ::1:6380 is synced, failing over.
16408:S 03 Aug 2021 21:37:58.439 # Connection with replica [::1]:6380 lost.
16408:S 03 Aug 2021 21:37:58.439 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
16408:S 03 Aug 2021 21:37:58.439 * Connecting to MASTER ::1:6380
16408:S 03 Aug 2021 21:37:58.440 * MASTER <-> REPLICA sync started
16408:S 03 Aug 2021 21:37:58.440 * Non blocking connect for SYNC fired the event.
16408:S 03 Aug 2021 21:37:58.440 * Master replied to PING, replication can continue...
16408:S 03 Aug 2021 21:37:58.440 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:13763).
16408:S 03 Aug 2021 21:37:58.440 * Successful partial resynchronization with master.
16408:S 03 Aug 2021 21:37:58.440 # Master replication ID changed to d9897d0cc6810d03551c6e1a29e580ed1ec26242
16408:S 03 Aug 2021 21:37:58.440 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16408:S 03 Aug 2021 21:57:00.296 # Connection with master lost.
16408:S 03 Aug 2021 21:57:00.296 * Caching the disconnected master state.
16408:S 03 Aug 2021 21:57:00.296 * Reconnecting to MASTER ::1:6380
16408:S 03 Aug 2021 21:57:00.297 * MASTER <-> REPLICA sync started
16408:S 03 Aug 2021 21:57:00.297 * Non blocking connect for SYNC fired the event.
16408:S 03 Aug 2021 21:57:00.298 * Master replied to PING, replication can continue...
16408:S 03 Aug 2021 21:57:00.298 * Trying a partial resynchronization (request d9897d0cc6810d03551c6e1a29e580ed1ec26242:14267).
16408:S 03 Aug 2021 21:57:00.299 * Successful partial resynchronization with master.
16408:S 03 Aug 2021 21:57:00.299 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.


```

New Primary which was a Replica previously

```bash
karuppiahn-a01:~ karuppiahn$ redis-server -p 6380

*** FATAL CONFIG FILE ERROR (Redis 6.2.5) ***
Reading the configuration file, at line 2
>>> '"-p" "6380"'
Bad directive or wrong number of arguments
karuppiahn-a01:~ karuppiahn$ redis-server -h
Usage: ./redis-server [/path/to/redis.conf] [options] [-]
       ./redis-server - (read config from stdin)
       ./redis-server -v or --version
       ./redis-server -h or --help
       ./redis-server --test-memory <megabytes>

Examples:
       ./redis-server (run the server with default conf)
       ./redis-server /etc/redis/6379.conf
       ./redis-server --port 7777
       ./redis-server --port 7777 --replicaof 127.0.0.1 8888
       ./redis-server /etc/myredis.conf --loglevel verbose -
       ./redis-server /etc/myredis.conf --loglevel verbose

Sentinel mode:
       ./redis-server /etc/sentinel.conf --sentinel
karuppiahn-a01:~ karuppiahn$ redis-server --port 6380
16991:C 03 Aug 2021 14:53:34.008 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
16991:C 03 Aug 2021 14:53:34.008 # Redis version=6.2.5, bits=64, commit=00000000, modified=0, pid=16991, just started
16991:C 03 Aug 2021 14:53:34.008 # Configuration loaded
16991:M 03 Aug 2021 14:53:34.009 * Increased maximum number of open files to 10032 (it was originally set to 2560).
16991:M 03 Aug 2021 14:53:34.009 * monotonic clock: POSIX clock_gettime
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 6.2.5 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                  
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: 6380
 |    `-._   `._    /     _.-'    |     PID: 16991
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           https://redis.io       
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

16991:M 03 Aug 2021 14:53:34.010 # Server initialized
16991:M 03 Aug 2021 14:53:34.010 * Loading RDB produced by version 6.2.5
16991:M 03 Aug 2021 14:53:34.010 * RDB age 135 seconds
16991:M 03 Aug 2021 14:53:34.010 * RDB memory usage when created 0.98 Mb
16991:M 03 Aug 2021 14:53:34.010 * DB loaded from disk: 0.000 seconds
16991:M 03 Aug 2021 14:53:34.010 * Ready to accept connections
16991:S 03 Aug 2021 14:54:57.188 * Before turning into a replica, using my own master parameters to synthesize a cached master: I may be able to synchronize with the new master with just a partial transfer.
16991:S 03 Aug 2021 14:54:57.188 * Connecting to MASTER localhost:6379
16991:S 03 Aug 2021 14:54:57.194 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 14:54:57.194 * REPLICAOF localhost:6379 enabled (user request from 'id=3 addr=127.0.0.1:49694 laddr=127.0.0.1:6380 fd=8 name= age=57 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=44 qbuf-free=65486 argv-mem=22 obl=0 oll=0 omem=0 tot-mem=82998 events=r cmd=replicaof user=default redir=-1')
16991:S 03 Aug 2021 14:54:57.194 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 14:54:57.194 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 14:54:57.194 * Trying a partial resynchronization (request f8e5a3ce0cc56c1dae31edf595eff12c987d9de0:1).
16991:S 03 Aug 2021 14:54:57.195 * Full resync from master: 67e88ce14822ac26e68a80f6bb3055b302d300d7:0
16991:S 03 Aug 2021 14:54:57.195 * Discarding previously cached master state.
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: receiving 319 bytes from master to disk
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: Flushing old data
16991:S 03 Aug 2021 14:54:57.248 * MASTER <-> REPLICA sync: Loading DB in memory
16991:S 03 Aug 2021 14:54:57.249 * Loading RDB produced by version 6.2.5
16991:S 03 Aug 2021 14:54:57.249 * RDB age 0 seconds
16991:S 03 Aug 2021 14:54:57.249 * RDB memory usage when created 2.08 Mb
16991:S 03 Aug 2021 14:54:57.249 * MASTER <-> REPLICA sync: Finished with success
16991:S 03 Aug 2021 15:36:05.794 # Connection with master lost.
16991:S 03 Aug 2021 15:36:05.794 * Caching the disconnected master state.
16991:S 03 Aug 2021 15:36:05.795 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 15:36:05.796 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 15:36:05.796 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 15:36:05.797 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 15:36:05.797 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:1527).
16991:S 03 Aug 2021 15:36:05.798 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 15:36:05.798 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 16:02:09.750 # MASTER timeout: no data nor PING received...
16991:S 03 Aug 2021 16:02:09.751 # Connection with master lost.
16991:S 03 Aug 2021 16:02:09.751 * Caching the disconnected master state.
16991:S 03 Aug 2021 16:02:09.751 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 16:02:09.752 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 16:02:09.752 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 16:02:09.753 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 16:02:09.753 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:3501).
16991:S 03 Aug 2021 16:02:09.753 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 16:02:09.754 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 16:52:43.840 # Connection with master lost.
16991:S 03 Aug 2021 16:52:43.840 * Caching the disconnected master state.
16991:S 03 Aug 2021 16:52:43.840 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 16:52:43.841 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 16:52:43.842 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 16:52:43.842 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 16:52:43.842 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:5601).
16991:S 03 Aug 2021 16:52:43.843 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 16:52:43.843 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 20:04:24.156 # Connection with master lost.
16991:S 03 Aug 2021 20:04:24.156 * Caching the disconnected master state.
16991:S 03 Aug 2021 20:04:24.156 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 20:04:24.158 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 20:04:24.158 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 20:04:24.159 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 20:04:24.159 * Trying a partial resynchronization (request 67e88ce14822ac26e68a80f6bb3055b302d300d7:5685).
16991:S 03 Aug 2021 20:04:24.159 * Successful partial resynchronization with master.
16991:S 03 Aug 2021 20:04:24.159 * MASTER <-> REPLICA sync: Master accepted a Partial Resynchronization.
16991:S 03 Aug 2021 21:25:11.502 * 1 changes in 3600 seconds. Saving...
16991:S 03 Aug 2021 21:25:11.503 * Background saving started by pid 43787
43787:C 03 Aug 2021 21:25:11.504 * DB saved on disk
16991:S 03 Aug 2021 21:25:11.605 * Background saving terminated with success
16991:S 03 Aug 2021 21:37:58.439 # Connection with master lost.
16991:S 03 Aug 2021 21:37:58.439 * Caching the disconnected master state.
16991:S 03 Aug 2021 21:37:58.439 * Reconnecting to MASTER localhost:6379
16991:S 03 Aug 2021 21:37:58.440 * MASTER <-> REPLICA sync started
16991:S 03 Aug 2021 21:37:58.440 * Non blocking connect for SYNC fired the event.
16991:S 03 Aug 2021 21:37:58.440 * Master replied to PING, replication can continue...
16991:S 03 Aug 2021 21:37:58.440 # Failover request received for replid 67e88ce14822ac26e68a80f6bb3055b302d300d7.
16991:M 03 Aug 2021 21:37:58.440 * Discarding previously cached master state.
16991:M 03 Aug 2021 21:37:58.440 # Setting secondary replication ID to 67e88ce14822ac26e68a80f6bb3055b302d300d7, valid up to offset: 13763. New replication ID is d9897d0cc6810d03551c6e1a29e580ed1ec26242
16991:M 03 Aug 2021 21:37:58.440 * MASTER MODE enabled (failover request from 'id=6 addr=[::1]:53719 laddr=[::1]:6380 fd=12 name= age=0 idle=0 flags=N db=0 sub=0 psub=0 multi=-1 qbuf=87 qbuf-free=65443 argv-mem=58 obl=0 oll=0 omem=0 tot-mem=83034 events=r cmd=psync user=default redir=-1')
16991:M 03 Aug 2021 21:37:58.440 * Replica [::1]:6379 asks for synchronization
16991:M 03 Aug 2021 21:37:58.440 * Partial resynchronization request from [::1]:6379 accepted. Sending 0 bytes of backlog starting from offset 13763.
16991:M 03 Aug 2021 21:57:00.296 # Disconnecting timedout replica (streaming sync): [::1]:6379
16991:M 03 Aug 2021 21:57:00.296 # Connection with replica [::1]:6379 lost.
16991:M 03 Aug 2021 21:57:00.298 * Replica [::1]:6379 asks for synchronization
16991:M 03 Aug 2021 21:57:00.298 * Partial resynchronization request from [::1]:6379 accepted. Sending 0 bytes of backlog starting from offset 14267.


```

Old Primary which is now Replica - CLI -

```bash
karuppiahn-a01:~ karuppiahn$ redis-cli
127.0.0.1:6379> info replication
# Replication
role:slave
master_host:::1
master_port:6380
master_link_status:up
master_last_io_seconds_ago:3
master_sync_in_progress:0
slave_repl_offset:15260
slave_priority:100
slave_read_only:1
replica_announced:1
connected_slaves:0
master_failover_state:no-failover
master_replid:d9897d0cc6810d03551c6e1a29e580ed1ec26242
master_replid2:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_repl_offset:15260
second_repl_offset:13763
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:15260
127.0.0.1:6379> 
```

New Primary which was a Replica previously

```bash
karuppiahn-a01:~ karuppiahn$ redis-cli -h localhost -p 6380
localhost:6380> info replication
# Replication
role:master
connected_slaves:1
slave0:ip=::1,port=6379,state=online,offset=15274,lag=0
master_failover_state:no-failover
master_replid:d9897d0cc6810d03551c6e1a29e580ed1ec26242
master_replid2:67e88ce14822ac26e68a80f6bb3055b302d300d7
master_repl_offset:15274
second_repl_offset:13763
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:15274
localhost:6380> 
```

Notice how the replication ID changed in the primary / master. The new ID is -

`master_replid:d9897d0cc6810d03551c6e1a29e580ed1ec26242`

The ID of the old primary has become a secondary ID now, more like an old ID now -

`master_replid2:67e88ce14822ac26e68a80f6bb3055b302d300d7`

Interesting! This is what I read about in the https://redis.io/topics/replication page, this old primary's replication ID is important because when replicas point to the new primary, they will try to check how much data they need to get to catch up with the latest information, and for this they exchange the replication ID they remember along with the offset. The replication ID they remember is what they get from the old primary initially during the handshake. If the new primary doesn't have this old replication ID, then replicas will unnecessarily start the replication from the start. Instead now since the new primary has the old replication ID, when replicas send replication ID, new primary can check it's replication ID and also it's old / secondary replication ID and match with it to understand how far behind the replicas are. If the replicas are too far behind - meaning very old replication ID which is not there in the primary - it's main and secondary replication ID, then I guess full synchronization happens. If it's just a matter of some offset difference with replication ID matching, then only a partial synchronization is needed which is way faster


