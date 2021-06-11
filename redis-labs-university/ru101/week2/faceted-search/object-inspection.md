# Object Inspection

Considering the events example, where we need to search for events with a particular set of filters - if it's accessible for disabled people, where's the venue and so on, let's see how object inspection method approaches

In object inspection method, we list down all the values that are present in the data store. In our example this would mean first listing down all the events, even if we are searching only for events which are accessible only for disabled people. Our search result is probably only a subset of all these values in reality. In a redis data store, how we do object inspection is, we first use `SCAN` and scan through all the keys that denote an event using `events:*`. This assuming that every event is stored under a key in the format of `events:<a-unique-id>` and is stored as a hash or as a JSON string or something. In the redis labs example it's a JSON string. Object inspection means - looking at all the data for the whole list of items. We just got the list of keys using `SCAN`. Also, not to mention, `SCAN` is better, though `KEYS` can also be used. `KEYS` is not effient though, and hence `SCAN` and we might have to `SCAN` multiple number of times to get all the keys associated with events

After getting the keys, we have get the values for each of these keys so that we get the whole event object for each event, and not just have some unique event id which is present as part of the key. The ID does not really have any data. Just an ID. So, when we get all the values for all the events using `GET` and all the events keys, we then do the search using our own program

For example, we can use Python, or Java, or Golang, or anything, and do the above multiple `SCAN`s and `GET`s and then do the search in the programming language that we have

Something to note is - we are pulling down all the data from redis in this case. We could keep it in-memory in our program or store it all in some file or something and then do the search on top of it.

If you think about it, it's like using Redis simply as a data storage where you store data and retrieve data, and then do the search yourself in the programming language of your comfort. This is only in this method. Other methods are a bit better
