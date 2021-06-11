# Hashed search

In this method too we store some extra metadata apart. Here what we try to do is - given an event we take the attribute and value pairs that will be used as part of searches. We then put it all together and then hash it using a hash function - like Message Digest (MD) example is MD5, or SHA, example is SHA1, SHA256, SHA512 etc and there are other hash functions too

After hashing we get a hash value, which we can use as a key for a set and then store the event ID in the set

This is based on the assumption that different data of attribute and value pairs will not lead to the same hash - basically a clash. To ensure this use a hashing function with high number of bits with minimal clashing comparatively or as much as possible

With this, what we can do is, when we get a search query like "What events that are accessible for disabled people and provide medals and are present in India?", then we can simply form a set of attribute and value pairs, hash it, look for a redis key with that hash, and peek into the set values using `SSCAN` which is more efficient than `SMEMBERS`

The time complexity is just the number of elements in the set under the key with that hash value which can be considered as N. It's basically the result list of the search operation. So, the number of values in the result list

How is that the time complexity? Well, given a key, the time complexity to find the value in redis using `GET` is O(1) and then scanning through all members of the set which is the search result list - time complexity is - O(N), where N is the number of elements in the set. So we take the higher value here :) which is O(N)

Some tricky things are -

For a given event with many attribute and value pairs, do we find exactly one hash out of the full attribute and value pairs and store the event in just one set under than hash value key?

For example,

```json
{
    "name": "Karate event",
    "disabled": true,
    "venue": "India",
    "medal": true
}
```

If the example hash value for below attribute and value pairs is H1

```json
{
    "disabled": true,
    "venue": "India",
    "medal": true
}
```

Then do we store `H1` key with one value in the set as `events:1889`?

With this we can only search with all three values, which is `disabled`, `venue` and `medal`

What if the search is done only with one attribute? Hashing that one attribute and value pair will not lead to the above hash value, so, it won't work out

So, do we store different combinations of the attribute and value pairs?

`disabled`

`venue`

`medal`

`disabled` and `venue`

`disabled` and `medal`

`venue` and `medal`

`disabled`, `venue` and `medal`

Also, not to mention, the hash value we create while inserting data - the mechanism we use to hash the attribute and value pairs, we need to use the same mechanism, ditto, while searching. So, the hash function input is key and has to be proper and exact always. For example, we can put the attributes in alphabetical order always so that there's a predefined order which we use as input for the hashing, and it's consistent and deterministic and same while creating metadata and while searching :) This way, we only have to take care of storing combination of attributes for metadata, but not permutation, as the order is predefined now - only alphabetical order while doing processing - metadata insertion and searching :)

When we store the hashes with event data in the above way, we can actually search with just any one attribute, any two attributes or all three attributes and we have the metadata for all

What are the costs here?

Well, there's a lot of metadata here

Not to mention, what happens when we update event data? We need to update the metadata - cleanup, remove values from sets, or remove whole sets, which redis will do by itself once all elements of the sets are removed! :)


