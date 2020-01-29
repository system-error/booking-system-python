from room import Room as r

guest1 = r()

#print(guest1.roomsAndBeds['room1'])


for room in guest1.roomsAndBeds:
    print(f"Rooms: {room} and beds: {guest1.roomsAndBeds[room]['beds']}")
