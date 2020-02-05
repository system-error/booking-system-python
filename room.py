# from reservation import Reservation

class Room:
    
    startDateReserved = [] 
    endDateReserved = []
    roomsAndBeds = {
        "room1":{
            "beds": 2,
            "price": 15,
            "startDateReserved": ["03-05-2020","15-5-2020","1-6-2020"],
            "endDateReserved": ["10-5-2020","22-5-2020","5-6-2020"]
        },
        "room2":{
            "beds": 1,
            "price": 10,
            "startDateReserved": ["03-06-2020"],
            "endDateReserved": ["10-06-2020"]
        },
        "room3":{
            "beds": 4,
            "price": 30,
            "startDateReserved": ["03-07-2020"],
            "endDateReserved": ["10-07-2020"]
        },
        "room4":{
            "beds": 3,
            "price": 25,
            "startDateReserved": ["03-08-2020"],
            "endDateReserved": ["10-08-2020"]
        }
    }

    def __init__(self):
        for room in self.roomsAndBeds:            
            self.startDateReserved.append([[int(y) for y in x.split("-")]for x in self.roomsAndBeds[room]['startDateReserved']])
            self.endDateReserved.append([[int(y) for y in x.split("-")]for x in self.roomsAndBeds[room]['endDateReserved']])

    



# t = Room()

# for x in t.roomsAndBeds:
#     print(x)
#     for y in x.split("-"):
#         print(int(y))