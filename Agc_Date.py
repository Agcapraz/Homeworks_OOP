class Date:


    def __init__(self, day = [1,31], month = [1,12], year = [1900,9999]):
        self.__day= day
        self.__month= month
        self.__year=year


    def __str__(self):
        return " Date[ " + \
               " day= " + str(self.__day) + " , " + \
               " month = " + str(self.__month) + " , " + \
               " year = " + str(self.__year) + \
                "] "


    def getday(self):
        return self.__day

    def getmonth(self):
        return self.__month

    def getyear(self):
        return self.__year

    def setday(self, newday):
        self.__day= newday

    def setmonth(self, newmonth):
        self.__month= newmonth

    def setyear(self, newyear):
        self.__year= newyear


    def setdate(self, newday, newmonth, newyear):
        self.__day= newday
        self.__month= newyear
        self.__year= newyear
