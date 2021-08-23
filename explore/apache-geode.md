https://duckduckgo.com/?t=ffab&q=redis+geode&ia=web

https://db-engines.com/en/system/Geode%3bRedis

http://geode.apache.org/docs/guide/19/tools_modules/redis_adapter.html

https://cwiki.apache.org/confluence/display/GEODE/Index#Index-Geodein5minutesGeodein5minutes

https://formulae.brew.sh/formula/apache-geode

https://github.com/apache/geode

https://github.com/apache/geode/releases

```bash
redis-stuff $ code .
redis-stuff $ java -version
The operation couldn’t be completed. Unable to locate a Java Runtime.
Please visit http://www.java.com for information on installing Java.

redis-stuff $ brew install apache-geode
Updating Homebrew...
==> Auto-updated Homebrew!
Updated Homebrew from 653aa4aa9 to d14fc2db1.
Updated 2 taps (homebrew/core and homebrew/cask).
==> New Formulae
cargo-bloat            fst                    ghostunnel             h2c                    reproc
==> Updated Formulae
Updated 189 formulae.
==> New Casks
blockbench                             mimestream                             mweb-pro
==> Updated Casks
Updated 86 casks.
==> Deleted Casks
agfeo-dashboard                        instasizer                             qtum
axe-electrum                           jabt-flow                              qyooo
colormunki-photo                       jidusm                                 rubitrack-pro
dnagedcom                              mweb                                   s3stat-setup
dragthing                              noraswitch                             scrooo
finisher-fluxx                         open-ecard                             stageplotpro
finisher-micro                         pastor                                 suuntodm5
finisher-neo                           pktriot                                thetube
fluxcenter                             plecs-standalone                       unity-appletv-support-for-editor
fm3-edit                               pomolectron                            unity-linux-il2cpp-support-for-editor
foxglove-studio                        privatus                               unity-macos-il2cpp-support-for-editor
instant-articles-builder               pro-fit                                wanna


==> Homebrew was updated to version 3.2.9
The changelog can be found at:
  https://github.com/Homebrew/brew/releases/tag/3.2.9
==> Downloading https://ghcr.io/v2/homebrew/core/openjdk/11/manifests/11.0.12
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/openjdk/11/blobs/sha256:2de8af552742c3caa4d19fa15f6c39c771c20684c0af
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:2de8af552742c3caa4d19fa15f6c39c7
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/apache-geode/manifests/1.13.4
######################################################################## 100.0%
==> Downloading https://ghcr.io/v2/homebrew/core/apache-geode/blobs/sha256:3798960b4ff3d88ed5cf1be5d4ee03c7fdffa66d24
==> Downloading from https://pkg-containers.githubusercontent.com/ghcr1/blobs/sha256:3798960b4ff3d88ed5cf1be5d4ee03c7
######################################################################## 100.0%
==> Installing dependencies for apache-geode: openjdk@11
==> Installing apache-geode dependency: openjdk@11
==> Pouring openjdk@11--11.0.12.big_sur.bottle.tar.gz
🍺  /usr/local/Cellar/openjdk@11/11.0.12: 679 files, 297.9MB
==> Installing apache-geode
==> Pouring apache-geode--1.13.4.all.bottle.tar.gz
==> Caveats
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
==> Summary
🍺  /usr/local/Cellar/apache-geode/1.13.4: 1,094 files, 155.5MB
==> Caveats
==> apache-geode
Bash completion has been installed to:
  /usr/local/etc/bash_completion.d
redis-stuff $ 
```

---

https://geode.apache.org/

https://geode.apache.org/community/#live

https://www.youtube.com/user/PivotalOpenSourceHub

https://www.youtube.com/playlist?list=PL62pIycqXx-R6IxZBlFyD_gq1EwT5CGE-

https://cwiki.apache.org/confluence/display/GEODE/FAQ

https://twitter.com/ApacheGeode

https://twitter.com/search?q=%23ApacheGeode%20OR%20Apache%20Geode

---

I just tried geode. Specifically Geode with Redis adapter! ;) I didn't read much but I tried it out just by following commands

```bash
~ $ gfsh 
    _________________________     __
   / _____/ ______/ ______/ /____/ /
  / /  __/ /___  /_____  / _____  / 
 / /__/ / ____/  _____/ / /    / /  
/______/_/      /______/_/    /_/    1.13.4

Monitor and Manage Apache Geode
gfsh>start locator
Starting a Geode Locator in /Users/karuppiahn/use-important-pan...
.......................
Locator in /Users/karuppiahn/use-important-pan on 192.168.1.3[10334] as use-important-pan is currently online.
Process ID: 46345
Uptime: 13 seconds
Geode Version: 1.13.4
Java Version: 11.0.12
Log File: /Users/karuppiahn/use-important-pan/use-important-pan.log
JVM Arguments: -Dgemfire.enable-cluster-configuration=true -Dgemfire.load-cluster-configuration-from-dir=false -Dgemfire.launcher.registerSignalHandlers=true -Djava.awt.headless=true -Dsun.rmi.dgc.server.gcInterval=9223372036854775806
Class-Path: /usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-core-1.13.4.jar:/usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-dependencies.jar

Successfully connected to: JMX Manager [host=192.168.1.3, port=1099]

Cluster configuration service is up and running.

gfsh>start server
Starting a Geode Server in /Users/karuppiahn/itch-jolly-feet...
......
Server in /Users/karuppiahn/itch-jolly-feet on 192.168.1.3[40404] as itch-jolly-feet is currently online.
Process ID: 46769
Uptime: 5 seconds
Geode Version: 1.13.4
Java Version: 11.0.12
Log File: /Users/karuppiahn/itch-jolly-feet/itch-jolly-feet.log
JVM Arguments: -Dgemfire.default.locators=192.168.1.3[10334] -Dgemfire.start-dev-rest-api=false -Dgemfire.use-cluster-configuration=true -Dgemfire.launcher.registerSignalHandlers=true -Djava.awt.headless=true -Dsun.rmi.dgc.server.gcInterval=9223372036854775806
Class-Path: /usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-core-1.13.4.jar:/usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-dependencies.jar

gfsh>create region --name=hello --type=REPLICATE
    Member      | Status | Message
--------------- | ------ | --------------------------------------------
itch-jolly-feet | OK     | Region "/hello" created on "itch-jolly-feet"

Cluster configuration for group 'cluster' is updated.

gfsh>?
Command '?' not found (for assistance press TAB)
gfsh>help
alter async-event-queue (Available)
    alter attributes of async-event-queue, needs rolling restart for new attributes to take effect. 
alter disk-store (Available)
    Alter some options for a region or remove a region in an offline disk store.
alter query-service (Available)
    Alter configuration parameters for the query service
alter region (Available)
    Alter a region with the given path and configuration.
alter runtime (Available)
    Alter a subset of member or members configuration properties while running.
backup disk-store (Available)
    Perform a backup on all members with persistent data. The target directory must exist on all members, but can be
    either local or shared. This command can safely be executed on active members and is strongly recommended over
    copying files via operating system commands.
change loglevel (Available)
    This command changes log-level run time on specified servers.
clear defined indexes (Available)
    Clears all the defined indexes.
close durable-client (Available)
    Attempts to close the durable client, the client must be disconnected.
close durable-cq (Available)
    Closes the durable cq registered by the durable client and drains events held for the durable cq from the
    subscription queue.
compact disk-store (Available)
    Compact a disk store on all members with that disk store. This command uses the compaction threshold that each
    member has configured for its disk stores. The disk store must have "allow-force-compaction" set to true.
compact offline-disk-store (Available)
    Compact an offline disk store. If the disk store is large, additional memory may need to be allocated to the
    process using the --J=-Xmx??? parameter.
configure pdx (Available)
    Configures Geode's Portable Data eXchange for all the cache(s) in the cluster. This command would not take
    effect on the running members in the system.
     This command persists the pdx configuration in the locator with cluster configuration service. 
     This command should be issued before starting any data members.
connect (Available)
    Connect to a jmx-manager either directly or via a Locator. If connecting via a Locator, and a jmx-manager
    doesn't already exist, the Locator will start one.
create async-event-queue (Available)
    Create Async Event Queue.
create data-source (Available)
    (Experimental) Creates a JDBC data source and verifies connectivity to an external JDBC database.
create defined indexes (Available)
    Creates all the defined indexes.
create disk-store (Available)
    Create a disk store.
create gateway-receiver (Available)
    Create the Gateway Receiver on a member or members.
create gateway-sender (Available)
    Create the Gateway Sender on a member or members.
create index (Available)
    Create an index that can be used when executing queries.
create jdbc-mapping (Available)
    (Experimental) Create a JDBC mapping for a region for use with a JDBC database.
create jndi-binding (Available)
    Create a jndi binding that holds the configuration for the XA datasource.
create lucene index (Available)
    Create a lucene index that can be used to execute queries.
create region (Available)
    Create a region with the given path and configuration. Specifying a --key-constraint and --value-constraint
    makes object type information available during querying and indexing.
debug (Available)
    Enable/Disable debugging output in GFSH.
define index (Available)
    Define an index that can be used when executing queries.
deploy (Available)
    Deploy JARs to a member or members.  Only one of either --jar or --dir may be specified.
deregister driver (Available)
    (Experimental) Deregister a driver with the cluster's Driver Manager using the name of a driver class contained
    within a currenly deployed jar.
describe client (Available)
    Display details of specified client
describe config (Available)
    Display configuration details of a member or members.
describe connection (Available)
    Display information about the current connection.
describe data-source (Available)
    (Experimental) Describe the configuration of the given data source.
describe disk-store (Available)
    Display information about a member's disk store.
describe jdbc-mapping (Available)
    (Experimental) Describe the specified JDBC mapping
describe jndi-binding (Available)
    Describe the configuration of the given jndi binding.
describe lucene index (Available)
    Display the description of lucene indexes created for all members.
describe member (Available)
    Display information about a member, including name, id, groups, regions, etc.
describe offline-disk-store (Available)
    Display information about an offline disk store.
describe query-service (Available)
    Describes the clusters query service
describe region (Available)
    Display the attributes and key information of a region.
destroy async-event-queue (Available)
    destroy an Async Event Queue
destroy data-source (Available)
    Destroy a data source that holds a jdbc configuration.
destroy disk-store (Available)
    Destroy a disk store, including deleting all files on disk used by the disk store. Data for closed regions
    previously using the disk store will be lost.
destroy function (Available)
    Destroy/Unregister a function. The default is for the function to be unregistered from all members.
destroy gateway-receiver (Available)
    Destroy the Gateway Receiver on a member or members.
destroy gateway-sender (Available)
    Destroy the Gateway Sender on a member or members.
destroy index (Available)
    Destroy/Remove the specified index.
destroy jdbc-mapping (Available)
    (Experimental) Destroy the specified JDBC mapping.
destroy jndi-binding (Available)
    Destroy a JNDI binding that holds the configuration for an XA datasource.
destroy lucene index (Available)
    Destroy the lucene index.
destroy region (Available)
    Destroy/Remove a region.
disconnect (Available)
    Close the current connection, if one is open.
echo (Available)
    Echo the given text which may include system and user variables.
execute function (Available)
    Execute the function with the specified ID. By default will execute on all members.
exit (Available)
    Exit GFSH and return control back to the calling process.
export cluster-configuration (Available)
    Exports the cluster configuration artifacts as a zip file.
export config (Available)
    Export configuration properties for a member or members.
export data (Available)
    Export user data from a region to a file.
export logs (Available)
    Export the log files for a member or members.
export offline-disk-store (Available)
    Export region data from an offline disk store into Geode snapshot files.
export stack-traces (Available)
    Export the stack trace for a member or members.
gc (Available)
    Force GC (Garbage Collection) on a member or members. The default is for garbage collection to occur on all
    caching members.
get (Available)
    Display an entry in a region. If using a region whose key and value classes have been set, then specifying
    --key-class and --value-class is unnecessary.
help (Available)
    Display syntax and usage information for all commands or list all available commands if <command> isn't
    specified.
hint (Available)
    Provide hints for a topic or list all available topics if "topic" isn't specified.
history (Available)
    Display or export previously executed GFSH commands.
import cluster-configuration (Available)
    Imports configuration into cluster configuration hosted at the locators
import data (Available)
    Import user data from a file to a region.
list async-event-queues (Available)
    Display the Async Event Queues for all members.
list clients (Available)
    Display list of connected clients
list data-source (Available)
    (Experimental) List each existing data source.
list deployed (Available)
    Display a list of JARs that were deployed to members using the "deploy" command.
list disk-stores (Available)
    Display disk stores for all members.
list drivers (Available)
    (Experimental) Lists all drivers currently registered by the cluster's Driver Manager.
list durable-cqs (Available)
    List durable client cqs associated with the specified durable client id.
list functions (Available)
    Display a list of registered functions. The default is to display functions for all members.
list gateways (Available)
    Display the Gateway Senders and Receivers for a member or members.
list indexes (Available)
    Display the list of indexes created for all members.
list jdbc-mappings (Available)
    (Experimental) Display JDBC mappings for all members.
list jndi-binding (Available)
    List all jndi bindings, active and configured. An active binding is one that is bound to the server's jndi
    context (and also listed in the cluster config). A configured binding is one that is listed in the cluster
    config, but may not be active on the servers.
list lucene indexes (Available)
    Display the list of lucene indexes created for all members.
list members (Available)
    Display all or a subset of members.
list regions (Available)
    Display regions of a member or members.
load-balance gateway-sender (Available)
    Cause the Gateway Sender to close its current connections so that it reconnects to its remote receivers in a
    more balanced fashion.
locate entry (Available)
    Identifies the location, including host, member and region, of entries that have the specified key.
netstat (Available)
    Report network information and statistics via the "netstat" operating system command.
pause gateway-sender (Available)
    Pause the Gateway Sender on a member or members.
pdx rename (Available)
    Renames PDX types in an offline disk store. 
     Any pdx types that are renamed will be listed in the output. 
     If no renames are done or the disk-store is online then this command will fail.
put (Available)
    Add/Update an entry in a region. If using a region whose key and value classes have been set, then specifying
    --key-class and --value-class is unnecessary.
query (Available)
    Run the specified OQL query as a single quoted string and display the results in one or more pages. Limit will
    default to the value stored in the "APP_FETCH_SIZE" variable. Page size will default to the value stored in the
    "APP_COLLECTION_LIMIT" variable.
exit (Available)
    Exit GFSH and return control back to the calling process.
rebalance (Available)
    Rebalance partitioned regions. The default is for all partitioned regions to be rebalanced.
register driver (Available)
    (Experimental) Register a driver with the cluster's Driver Manager using the name of a driver class contained
    within a currenly deployed jar.
remove (Available)
    Remove an entry from a region. If using a region whose key class has been set, then specifying --key-class is
    unnecessary.
restore redundancy (Available)
    Restore redundancy and optionally reassign primary bucket hosting for partitioned regions in connected members.
    The default is for all regions to have redundancy restored and for primary buckets to be reassigned for better
    load balance.
resume async-event-queue-dispatcher (Available)
    Resume the processing of the events in the Async Event Queue on a member or members.
resume gateway-sender (Available)
    Resume the Gateway Sender on a member or members.
revoke missing-disk-store (Available)
    Instructs the member(s) of a distributed system to stop waiting for a disk store to be available. Only revoke a
    disk store if its files are lost as it will no longer be recoverable once revoking is initiated. Use the "show
    missing-disk-store" command to get descriptions of missing disk stores.
run (Available)
    Execute a set of GFSH commands. Commands that normally prompt for additional input will instead use default
    values.
search lucene (Available)
    Search lucene index
set variable (Available)
    Set GFSH variables that can be used by commands. For example: if variable "CACHE_SERVERS_GROUP" is set then to
    use it with "list members", use "list members --group=${CACHE_SERVERS_GROUP}". The "echo" command can be used to
    know the value of a variable.
sh (Available)
    Allows execution of operating system (OS) commands. Use '&' to return to gfsh prompt immediately. NOTE: Commands
    which pass output to another shell command are not currently supported.
show dead-locks (Available)
    Display any deadlocks in the Geode distributed system.
show log (Available)
    Display the log for a member.
show metrics (Available)
    Display or export metrics for the entire distributed system, a member or a region.
show missing-disk-stores (Available)
    Display a summary of the disk stores that are currently missing from a distributed system.
show subscription-queue-size (Available)
    Shows the number of events in the subscription queue.  If a cq name is provided, counts the number of events in
    the subscription queue for the specified cq.
shutdown (Available)
    Stop all members.
sleep (Available)
    Delay for a specified amount of time in seconds - floating point values are allowed.
start gateway-receiver (Available)
    Start the Gateway Receiver on a member or members.
start gateway-sender (Available)
    Start the Gateway Sender on a member or members.
start jconsole (Available)
    Start the JDK's JConsole tool in a separate process. JConsole will be launched, but connecting to Geode must be
    done manually.
start jvisualvm (Available)
    Start the JDK's Java VisualVM (jvisualvm) tool in a separate process. Java VisualVM will be launched, but
    connecting to Geode must be done manually.
start locator (Available)
    Start a Locator.
start pulse (Available)
    Open a new window in the default Web browser with the URL for the Pulse application.
start server (Available)
    Start a Geode Cache Server.
start vsd (Available)
    Start VSD in a separate process.
status cluster-config-service (Available)
    Displays the status of cluster configuration service on all the locators with enable-cluster-configuration set
    to true.
status gateway-receiver (Available)
    Display the status of a Gateway Receiver.
status gateway-sender (Available)
    Display the status of a Gateway Sender.
status locator (Available)
    Display the status of a Locator. Possible statuses are: started, online, offline or not responding.
status redundancy (Available)
    Report the redundancy status for partitioned regions in connected members. The default is to report status for
    all regions.
status server (Available)
    Display the status of a Geode Cache Server.
stop gateway-receiver (Available)
    Stop the Gateway Receiver on a member or members.
stop gateway-sender (Available)
    Stop the Gateway Sender on a member or members.
stop locator (Available)
    Stop a Locator.
stop server (Available)
    Stop a Geode Cache Server.
undeploy (Available)
    Undeploy JARs from a member or members.
upgrade offline-disk-store (Available)
    Upgrade an offline disk store. If the disk store is large, additional memory may need to be allocated to the
    process using the --J=-Xmx??? parameter.
validate offline-disk-store (Available)
    Scan the contents of a disk store to verify that it has no errors.
version (Available)
    Display product version information.


gfsh>stop server
Server in /Users/karuppiahn on 192.168.1.3[40404] is currently not responding.

gfsh>stop server
Server in /Users/karuppiahn on 192.168.1.3[40404] is currently not responding.

gfsh>shutdown
As a lot of data in memory will be lost, including possibly events in queues, do you really want to shutdown the entire distributed system? (Y/n): y
Shutdown is triggered

gfsh>shutdown
As a lot of data in memory will be lost, including possibly events in queues, do you really want to shutdown the entire distributed system? (Y/n): y
No data node found for stopping. Please specify --include-locators option if you want locators to be stopped

gfsh>shutdown --include-locators
As a lot of data in memory will be lost, including possibly events in queues, do you really want to shutdown the entire distributed system? (Y/n): y
Shutdown is triggered

gfsh>
No longer connected to 192.168.1.3[1099].
gfsh>list regions
Command 'list regions' was found but is not currently available (type 'help' then ENTER to learn about this command)
gfsh>list members
Command 'list members' was found but is not currently available (type 'help' then ENTER to learn about this command)
gfsh>
Exiting... 
~ $ gfsh 
    _________________________     __
   / _____/ ______/ ______/ /____/ /
  / /  __/ /___  /_____  / _____  / 
 / /__/ / ____/  _____/ / /    / /  
/______/_/      /______/_/    /_/    1.13.4

Monitor and Manage Apache Geode
gfsh>start locator
Starting a Geode Locator in /Users/karuppiahn/call-delightful-bun...
.....................
Locator in /Users/karuppiahn/call-delightful-bun on 192.168.1.3[10334] as call-delightful-bun is currently online.
Process ID: 48286
Uptime: 12 seconds
Geode Version: 1.13.4
Java Version: 11.0.12
Log File: /Users/karuppiahn/call-delightful-bun/call-delightful-bun.log
JVM Arguments: -Dgemfire.enable-cluster-configuration=true -Dgemfire.load-cluster-configuration-from-dir=false -Dgemfire.launcher.registerSignalHandlers=true -Djava.awt.headless=true -Dsun.rmi.dgc.server.gcInterval=9223372036854775806
Class-Path: /usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-core-1.13.4.jar:/usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-dependencies.jar

Successfully connected to: JMX Manager [host=192.168.1.3, port=1099]

Cluster configuration service is up and running.

gfsh>start server --name=server1 --redis-bind-address=localhost \
ION_PERSISTENT=11211 --J=-Dgemfireredis.regiontype=PARTIT 
Starting a Geode Server in /Users/karuppiahn/server1...
.......
Server in /Users/karuppiahn/server1 on 192.168.1.3[40404] as server1 is currently online.
Process ID: 48378
Uptime: 4 seconds
Geode Version: 1.13.4
Java Version: 11.0.12
Log File: /Users/karuppiahn/server1/server1.log
JVM Arguments: -Dgemfire.default.locators=192.168.1.3[10334] -Dgemfire.start-dev-rest-api=false -Dgemfire.redis-bind-address=localhost -Dgemfire.use-cluster-configuration=true -Dgemfire.redis-port=11211 -Dgemfireredis.regiontype=PARTITION_PERSISTENT -Dgemfire.launcher.registerSignalHandlers=true -Djava.awt.headless=true -Dsun.rmi.dgc.server.gcInterval=9223372036854775806
Class-Path: /usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-core-1.13.4.jar:/usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-dependencies.jar

gfsh>
Exiting... 
~ $ 
```

```bash
Last login: Mon Aug 23 22:31:40 on ttys004
~ $ redis-cli -p 11211
127.0.0.1:11211> ping
PONG
127.0.0.1:11211> keys *
1) "ReDiS_SET"
2) "ReDiS_HASH"
127.0.0.1:11211> dbsize
(integer) 2
127.0.0.1:11211> get ReDiS_SET
(error) WRONGTYPE The key name "ReDiS_SET" is protected
127.0.0.1:11211> type ReDiS_SET
"protected"
127.0.0.1:11211> type ReDiS_HASH
"protected"
127.0.0.1:11211> set food is-good
OK
127.0.0.1:11211> get food
"is-good"
127.0.0.1:11211> ping
PONG
127.0.0.1:11211> ping
PONG
127.0.0.1:11211> 
```

```bash
Last login: Mon Aug 23 22:24:28 on ttys001
~ $ ls use-important-pan/
ConfigDiskDir_use-important-pan	locator10334views.log		vf.gf.locator.pid
GemFire_karuppiahn		pulse.log
locator10334view.dat		use-important-pan.log
~ $ ls use-important-pan/
ConfigDiskDir_use-important-pan	locator10334view.dat		pulse.log
GemFire_karuppiahn		locator10334views.log		use-important-pan.log
~ $ ls call-delightful-bun/
ConfigDiskDir_call-delightful-bun	locator10334views.log
GemFire_karuppiahn			pulse.log
call-delightful-bun.log			vf.gf.locator.pid
locator10334view.dat
~ $ ls call-delightful-bun/
ConfigDiskDir_call-delightful-bun	locator10334views.log
GemFire_karuppiahn			pulse.log
call-delightful-bun.log			vf.gf.locator.pid
locator10334view.dat
~ $ ls call-delightful-bun/vf.gf.locator.pid 
call-delightful-bun/vf.gf.locator.pid
~ $ cat call-delightful-bun/vf.gf.locator.pid 
48286~ $ cat call-delightful-bun/vf.gf.locator.pid 
~ $ ps aux | rg $(cat call-delightful-bun/vf.gf.locator.pid)
karuppiahn       49422   0.0  0.0  4265112     12 s002  S+   10:33PM   0:00.00 rg 48286
karuppiahn       48286   0.0  3.0 17144036 1014828 s001  S    10:30PM   0:35.77 /usr/local/Cellar/openjdk@11/11.0.12/libexec/openjdk.jdk/Contents/Home/bin/java -server -classpath /usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-core-1.13.4.jar:/usr/local/Cellar/apache-geode/1.13.4/libexec/lib/geode-dependencies.jar -Dgemfire.enable-cluster-configuration=true -Dgemfire.load-cluster-configuration-from-dir=false -Dgemfire.launcher.registerSignalHandlers=true -Djava.awt.headless=true -Dsun.rmi.dgc.server.gcInterval=9223372036854775806 org.apache.geode.distributed.LocatorLauncher start call-delightful-bun --port=10334
~ $ kill $(cat call-delightful-bun/vf.gf.locator.pid)
~ $ ps aux | rg $(cat call-delightful-bun/vf.gf.locator.pid)
cat: call-delightful-bun/vf.gf.locator.pid: No such file or directory
error: The following required arguments were not provided:
    <PATTERN>

USAGE:
    
    rg [OPTIONS] PATTERN [PATH ...]
    rg [OPTIONS] -e PATTERN ... [PATH ...]
    rg [OPTIONS] -f PATTERNFILE ... [PATH ...]
    rg [OPTIONS] --files [PATH ...]
    rg [OPTIONS] --type-list
    command | rg [OPTIONS] PATTERN
    rg [OPTIONS] --help
    rg [OPTIONS] --version

For more information try --help

~ $ ps aux | rg 48286
karuppiahn       49437   0.0  0.0  4265112    184 s002  R+   10:33PM   0:00.00 rg 48286
~ $ 
```

I wasn't sure if `start locator` was needed or not, haha

I need to understand how the whole Geode management works with `gfsh` and why the name `gfsh` too

Some stuff to checkout - [TODO]

http://geode.apache.org/docs/guide/19/tools_modules/gfsh/about_gfsh.html

https://www.baeldung.com/apache-geode

https://blogs.vmware.com/opensource/2020/04/14/apache-geode-a-quick-history/

Geode like memcached hmm, interesting

http://geode.apache.org/docs/guide/19/tools_modules/gemcached/chapter_overview.html


