def get_available(seat_map, seats_required): # ?, 5
  """Return the available contiguous seats that match the criteria"""
  seats = []
  end_seat = seat_map.bit_length()+1 # 10 + 1 = 11
  if seats_required <= end_seat: # 5 <= 11
    required_block = int(math.pow(2, seats_required))-1 # 2^5 - 1 = 32 - 1 = 31
    for i in range(1, end_seat+1): # range(1, 12)
      if (seat_map & required_block) == required_block: # 
        seats.append({'first_seat': i, 'last_seat': i + seats_required -1})
      required_block = required_block << 1
  return seats
