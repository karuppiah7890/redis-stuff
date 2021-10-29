
# Redis Conf Parser CLI

This would be a CLI that can parse and modify Redis config file. Usually we would rely on redis-server and a client to change the config and write it back to the config file and also let redis-server do config validations

I thought about developing a pet project just to learn about different configs and also be able to change the config file without redis-server or something like redis-cli client. The parser would need to have a lot of knowledge about the Redis config file and each of the configs in it to be able to parse and validate and modify them, almost like porting the Redis server C language code to some other language in which the CLI is written. I'll most probably choose Golang.

Example configs - we would have different types of configs - some having string values, some may have some other kind of special string value for example IPv4 or IPv6 address which is also a string but of a special kind with some format, validation etc. So, we need to parse with some logic and also validate with a separate logic / data types for each of the configs
