I was checking about secrets management in Redis. I'll have to read about ACL though, I guess, but I wanted to check if Hashicorp Vault can generate secrets dynamically in Redis, I guess not, at least as of now

https://duckduckgo.com/?t=ffab&q=hashicorp+vault+secrets+engine&ia=web

https://learn.hashicorp.com/tutorials/vault/getting-started-secrets-engines

https://www.vaultproject.io/docs/secrets

A similar thing for Postgres - https://www.vaultproject.io/docs/secrets/databases/postgresql , to generate secrets dynamically for Postgres

Also, Postgres can be used as backend to store Vault's secrets too https://www.vaultproject.io/docs/configuration/storage/postgresql . Redis - I couldn't find any such thing

https://www.vaultproject.io/api-docs/secret/databases/postgresql - to generate secrets dynamically for Postgres

https://github.com/search?utf8=%E2%9C%93&q=hashicorp%20vault%20redis

https://github.com/RedisLabs/vault-plugin-database-redis-enterprise

https://github.com/RedisLabs/vault-plugin-database-redis-enterprise/issues/10 - issue asking about open source Redis

There's a secrets engine for redis enterprise alone


