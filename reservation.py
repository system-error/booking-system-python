from room import Room

class Reservation:
    days = [1,2,3,4,5,6,7,8,9,10,
            11,12,13,14,15,16,17,18,19,20,
            21,22,23,24,25,26,27,28,29,30,31]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    year = 2020 
    
    def makeReservation(self,roomSelected):
        
        theRoom = "room"+str(roomSelected)
        price = 0 
        print(theRoom)
        startDate = []
        endDate = []
        counter = 0
        start = "start"
        end = "end"
        
        print("The reserved days for this room are: ")

        for x in range(len(r.roomsAndBeds[theRoom]['startDateReserved'])):
            print(f"{x+1}. From: {r.roomsAndBeds[theRoom]['startDateReserved'][x]}")
            print(f"   To: {r.roomsAndBeds[theRoom]['endDateReserved'][x]}")
            print("")
            print("Please choose the booking dates")

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

        reservationDays = abs(startDate[0] - endDate[0])
        price = reservationDays * Room.roomsAndBeds[theRoom]['price']  
        self.availability(startDate,endDate,theRoom,price,reservationDays)

    def availability(self,startDates,endDates,room,totalPrice,reservationDays):
        
        for x in range(0, len(Room.roomsAndBeds)):
            for y in range (len(Room.startDateReserved[x])):
                if(((startDates[0] <= Room.startDateReserved[x][y][0]) and ((endDates[0] <= Room.endDateReserved[x][y][0]) or (endDates[0] > Room.endDateReserved[x][y][0])) and (Room.startDateReserved[x][y][1] == startDates[1]))
                or ((endDates[0] >= Room.startDateReserved[x][y][0]) and (endDates[0] <= Room.endDateReserved[x][y][0]) and (Room.endDateReserved[x][y][1] == endDates[1])) ):
                    print("This dates are already reserved please give us another date")
                    self.makeReservation(room.replace('room',''))
                
        print("Thanks the room is booked!")
        print(f"The total price of booking is {totalPrice} and the days you are booked are {reservationDays}")
        Room.startDateReserved.append(startDates)
        Room.endDateReserved.append(endDates)            


    def displayTheRooms(self):
        print("Our Rooms")
        print("")
        for room in Room.roomsAndBeds:
            print(f"====== {room}  ======")
            print(f"The number of beds for this room are: {Room.roomsAndBeds[room]['beds']}")
            print("=================")
            print(f"The price for this room is: {Room.roomsAndBeds[room]['price']} €")
            print("")
        roomSelected = input(f"Select the room that you need from 1 up to {len(room)-1}: ")
        print("You have selected the room",roomSelected)
        self.makeReservation(roomSelected)     

    def greetings(self):
        print("Welcome to our booking system")
        print("Press 1 to do a book")
        print("Press 2 to exit")
        print("==========")
        inputValue = int(input("Choose : "))
        if(inputValue == 1):
            self.displayTheRooms()
        else:
            exit("Good Bye")            


r = Room()