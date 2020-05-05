class Time:


    def __init__(self, hour, minute, second):
        self.__hour = hour[0, 23]
        self.__minute = minute[0, 59]
        self.__second = second[0, 59]


    def __str__(self):
        return "Time[" + \
               "hour=" + str(self.__hour) + "," + \
               "minute=" + str(self.__minute) + "," + \
               " second=" + str(self.__second) + \
               "]"

    def getHour(self):
        return self.__hour


    def getMinute(self):
        return self.__minute


    def getSecond(self):
        return self.__second


    def setHour(self,newHour):
        self.__hour= newHour


    def setMinute(self, newMinute):
        self.__minute = newMinute


    def setSecond(self, newSecond):
        self.__second = newSecond


    def setTime(self, newHour,newMinute, newSecond):
        self.__hour= newHour
        self.__minute= newMinute
        self.__second = newSecond

    def nextSecond(self):
        return Time


    def previousSecond(self):
        return Time



