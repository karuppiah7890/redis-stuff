There's a GitHub repo for this

https://github.com/redislabs-training/exercises-scaling-redis

I just finished watching the introduction, it's pretty interesting to know some differences between open source redis and enterprise redis

Looks like there's actually an enterprise redis and an enterprise redis cloud or aka redis cloud. I guess enterprise redis is a self hosted but paid software, unlike open source redis and enterprise redis cloud / redis cloud is more of a SaaS / Database as a Service offering for a managed service - managed Redis service - managed Redis as a Service

Looking at the Redis Server overview - apparently Enterprise Redis can actually make use of all the CPU cores in a single machine, unlike open source Redis which is single threaded and uses only one core, hmm

And some interesting general things to think about when it comes to databases

In a basic interaction between a databases client and a database server, some basic things that happen are

- Server is listening for connections
- Client connects to the server
- Client sends command(s) to the server. This can be any kind of command - generically a read / write. Or one or many of CRUD - Created, Read, Update, Delete
- Server reads the command - parses the command
- Server understands how to execute the command over the data it has
- Server executes the command
- Depending upon the execution - a failure or success happens
- Server sends the response back to the client

The command could also be an invalid one - in multiple ways, like
- Invalid syntax - invalid command name, invalid number of command arguments, invalid type for command arguments, invalid value for command arguments and what not
- Invalid operation based on the data, or say if the databases was a readonly, but the command was a write command, then depending on the database, it will error out or not

Some errors can be caught early - while reading / parsing the command - and looking for invalid syntax. Some errors are harder to catch and only happen when executing

This is a basic interaction between client and server. To scale this, one has to scale a lot of things. More like, one could scale a lot of things

First, for many clients to be able to connect to the server, the server has to have that many open ports / sockets so that there can be communication between the client and the server. So, for example in Linux, one has to check the maximum limit for open files, using something like

```bash
$ ulimit -n
256
```

The server usually uses only one port / socket for listening, and other random ports / sockets for the client communication once the connection is accepted. So, this is pretty important

From what I remember, to communicate in a network, a system needs many things. One among them is a - socket address - is a mix of IP address + port address

After the connectivity, that is, the networking problem - the listening and handling many client connections, the next thing is reading and parsing the command. The server needs lots of power (?), or maybe just enough power (like, CPU?) to parse the command. From the redis university RU301 video, it says that reading from the socket is really expensive and the same goes for writing to the socket. So it's mentioned that it's better to keep all that functionality in a different thread

I have also seen that the command execution is tricky - some databases use query engines and what not, and have a plan to execute the query / command. So, that requires some power too

And then the actual execution of the command also needs some power, not to mention it also needs to read the data from the data storage. In redis it's the RAM so it's fast. Some databases use Disk, I know one that uses S3 - Simple Storage Service, so it's gonna be totally different there. So that Input/Output operations also requires quite some power - CPU and/ other power? IO power?


