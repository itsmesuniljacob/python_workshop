class date():
    def __init__(self):
        self.dd = 10
        self.mm = 5
        self.yy = 2019

    def Display(self):
        print(str(self.dd)+'-'+str(self.mm)+'-'+str(self.yy))
    
    def __add__(self,days):
        
        temp_day = date()
        temp_day.dd = self.dd + days
        while (temp_day.dd > 28):
            if temp_day.mm in [1,3,5,7,8,10,12] and temp_day.dd > 31:
                temp_day.dd -= 31
                temp_day.mm += 1
                if temp_day.mm == 13:
                    temp_day.mm = 1
                    temp_day.yy += 1        
            elif temp_day.mm in [4,6,9,11] and temp_day.dd > 30:
                temp_day.dd -= 30
                temp_day.mm += 1
            elif temp_day.mm == 2 and temp_day.dd > 28 and (temp_day.yy % 4) != 0:
                temp_day.dd -= 28
                temp_day.mm += 1
            elif temp_day.mm == 2 and temp_day.dd > 29 and (temp_day.yy % 4) == 0:
                temp_day.dd -= 29
                temp_day.mm += 1

        return temp_day
        # self.dd += days
        # return self
today = date()
today.Display()
# today is an object of class date is equivalent to __add__(today,1) , all depends on the +
# help(int) for more info -- > __add__ comes from here
tomorrow = today + 3650
tomorrow.Display()
#today.Display()