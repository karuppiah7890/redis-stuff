I was skimming through the section

I checked out about the different metrics that I had already seen a bit before when using `INFO` command

I had already heard of `MEMORY` and `LATENCY` Redis command too

I need to try some of this stuff!! [TODO]
- `redis-cli --latency`
- `redis-cli --latency --csv`
- `redis-cli --latency-history -i 60`
- `redis-cli --latency-history -i 60 --csv`
- `redis-cli --latency-dist`
- `redis-cli --latency-dist -i 60`
- `redis-cli --stat`
- `redis-cli memory stats`
- `redis-cli LATENCY DOCTOR`

and then read the `Latency Monitoring` section [TODO]

---

```bash
Last login: Sun Aug 22 22:45:54 on ttys000
~ $ redis-cli --latency
min: 0, max: 1, avg: 0.20 (1135 samples)^C
~ $ redis-cli -h
redis-cli 6.2.5

Usage: redis-cli [OPTIONS] [cmd [arg [arg ...]]]
  -h <hostname>      Server hostname (default: 127.0.0.1).
  -p <port>          Server port (default: 6379).
  -s <socket>        Server socket (overrides hostname and port).
  -a <password>      Password to use when connecting to the server.
                     You can also use the REDISCLI_AUTH environment
                     variable to pass this password more safely
                     (if both are used, this argument takes precedence).
  --user <username>  Used to send ACL style 'AUTH username pass'. Needs -a.
  --pass <password>  Alias of -a for consistency with the new --user option.
  --askpass          Force user to input password with mask from STDIN.
                     If this argument is used, '-a' and REDISCLI_AUTH
                     environment variable will be ignored.
  -u <uri>           Server URI.
  -r <repeat>        Execute specified command N times.
  -i <interval>      When -r is used, waits <interval> seconds per command.
                     It is possible to specify sub-second times like -i 0.1.
  -n <db>            Database number.
  -3                 Start session in RESP3 protocol mode.
  -x                 Read last argument from STDIN.
  -d <delimiter>     Delimiter between response bulks for raw formatting (default: \n).
  -D <delimiter>     Delimiter between responses for raw formatting (default: \n).
  -c                 Enable cluster mode (follow -ASK and -MOVED redirections).
  -e                 Return exit error code when command execution fails.
  --tls              Establish a secure TLS connection.
  --sni <host>       Server name indication for TLS.
  --cacert <file>    CA Certificate file to verify with.
  --cacertdir <dir>  Directory where trusted CA certificates are stored.
                     If neither cacert nor cacertdir are specified, the default
                     system-wide trusted root certs configuration will apply.
  --insecure         Allow insecure TLS connection by skipping cert validation.
  --cert <file>      Client certificate to authenticate with.
  --key <file>       Private key file to authenticate with.
  --tls-ciphers <list> Sets the list of prefered ciphers (TLSv1.2 and below)
                     in order of preference from highest to lowest separated by colon (":").
                     See the ciphers(1ssl) manpage for more information about the syntax of this string.
  --tls-ciphersuites <list> Sets the list of prefered ciphersuites (TLSv1.3)
                     in order of preference from highest to lowest separated by colon (":").
                     See the ciphers(1ssl) manpage for more information about the syntax of this string,
                     and specifically for TLSv1.3 ciphersuites.
  --raw              Use raw formatting for replies (default when STDOUT is
                     not a tty).
  --no-raw           Force formatted output even when STDOUT is not a tty.
  --quoted-input     Force input to be handled as quoted strings.
  --csv              Output in CSV format.
  --show-pushes <yn> Whether to print RESP3 PUSH messages.  Enabled by default when
                     STDOUT is a tty but can be overriden with --show-pushes no.
  --stat             Print rolling stats about server: mem, clients, ...
  --latency          Enter a special mode continuously sampling latency.
                     If you use this mode in an interactive session it runs
                     forever displaying real-time stats. Otherwise if --raw or
                     --csv is specified, or if you redirect the output to a non
                     TTY, it samples the latency for 1 second (you can use
                     -i to change the interval), then produces a single output
                     and exits.
  --latency-history  Like --latency but tracking latency changes over time.
                     Default time interval is 15 sec. Change it using -i.
  --latency-dist     Shows latency as a spectrum, requires xterm 256 colors.
                     Default time interval is 1 sec. Change it using -i.
  --lru-test <keys>  Simulate a cache workload with an 80-20 distribution.
  --replica          Simulate a replica showing commands received from the master.
  --rdb <filename>   Transfer an RDB dump from remote server to local file.
                     Use filename of "-" to write to stdout.
  --pipe             Transfer raw Redis protocol from stdin to server.
  --pipe-timeout <n> In --pipe mode, abort with error if after sending all data.
                     no reply is received within <n> seconds.
                     Default timeout: 30. Use 0 to wait forever.
  --bigkeys          Sample Redis keys looking for keys with many elements (complexity).
  --memkeys          Sample Redis keys looking for keys consuming a lot of memory.
  --memkeys-samples <n> Sample Redis keys looking for keys consuming a lot of memory.
                     And define number of key elements to sample
  --hotkeys          Sample Redis keys looking for hot keys.
                     only works when maxmemory-policy is *lfu.
  --scan             List all keys using the SCAN command.
  --pattern <pat>    Keys pattern when using the --scan, --bigkeys or --hotkeys
                     options (default: *).
  --quoted-pattern <pat> Same as --pattern, but the specified string can be
                         quoted, in order to pass an otherwise non binary-safe string.
  --intrinsic-latency <sec> Run a test to measure intrinsic system latency.
                     The test will run for the specified amount of seconds.
  --eval <file>      Send an EVAL command using the Lua script at <file>.
  --ldb              Used with --eval enable the Redis Lua debugger.
  --ldb-sync-mode    Like --ldb but uses the synchronous Lua debugger, in
                     this mode the server is blocked and script changes are
                     not rolled back from the server memory.
  --cluster <command> [args...] [opts...]
                     Cluster Manager command and arguments (see below).
  --verbose          Verbose mode.
  --no-auth-warning  Don\'t show warning message when using password on command
                     line interface.
  --help             Output this help and exit.
  --version          Output version and exit.

Cluster Manager Commands:
  Use --cluster help to list all available cluster manager commands.

Examples:
  cat /etc/passwd | redis-cli -x set mypasswd
  redis-cli get mypasswd
  redis-cli -r 100 lpush mylist x
  redis-cli -r 100 -i 1 info | grep used_memory_human:
  redis-cli --quoted-input set '"null-\x00-separated"' value
  redis-cli --eval myscript.lua key1 key2 , arg1 arg2 arg3
  redis-cli --scan --pattern '*:12345*'

  (Note: when using --eval the comma separates KEYS[] from ARGV[] items)

When no command is given, redis-cli starts in interactive mode.
Type "help" in interactive mode for information on available commands
and settings.

~ $ 
```

For me it showed latency in real time forever, not just one second

```
--latency          Enter a special mode continuously sampling latency.
                     If you use this mode in an interactive session it runs
                     forever displaying real-time stats. Otherwise if --raw or
                     --csv is specified, or if you redirect the output to a non
                     TTY, it samples the latency for 1 second (you can use
                     -i to change the interval), then produces a single output
                     and exits.
```

There's also `--latency-history`

```
--latency-history  Like --latency but tracking latency changes over time.
                     Default time interval is 15 sec. Change it using -i.
```

```bash
~ $ redis-cli --latency --csv
0,1,0.33,86
~ $ redis-cli --latency --csv -i 10

0,1,0.22,856
~ $ 
~ $ redis-cli --latency-history
min: 0, max: 1, avg: 0.21 (1298 samples) -- 15.00 seconds range
min: 0, max: 1, avg: 0.20 (1295 samples) -- 15.01 seconds range
min: 0, max: 1, avg: 0.20 (1287 samples) -- 15.01 seconds range
min: 0, max: 1, avg: 0.23 (283 samples)^C
```

Looks like it's showing a min value, max value and an average, based on the samples. I need to understand exactly what it means. I mean, it looks like it's min - 0 seconds, max - 1 seconds and avg - 0.21 seconds. I'm wondering how it determined the max and the min. Maybe min is too easy, just 0. But idk, I can see in the exercise a min where there's 1 and max field where there's 17, a big value

Latency history shows the values every T interval time, and gets samples within that time T. Hmm. Else it's the values over the whole time given or real time value for the whole time

```bash
~ $ redis-cli --latency-history --csv
1,1,1.00,1
0,1,0.50,2
0,1,0.33,3
0,1,0.25,4
0,1,0.20,5
0,1,0.33,6
0,1,0.29,7
0,1,0.25,8
0,1,0.22,9
0,1,0.30,10
0,1,0.27,11
0,1,0.33,12
0,1,0.31,13
0,1,0.29,14
0,1,0.27,15
0,1,0.25,16
0,1,0.24,17
0,1,0.22,18
0,1,0.21,19
0,1,0.25,20
0,1,0.24,21
0,1,0.23,22
0,1,0.22,23
0,1,0.21,24
0,1,0.20,25
0,1,0.19,26
0,1,0.19,27
0,1,0.18,28
0,1,0.17,29
0,1,0.17,30
0,1,0.16,31
0,1,0.16,32
0,1,0.15,33
0,1,0.15,34
0,1,0.14,35
0,1,0.14,36
0,1,0.16,37
0,1,0.18,38
0,1,0.18,39
0,1,0.17,40
0,1,0.17,41
0,1,0.17,42
0,1,0.16,43
0,1,0.16,44
0,1,0.16,45
0,1,0.15,46
0,1,0.17,47
0,1,0.17,48
0,1,0.18,49
0,1,0.18,50
0,1,0.20,51
0,1,0.19,52
0,1,0.21,53
0,1,0.20,54
0,1,0.20,55
0,1,0.20,56
0,1,0.19,57
0,1,0.21,58
0,1,0.20,59
0,1,0.22,60
0,1,0.21,61
0,1,0.21,62
0,1,0.21,63
0,1,0.20,64
0,1,0.22,65
0,1,0.21,66
0,1,0.21,67
0,1,0.21,68
0,1,0.20,69
0,1,0.20,70
0,1,0.21,71
0,1,0.21,72
0,1,0.21,73
0,1,0.20,74
0,1,0.21,75
0,1,0.22,76
0,1,0.22,77
0,1,0.23,78
0,1,0.23,79
0,1,0.24,80
0,1,0.23,81
0,1,0.23,82
0,1,0.23,83
0,1,0.24,84
0,1,0.24,85
0,1,0.23,86
0,1,0.23,87
0,1,0.23,88
0,1,0.22,89
0,1,0.22,90
0,1,0.22,91
0,1,0.22,92
0,1,0.22,93
0,1,0.21,94
0,1,0.21,95
0,1,0.21,96
0,1,0.21,97
0,1,0.20,98
0,1,0.20,99
0,1,0.20,100
0,1,0.20,101
0,1,0.20,102
0,1,0.19,103
0,1,0.19,104
0,1,0.20,105
0,1,0.20,106
0,1,0.20,107
0,1,0.19,108
0,1,0.20,109
0,1,0.20,110
0,1,0.20,111
0,1,0.20,112
0,1,0.20,113
0,1,0.20,114
0,1,0.20,115
0,1,0.20,116
0,1,0.21,117
0,1,0.20,118
0,1,0.20,119
0,1,0.21,120
0,1,0.21,121
0,1,0.20,122
0,1,0.20,123
0,1,0.20,124
0,1,0.20,125
0,1,0.20,126
0,1,0.20,127
0,1,0.20,128
0,1,0.19,129
0,1,0.19,130
0,1,0.19,131
0,1,0.19,132
0,1,0.19,133
0,1,0.19,134
0,1,0.19,135
0,1,0.19,136
0,1,0.19,137
0,1,0.19,138
0,1,0.19,139
0,1,0.19,140
0,1,0.18,141
0,1,0.18,142
0,1,0.18,143
0,1,0.18,144
0,1,0.18,145
0,1,0.18,146
0,1,0.18,147
0,1,0.18,148
0,1,0.18,149
0,1,0.18,150
0,1,0.18,151
0,1,0.18,152
0,1,0.18,153
0,1,0.18,154
0,1,0.17,155
0,1,0.18,156
0,1,0.18,157
0,1,0.18,158
0,1,0.18,159
0,1,0.17,160
0,1,0.17,161
0,1,0.18,162
0,1,0.18,163
0,1,0.18,164
0,1,0.19,165
0,1,0.19,166
0,1,0.20,167
0,1,0.20,168
0,1,0.20,169
0,1,0.20,170
0,1,0.20,171
0,1,0.21,172
0,1,0.21,173
0,1,0.21,174
0,1,0.21,175
0,1,0.22,176
0,1,0.21,177
0,1,0.21,178
0,1,0.21,179
0,1,0.21,180
0,1,0.21,181
0,1,0.21,182
0,1,0.21,183
0,1,0.21,184
0,1,0.21,185
0,1,0.22,186
0,1,0.21,187
0,1,0.21,188
0,1,0.21,189
0,1,0.21,190
0,1,0.21,191
0,1,0.21,192
0,1,0.21,193
0,1,0.21,194
0,1,0.21,195
0,1,0.21,196
0,1,0.21,197
0,1,0.21,198
0,1,0.21,199
0,1,0.21,200
0,1,0.21,201
0,1,0.21,202
0,1,0.21,203
0,1,0.21,204
0,1,0.21,205
0,1,0.21,206
0,1,0.21,207
0,1,0.21,208
0,1,0.21,209
0,1,0.21,210
0,1,0.21,211
0,1,0.21,212
0,1,0.21,213
0,1,0.21,214
0,1,0.20,215
0,1,0.20,216
0,1,0.21,217
0,1,0.21,218
0,1,0.21,219
0,1,0.21,220
0,1,0.21,221
0,1,0.21,222
0,1,0.21,223
0,1,0.21,224
0,1,0.20,225
0,1,0.20,226
0,1,0.20,227
0,1,0.20,228
0,1,0.20,229
0,1,0.20,230
0,1,0.20,231
0,1,0.20,232
0,1,0.20,233
0,1,0.20,234
0,1,0.20,235
0,1,0.19,236
0,1,0.20,237
0,1,0.20,238
0,1,0.20,239
0,1,0.20,240
0,1,0.20,241
0,1,0.19,242
0,1,0.19,243
0,1,0.20,244
0,1,0.20,245
0,1,0.20,246
0,1,0.20,247
0,1,0.20,248
0,1,0.20,249
0,1,0.20,250
0,1,0.20,251
0,1,0.20,252
0,1,0.20,253
0,1,0.20,254
0,1,0.20,255
0,1,0.20,256
0,1,0.20,257
0,1,0.20,258
0,1,0.20,259
0,1,0.20,260
0,1,0.20,261
0,1,0.20,262
0,1,0.20,263
0,1,0.20,264
0,1,0.20,265
0,1,0.20,266
0,1,0.20,267
0,1,0.20,268
0,1,0.20,269
0,1,0.20,270
0,1,0.20,271
0,1,0.20,272
0,1,0.20,273
0,1,0.20,274
0,1,0.20,275
0,1,0.20,276
0,1,0.20,277
0,1,0.20,278
0,1,0.20,279
0,1,0.20,280
0,1,0.20,281
0,1,0.20,282
0,1,0.19,283
0,1,0.19,284
0,1,0.19,285
0,1,0.19,286
0,1,0.19,287
0,1,0.19,288
0,1,0.19,289
0,1,0.19,290
0,1,0.19,291
0,1,0.19,292
0,1,0.19,293
0,1,0.19,294
0,1,0.19,295
0,1,0.19,296
0,1,0.19,297
0,1,0.19,298
0,1,0.19,299
0,1,0.19,300
0,1,0.19,301
0,1,0.19,302
0,1,0.19,303
0,1,0.19,304
0,1,0.19,305
0,1,0.19,306
0,1,0.19,307
0,1,0.19,308
0,1,0.18,309
0,1,0.19,310
0,1,0.19,311
0,1,0.19,312
0,1,0.19,313
0,1,0.18,314
0,1,0.18,315
0,1,0.18,316
0,1,0.19,317
0,1,0.19,318
0,1,0.19,319
0,1,0.19,320
0,1,0.19,321
0,1,0.19,322
0,1,0.19,323
0,1,0.19,324
0,1,0.19,325
0,1,0.19,326
0,1,0.19,327
0,1,0.19,328
0,1,0.19,329
0,1,0.19,330
0,1,0.19,331
0,1,0.19,332
0,1,0.19,333
0,1,0.19,334
0,1,0.19,335
0,1,0.19,336
0,1,0.19,337
0,1,0.19,338
0,1,0.19,339
0,1,0.19,340
0,1,0.18,341
0,1,0.19,342
0,1,0.19,343
0,1,0.19,344
0,1,0.19,345
0,1,0.18,346
0,1,0.19,347
0,1,0.19,348
0,1,0.19,349
0,1,0.19,350
0,1,0.19,351
0,1,0.19,352
0,1,0.19,353
0,1,0.19,354
0,1,0.19,355
0,1,0.19,356
0,1,0.19,357
0,1,0.19,358
0,1,0.19,359
0,1,0.19,360
0,1,0.19,361
0,1,0.19,362
0,1,0.19,363
0,1,0.19,364
0,1,0.19,365
0,1,0.19,366
0,1,0.19,367
0,1,0.19,368
0,1,0.19,369
0,1,0.19,370
0,1,0.19,371
0,1,0.19,372
0,1,0.19,373
0,1,0.20,374
0,1,0.19,375
0,1,0.19,376
0,1,0.19,377
0,1,0.19,378
0,1,0.19,379
0,1,0.19,380
0,1,0.19,381
0,1,0.19,382
0,1,0.20,383
0,1,0.20,384
0,1,0.19,385
0,1,0.19,386
0,1,0.19,387
0,1,0.19,388
0,1,0.19,389
0,1,0.19,390
0,1,0.19,391
0,1,0.19,392
0,1,0.19,393
0,1,0.19,394
0,1,0.19,395
0,1,0.19,396
0,1,0.19,397
0,1,0.19,398
0,1,0.19,399
0,1,0.19,400
0,1,0.19,401
0,1,0.19,402
0,1,0.19,403
0,1,0.19,404
0,1,0.19,405
0,1,0.19,406
0,1,0.19,407
0,1,0.19,408
0,1,0.19,409
0,1,0.19,410
0,1,0.19,411
0,1,0.19,412
0,1,0.19,413
0,1,0.19,414
0,1,0.19,415
0,1,0.19,416
0,1,0.19,417
0,1,0.19,418
0,1,0.19,419
0,1,0.19,420
0,1,0.19,421
0,1,0.19,422
0,1,0.19,423
0,1,0.19,424
0,1,0.19,425
0,1,0.19,426
0,1,0.19,427
0,1,0.19,428
0,1,0.19,429
0,1,0.19,430
0,1,0.19,431
0,1,0.19,432
0,1,0.19,433
0,1,0.19,434
0,1,0.19,435
0,1,0.19,436
0,1,0.19,437
0,1,0.19,438
0,1,0.19,439
0,1,0.19,440
0,1,0.19,441
0,1,0.19,442
0,1,0.19,443
0,1,0.19,444
0,1,0.19,445
0,1,0.19,446
0,1,0.19,447
0,1,0.19,448
0,1,0.19,449
0,1,0.19,450
0,1,0.19,451
0,1,0.19,452
0,1,0.19,453
0,1,0.19,454
0,1,0.19,455
0,1,0.19,456
0,1,0.19,457
0,1,0.19,458
0,1,0.19,459
0,1,0.19,460
0,1,0.19,461
0,1,0.19,462
0,1,0.19,463
0,1,0.19,464
0,1,0.19,465
0,1,0.19,466
0,1,0.19,467
0,1,0.19,468
0,1,0.19,469
0,1,0.19,470
0,1,0.19,471
0,1,0.19,472
0,1,0.19,473
0,1,0.19,474
0,1,0.19,475
0,1,0.19,476
0,1,0.19,477
0,1,0.19,478
0,1,0.19,479
0,1,0.19,480
0,1,0.19,481
0,1,0.19,482
0,1,0.19,483
0,1,0.19,484
0,1,0.19,485
0,1,0.19,486
0,1,0.19,487
0,1,0.19,488
0,1,0.19,489
0,1,0.19,490
0,1,0.19,491
0,1,0.19,492
0,1,0.19,493
0,1,0.19,494
0,1,0.19,495
0,1,0.19,496
0,1,0.19,497
0,1,0.19,498
0,1,0.19,499
0,1,0.19,500
0,1,0.19,501
0,1,0.19,502
0,1,0.19,503
0,1,0.19,504
0,1,0.19,505
0,1,0.19,506
0,1,0.19,507
0,1,0.19,508
0,1,0.19,509
0,1,0.19,510
0,1,0.19,511
0,1,0.19,512
0,1,0.19,513
0,1,0.19,514
0,1,0.19,515
0,1,0.19,516
0,1,0.19,517
0,1,0.19,518
0,1,0.19,519
0,1,0.19,520
0,1,0.19,521
0,1,0.19,522
0,1,0.19,523
0,1,0.19,524
0,1,0.19,525
0,1,0.19,526
0,1,0.19,527
0,1,0.19,528
0,1,0.19,529
0,1,0.19,530
0,1,0.19,531
0,1,0.19,532
0,1,0.19,533
0,1,0.19,534
0,1,0.19,535
0,1,0.19,536
0,1,0.19,537
0,1,0.19,538
0,1,0.19,539
0,1,0.19,540
0,1,0.19,541
0,1,0.19,542
0,1,0.19,543
0,1,0.19,544
0,1,0.19,545
0,1,0.19,546
0,1,0.19,547
0,1,0.19,548
0,1,0.19,549
0,1,0.19,550
0,1,0.19,551
0,1,0.19,552
0,1,0.19,553
0,1,0.19,554
0,1,0.19,555
0,1,0.19,556
0,1,0.19,557
0,1,0.19,558
0,1,0.19,559
0,1,0.19,560
0,1,0.19,561
0,1,0.19,562
0,1,0.19,563
0,1,0.19,564
0,1,0.19,565
0,1,0.19,566
0,1,0.19,567
0,1,0.19,568
0,1,0.19,569
0,1,0.19,570
0,1,0.19,571
0,1,0.19,572
0,1,0.19,573
0,1,0.19,574
0,1,0.19,575
0,1,0.19,576
0,1,0.19,577
0,1,0.19,578
0,1,0.19,579
0,1,0.19,580
0,1,0.19,581
0,1,0.19,582
0,1,0.19,583
0,1,0.19,584
0,1,0.19,585
0,1,0.19,586
0,1,0.19,587
0,1,0.19,588
0,1,0.19,589
0,1,0.19,590
0,1,0.19,591
0,1,0.19,592
0,1,0.19,593
0,1,0.19,594
0,1,0.19,595
0,1,0.19,596
0,1,0.19,597
0,1,0.19,598
0,1,0.19,599
0,1,0.20,600
0,1,0.20,601
0,1,0.20,602
0,1,0.20,603
0,1,0.20,604
0,1,0.20,605
0,1,0.20,606
0,1,0.20,607
0,1,0.20,608
0,1,0.20,609
0,1,0.20,610
0,1,0.20,611
0,1,0.20,612
0,1,0.20,613
0,1,0.20,614
0,1,0.20,615
0,1,0.20,616
0,1,0.20,617
0,1,0.20,618
0,1,0.20,619
0,1,0.20,620
0,1,0.20,621
0,1,0.20,622
0,1,0.20,623
0,1,0.20,624
0,1,0.20,625
^C
~ $ 
```

```bash
~ $ redis-cli --latency-dist
---------------------------------------------
. - * #          .01 .125 .25 .5 milliseconds
1,2,3,...,9      from 1 to 9     milliseconds
A,B,C,D,E        10,20,30,40,50  milliseconds
F,G,H,I,J        .1,.2,.3,.4,.5       seconds
K,L,M,N,O,P,Q,?  1,2,4,8,16,30,60,>60 seconds
From 0 to 100%:                    
---------------------------------------------
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
---------------------------------------------
. - * #          .01 .125 .25 .5 milliseconds
1,2,3,...,9      from 1 to 9     milliseconds
A,B,C,D,E        10,20,30,40,50  milliseconds
F,G,H,I,J        .1,.2,.3,.4,.5       seconds
K,L,M,N,O,P,Q,?  1,2,4,8,16,30,60,>60 seconds
From 0 to 100%:                    
---------------------------------------------
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
.-*#123456789ABCDEFGHIJKLMNOPQ?
---------------------------------------------
. - * #          .01 .125 .25 .5 milliseconds
1,2,3,...,9      from 1 to 9     milliseconds
A,B,C,D,E        10,20,30,40,50  milliseconds
F,G,H,I,J        .1,.2,.3,.4,.5       seconds
K,L,M,N,O,P,Q,?  1,2,4,8,16,30,60,>60 seconds
From 0 to 100%:                    
---------------------------------------------
.-*#123456789ABCDEFGHIJKLMNOPQ?
^C
~ $ 
```

```bash
~ $ redis-cli --stat
------- data ------ --------------------- load -------------------- - child -
keys       mem      clients blocked requests            connections          
1          1.06M    1       0       10544 (+0)          7           
1          1.06M    1       0       10545 (+1)          7           
1          1.06M    1       0       10546 (+1)          7           
1          1.06M    1       0       10547 (+1)          7           
^C
```

```bash
~ $ redis-cli memory stats
 1) "peak.allocated"
 2) (integer) 1111232
 3) "total.allocated"
 4) (integer) 1109216
 5) "startup.allocated"
 6) (integer) 1025568
 7) "replication.backlog"
 8) (integer) 0
 9) "clients.slaves"
10) (integer) 0
11) "clients.normal"
12) (integer) 0
13) "aof.buffer"
14) (integer) 0
15) "lua.caches"
16) (integer) 0
17) "db.0"
18) 1) "overhead.hashtable.main"
    2) (integer) 72
    3) "overhead.hashtable.expires"
    4) (integer) 32
19) "overhead.total"
20) (integer) 1025672
21) "keys.count"
22) (integer) 1
23) "keys.bytes-per-key"
24) (integer) 83648
25) "dataset.bytes"
26) (integer) 83544
27) "dataset.percentage"
28) "99.87567138671875"
29) "peak.percentage"
30) "99.818580627441406"
31) "allocator.allocated"
32) (integer) 1025728
33) "allocator.active"
34) (integer) 3935232
35) "allocator.resident"
36) (integer) 3935232
37) "allocator-fragmentation.ratio"
38) "3.8365259170532227"
39) "allocator-fragmentation.bytes"
40) (integer) 2909504
41) "allocator-rss.ratio"
42) "1"
43) "allocator-rss.bytes"
44) (integer) 0
45) "rss-overhead.ratio"
46) "1.0096279382705688"
47) "rss-overhead.bytes"
48) (integer) 37888
49) "fragmentation"
50) "3.8734636306762695"
51) "fragmentation.bytes"
52) (integer) 2947392
~ $ 
```

```bash
~ $ redis-cli LATENCY DOCTOR
I'm sorry, Dave, I can't do that. Latency monitoring is disabled in this Redis instance. You may use "CONFIG SET latency-monitor-threshold <milliseconds>." in order to enable it. If we weren't in a deep space mission I'd suggest to take a look at https://redis.io/topics/latency-monitor.
~ $ 
```

```bash
~ $ redis-cli CONFIG SET latency-monitor-threshold 1000
OK
~ $ redis-cli LATENCY DOCTOR
Dave, no latency spike was observed during the lifetime of this Redis instance, not in the slightest bit. I honestly think you ought to sit down calmly, take a stress pill, and think things over.
~ $ redis-cli LATENCY DOCTOR
Dave, no latency spike was observed during the lifetime of this Redis instance, not in the slightest bit. I honestly think you ought to sit down calmly, take a stress pill, and think things over.
~ $ 
```

I enabled the latency monitoring using `CONFIG SET latency-monitor-threshold 1000`

https://redis.io/topics/latency-monitor [TODO]

So, the threshold time that I put as 1000 milliseconds - it's about events that take longer time than that - only those will be logged as latency spikes

Looks like Redis has an elaborate system to capture data for latency analysis, and engines to to report and analyze the data and provide reports. Interesting

```bash
~ $ redis-cli LATENCY LATEST
(empty array)
~ $ redis-cli CONFIG SET latency-monitor-threshold 1
OK
~ $ redis-cli LATENCY LATEST
(empty array)
~ $ redis-cli GET FOOD
(nil)
~ $ redis-cli LATENCY LATEST
(empty array)
~ $ redis-cli SET FOOD
(error) ERR wrong number of arguments for 'set' command
~ $ redis-cli SET FOOD good
OK
~ $ redis-cli GET FOOD
"good"
~ $ redis-cli GET food
(nil)
~ $ redis-cli GET FOOD
"good"
~ $ redis-cli LATENCY LATEST
(empty array)
~ $ redis-cli LATENCY HISTORY
(error) ERR Unknown subcommand or wrong number of arguments for 'HISTORY'. Try LATENCY HELP.
~ $ redis-cli LATENCY HELP
 1) LATENCY <subcommand> [<arg> [value] [opt] ...]. Subcommands are:
 2) DOCTOR
 3)     Return a human readable latency analysis report.
 4) GRAPH <event>
 5)     Return an ASCII latency graph for the <event> class.
 6) HISTORY <event>
 7)     Return time-latency samples for the <event> class.
 8) LATEST
 9)     Return the latest latency samples for all events.
10) RESET [<event> ...]
11)     Reset latency data of one or more <event> classes.
12)     (default: reset all data for all event classes)
13) HELP
14)     Prints this help.
~ $ redis-cli LATENCY GRAPH
(error) ERR Unknown subcommand or wrong number of arguments for 'GRAPH'. Try LATENCY HELP.
~ $ redis-cli LATENCY GRAPH fork
ERR No samples available for event 'fork'
~ $ redis-cli LATENCY HISTORY fork
(empty array)
~ $ redis-cli LATENCY HISTORY command
(empty array)
~ $ redis-cli LATENCY GRAPH command
ERR No samples available for event 'command'
~ $ 
```

There's something called as events and event classes

https://redis.io/commands/latency-history

Some examples of events are `command`, `fork` and what not that's defined in here - https://redis.io/commands/latency-history

Ah, it's also mentioned in the exercise, right

I need to read more about latency from section 5.1 and read more detailed stuff [TODO]. I just skimmed through a lot of inner detail stuff, it's a lot of depth, too many events (aof and what not) and too much data there


