class Date:
    def __init__(self, day=[1,31], month=[1,12], year=[1900,9999]):
        self.day= day
        self.month= month
        self.year=year

    def __str__(self):
        return "Date[" + \
               "day=" + self.day + "," + \
               "month=" +self.month + "," + \
               "year=" + self.year + \
               "]"

    def getday(self):
        return self.day

    def getmonth(self):
        return self.month

    def getyear(self):
        return self.year

    def setday(self, newday):
        self.day= newday

    def setmonth(self, newmonth):
        self.month= newmonth

    def setyear(self, newyear):
        self.year= newyear

    def setdate(self, newday, newmonth, newyear):
        self.day= newday
        self.month= newyear
        self.year= newyear
