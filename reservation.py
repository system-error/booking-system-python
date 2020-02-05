from room import Room

class Reservation:
    days = [1,2,3,4,5,6,7,8,9,10,
            11,12,13,14,15,16,17,18,19,20,
            21,22,23,24,25,26,27,28,29,30,31]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    year = 2020
    numberOfDays=1

    # def __init__(self):
    #     self.days
    #     self.months
    #     self.year
    #     self.numberOfDays
    

    def makeReservation(self):
        
        startDate = []
        endDate = []
        counter = 0
        start = "start"
        end = "end"
        
        while counter<2:

            if (counter<1):
                day = int(input(f"Give me the {start} day in number from 1-31 "))
            else:
                day = int(input(f"Give me the {end} day in number from 1-31 "))
            if self.days.__contains__(day):
                if len(startDate) < 3:
                    startDate.append(day)
                else:
                    endDate.append(day)   
            else:
                print("Wrong number, try again")
                counter = 2

            if (counter<1):
                month = int(input(f"Give me the {start} month in number from 1-12 "))
            else:
                month = int(input(f"Give me the {end} month in number from 1-12 "))
            if self.months.__contains__(month):
                if len(startDate) < 3:
                    startDate.append(month)
                else:
                    endDate.append(month) 
            else:
                print("Wrong number, try again")
                counter = 2    
            
            if len(startDate) < 3:
                startDate.append(self.year)
            else:
                endDate.append(self.year)
            counter +=1    
        return startDate,endDate
        


    def availability(self,startDates,endDates,room):
        # print(Room.roomsAndBeds[room])
        # test=len(Room.roomsAndBeds)
        for x in range(0, len(Room.roomsAndBeds)):
            for y in range (len(Room.startDateReserved[x])):
                if(((Room.startDateReserved[x][y][0] < startDates[0]) and (Room.startDateReserved[x][y][1] == startDates[1])) 
                    or ((Room.endDateReserved[x][y][0] < endDates[0]) and (Room.endDateReserved[x][y][1] == endDates[1]))) :
                    print("test")


    def displayTheRooms(self):
        print("Our Rooms")
        print("")
        for room in Room.roomsAndBeds:
            print(f"====== {room}  ======")
            print(f"The number of beds for this room are: {Room.roomsAndBeds[room]['beds']}")
            print("=================")
            print(f"The price for this room is: {Room.roomsAndBeds[room]['price']} €")
            print("")

    def greetings(self):
        pass                           

# re = Reservation()

# startDate = re.makeReservation()

r = Room()

# re = Reservation()

# startDate,endDate = re.makeReservation()

# re.availability(startDate,endDate,r.roomsAndBeds['room1'])


# ro = Room()







        
         

    
