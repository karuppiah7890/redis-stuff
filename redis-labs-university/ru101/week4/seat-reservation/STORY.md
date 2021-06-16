# Story

I was a bit confused with the `get_available` function

I need to understand how it works sometime

Especially the part about 

```python
end_seat = seat_map.bit_length()+1
```

I was thinking that the `bit_length` is always 10 if the seat block size is 10 bits, no matter what those ten bits hold. If that is true, I was wondering how they add 1 to it and then do the check like this

```python
if seats_required <= end_seat:
```

For example, if the value of the `seat_map.bit_length()` is 10, and `end_seat`'s value is 11, then how can one justify that if `seats_required` is less than or equal to `end_seat` then we can find the seats we need?

I mean, let's say `seat_required` is 11, it can't be satisfied! As the block only has 10 seats based on the setup in the program. The above condition seems to allow going into the `if` condition though, hmm. I'm wondering how that works

Gotta dig in and understand better about what these functions do and use print statements to see values

I tried to do that and noticed that the values I guessed were right, hmm

```bash
uc03-seat-reservation$ python seat_reservation.py

==Test - Find Seats
== Find 6 contiguous available seats
seat_map 1023 seats_required 6
end_seat 11
required_block 63
seat_map 1023 seats_required 6
end_seat 11
required_block 63
Event: 123-ABC-723
-Row: B, Start 1, End 6
-Row: B, Start 2, End 7
-Row: B, Start 3, End 8
-Row: B, Start 4, End 9
-Row: B, Start 5, End 10
Event: 123-ABC-723
-Row: A, Start 1, End 6
-Row: A, Start 2, End 7
-Row: A, Start 3, End 8
-Row: A, Start 4, End 9
-Row: A, Start 5, End 10
== Remove a 4 seat from Block A, so only Block B has the right
 availability for 6 seats
uc03:seatmap:123-ABC-723:General:B        | 1 1 1 1 1 1 1 1 1 1 |
uc03:seatmap:123-ABC-723:General:A        | 1 0 0 0 0 1 1 1 1 1 |
seat_map 1023 seats_required 6
end_seat 11
required_block 63
seat_map 993 seats_required 6
end_seat 11
required_block 63
Event: 123-ABC-723
-Row: B, Start 1, End 6
-Row: B, Start 2, End 7
-Row: B, Start 3, End 8
-Row: B, Start 4, End 9
-Row: B, Start 5, End 10
uc03-seat-reservation$
```

I tried reserving 11 contiguous seats and got this

```bash
$ python seat_reservation.py

==Test - Find Seats
== Find 6 contiguous available seats
Row 'uc03:seatmap:123-ABC-723:General:B' does not have enough seats
Row 'uc03:seatmap:123-ABC-723:General:A' does not have enough seats
== Remove a 4 seat from Block A, so only Block B has the right
 availability for 6 seats
uc03:seatmap:123-ABC-723:General:B        | 1 1 1 1 1 1 1 1 1 1 |
uc03:seatmap:123-ABC-723:General:A        | 1 0 0 0 0 1 1 1 1 1 |
seat_map 1023 seats_required 6
end_seat 11
required_block 63
seat_map 993 seats_required 6
end_seat 11
required_block 63
Event: 123-ABC-723
-Row: B, Start 1, End 6
-Row: B, Start 2, End 7
-Row: B, Start 3, End 8
-Row: B, Start 4, End 9
-Row: B, Start 5, End 10
uc03-seat-reservation$
```

I think the below `if` condition

```python
    if redis.bitcount(block) >= seats_required:
```

helps with this check, before it even reaches `get_available` which is part of the `if` body


