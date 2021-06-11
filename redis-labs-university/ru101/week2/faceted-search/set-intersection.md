# Set Intersection

In this method, we can take every event and store some extra metadata separately about it. How?

So, the goal is - we have to be able to filter out events based on some attributes of the events - it could be one attribute or multiple attributes

Now, every time someone creates an event, we could insert the event data into the data store using a key `events:<a-unique-id>` and value `<event-data>` in some form (string, list of strings, set, sorted sets, hash). Apart from this, we can also do this - for every attribute and value pair in the event, we can create a set and then put the event ID as a value / element in that set! :D

For example, in event `events:1889`

```json
{
    "name": "Karate event",
    "disabled": true,
    "venue": "India",
    "medal": true
}
```

Now, assuming that we allow searches only based on `disabled`, `venue` and `medal` (medal - is a medal given as price for winning), we can do this -

```
> SADD `disabled:true` 1889

> SADD `venue:India` 1889

> SADD `medal:true` 1889
```

What we are doing is - creating sets with the attribute and value pair, separated by `:` and then storing the event ID in the sets

So, when someone searches for - "What are the events that are accessible for disabled people?", we simply look at the set `disabled:true`

Note that the name of the set is presented in this way, though a bit of extra detailing can added, like, if this set and search is for events and we have separate searches for other stuff, then we can use the set name as -

`events:search:disabled:true`

Any name that makes sense :) In the above case, it helps us with adding another kind of search set for something else, let's say list of softwares? list of services? where again `disabled` is a field, with values like `true` and `false` and can have similar or totally different meaning and the data set can be different too of course, like I just mentioned - list of softwares and list of services etc, then we can create sets with names

`softwares:search:disabled:true`

`services:search:disabled:true`

Now, with the naming discussed, how does the whole solution now look like?

So, for every event data that's inserted, we create some extra metadata regarding the event and put it in sets, for future purposes, for helping with search. So, insertion is more complex - as it's not just insertion of the event data, but we also need to insert metadata. The extra metadata will take up more space too. The search could be faster though, how? Let's see

Before going into search speed, let's look at how many sets would get created and how much event IDs would be present in each of them. Event IDs is the metadata I was referring to when I said extra metadata

The number of sets and size of each set really depends on the data at hand. What does it depend on exactly? What part of the data? So, we create a set for each attribute and value pair, right? So, if there are many attributes, or many different kinds of values for a given attribute, then the number of sets is going to be huge!! For example, if event has multiple attributes, like say 10 attributes, that would mean you would have at least 10 sets each having a name starting with `<attribute-name>:`, for example `medal:`, `disabled:` etc. And then comes the number of values or the value distribution for each of these attributes.

For example, `disabled` has only two discrete values - `true` and `false`, so there will only be two sets `disabled:true` and `disabled:false` (an example, names could vary though) related to `disabled` attribute

What if an attribute can contain 3 discrete values? Then 3 sets. What if it's n discrete values? n sets! Not to mention, I'm talking about these values being present in the event data in the attributes. If it's not present, there's no point in creating the sets as it will be empty as there wouldn't be any event with that attribute and value pair

What if the attribute can contain continuous values? :O For example, if there's an attribute named `highest_score` to tell about the event's highest score from last year, or this year, something like that. And `highest_score` can be a floating point value between 1 and 100. This is a very tricky situation, as there could be so many sets. Especially if every event highest score value is different and unique, then there will be as many number of faceted search highest score sets as the number of events, with each set containing just one event!! :O That's crazy! Also, food for thought - what if someone says "What are the events that have the highest_score between 80 and 100?", it's a whole different game and different kind of searching compared to what we are doing. Ours seems more easier, especially with a discrete value, compared to range or continuous values

That brings us to the next point, apart from the number of sets, what's the size of these sets? Or to put it technically, what's the cardinality of these sets?

Well, cardinality again depends on the value distribution. For example, let's take `disabled` attribute. If there are only two discrete value, what it means is - for any event, it will either be part of `disabled:true` or `disabled:false`, assuming every event has this attribute defined with a value. So, all events fall into one of the two sets. If there are many `true` values, then `disabled:true` set cardinality is going to be high with lot of event IDs, and for `disabled:false`, the cardinality will be small. So, you can put some sort of percentage for the size of the data that's being distributed among the different attribute and value pair associated sets, for a given attribute

For example, for attribute `disabled`, 80% events could have it as `true` and 20% events could have it as `false`. If total events count is 100, then you can find out cardinality just by calculating percentage based values, so 80 for `true` and 20 for `false`

Similarly, if there are more discrete values, more distribution among the sets of a given attribute. So, the size of each set is going to vary depending on how many events have a given attribute and value pair

For continuous values, and all unique values for a given attribute, like I said, every attribute and unique value pair will have a set and each set will have only 1 value. I know, crazy! Just an interesting edge case 😅

So, how does this all matter? Well, coming to the speed of search part, let's say I want to search

"What events that are accessible for disabled people and provide medals and are present in India?"

Notice the different attributes and how I use "and"

So, it's like - putting the different conditions and saying that all have to be met

For such a scenario, when we use sets metadata, we can actually do this -

```
> SINTER disabled:true medals:true venue:India
```

And that will do an intersection of all the sets which are associated with a given attribute and value pair and have event ID which have that particular attribute and value pair. When you do intersection, you find all events that have all these attribute and value pairs and it answers your question. You just need to then get the full event data using the IDs you get as a result

How fast is this? Well, set intersection in this case has a time complexity of O(N x M). What does that mean?

Well, logically, to do intersection, you can easily do intersection if you find out what's the smallest set - the set with the smallest cardinality / number of values and then use that to do the intersection. How? You could iterate over all the values in this smallest size set and then for each value, look for the value in the other bigger sets

So, at the end, you first iterate only through the values in the smallest set! :) Which is better than iterating through larger sets. Next, you also look for the element in each of the other sets, and then find the common values which gives you the intersection

So, let's say N is the size of the smallest set. Let's move on to understanding how much time it takes to find out if an element / value is present in other sets

For a given value, to check if it exists in each of the other sets, it takes how much time complexity?

Well, checking if a set contains an elements or not, it's only O(1). It can be done using `SISMEMBER` - https://redis.io/commands/sismember

So, if the number of attribute and value pairs that are part of our search is M, then the time complexity is O(M). In the above example, the number of attributes that are part of our search is - 3 - (disabled and true), (medals and true), (venue and India). If you look closely, in this case specifically, it's also kind of the number of attributes that are part of our search, the value is of course going to come together with attribute to understand what value should that attribute have, and it's only a single discrete value

Now, for one element it takes O(M) time complexity, then for N elements the time complexity is O(N x M) :D

Something to note is - we didn't talk about how we will handle update in event attribute and values. The redis labs video also mentions this.

When updating event data, we have to update the search set data too, which is kind of the metadata to help with search. And if we don't update it, it will be based on old event data and will lead to wrong search results!! :O
