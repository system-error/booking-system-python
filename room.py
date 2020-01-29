from reservation import Reservation

class Room:
    roomsAndBeds = {
        "room1":{
            "beds": 2,
            "price": 15,
            "startDate": "2020-05-03",
            "endDate": "2020-05-10"
        },
        "room2":{
            "beds": 1,
            "price": 10,
            "startDate": "2020-06-03",
            "endDate": "2020-06-10"
        },
        "room3":{
            "beds": 4,
            "price": 30,
            "startDate": "2020-07-03",
            "endDate": "2020-07-10"
        },
        "room4":{
            "beds": 3,
            "price": 25,
            "startDate": "2020-08-03",
            "endDate": "2020-08-10"
        }
    }
    startDate = []
    endDate =[]

res = Reservation()

startDate,endDate = res.makeReservation()

print(startDate)
print(endDate)

    