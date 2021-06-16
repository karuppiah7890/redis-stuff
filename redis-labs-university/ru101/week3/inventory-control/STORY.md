
```bash
uc02-inventory-control$ python inventory.py

==Test 1: Check stock levels & purchase
== Request 5 ticket, success
Purchase complete!
{'sku': '123-ABC-723', 'name': "Men's 100m Final", 'disabled_access': 'True', 'medal_event': 'True', 'venue': 'Olympic Stadium', 'category': 'Track & Field', 'capacity': '60102', 'available:General': '5', 'price:General': '25.0'}
== Request 6 ticket, failure because of insufficient inventory
Insufficient inventory, have 5, requested 6
Purchase complete!
{'sku': '123-ABC-723', 'name': "Men's 100m Final", 'disabled_access': 'True', 'medal_event': 'True', 'venue': 'Olympic Stadium', 'category': 'Track & Field', 'capacity': '60102', 'available:General': '5', 'price:General': '25.0'}

==Test 2: Reserve stock, perform credit auth and complete purchase
== Reserve & purchase 5 tickets
Purchase complete!
{'sku': '737-DEF-911', 'name': "Women's 4x100m Heats", 'disabled_access': 'True', 'medal_event': 'False', 'venue': 'Olympic Stadium', 'category': 'Track & Field', 'capacity': '60102', 'available:General': '5', 'price:General': '19.5',
 'held:General': '0'}
== Reserve 5 tickets, failure on auth, return tickets to inventory
Auth failure on order UYTGRN-ZIWMWD for customer joan $97.5
{'sku': '737-DEF-911', 'name': "Women's 4x100m Heats", 'disabled_access': 'True', 'medal_event': 'False', 'venue': 'Olympic Stadium', 'category': 'Track & Field', 'capacity': '60102', 'available:General': '5', 'price:General': '19.5',
 'held:General': '0'}

==Test 3: Back out reservations when expiration threshold exceeded
== Create ticket holds, expire > 30 sec, return tickets to inventory
320-GHI-921, Available:485, Reservations:['3', '5', '7']
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:492, Reservations:['3', '5', None]
320-GHI-921, Available:497, Reservations:['3', None, None]
320-GHI-921, Available:497, Reservations:['3', None, None]
320-GHI-921, Available:497, Reservations:['3', None, None]
320-GHI-921, Available:497, Reservations:['3', None, None]
320-GHI-921, Available:497, Reservations:['3', None, None]
320-GHI-921, Available:497, Reservations:['3', None, None]
320-GHI-921, Available:500, Reservations:[None, None, None]
```


