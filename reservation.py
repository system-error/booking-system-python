class Reservation:
    days = [1,2,3,4,5,6,7,8,9,10,
            11,12,13,14,15,16,17,18,19,20,
            21,22,23,24,25,26,27,28,29,30,31]
    months = [1,2,3,4,5,6,7,8,9,10,11,12]
    year = 2020
    numberOfDays=0

    # def __init__(self):
    #     self.days
    #     self.months
    #     self.year
    #     self.numberOfDays
    

    def makeReservation(self):
        # l.__contains__(3)
        startDate = []
        endDate = []
        counter = 0
        print(len(startDate))
        
        while counter<2:

            day = int(input("Give me the day in number from 1-31 "))
            if self.days.__contains__(day):
                if len(startDate) < 3:
                    startDate.append(day)
                else:
                    endDate.append(day)   
            else:
                print("Wrong number, try again")
                counter = 2

            month = int(input("Give me the month in number from 1-12 "))
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
            
                




        
         

    
