class Ball:


    def __init__(self, x, y, Radius, xDelta , yDelta):
        self.__x= x
        self.__y= y
        self.__Radius= Radius
        self.__xDelta= xDelta
        self.__yDelta= yDelta


    def __str__(self):
        return("Ball[" + \
               "(x,y)= " + (" + str(self.x) + "," + str(self.y) + ") + \
               "speed=" + (" + str(self.xDelta) + "," + str(self.yDelta) + ") +\
               "]")

    def getx(self):
        return self.__x


    def setx(self,xNew):
        self.__x= xNew


    def gety(self):
        return self.__y


    def sety(self, yNew):
        self.__y= yNew


    def getRadius(self):
        return self.__Radius


    def setRadius(self, RadiusNew):
         self.__Radius= RadiusNew


    def getxDelta(self):
        return self.__xDelta


    def setxDelta(self, xDeltaNew):
        self.__xDelta= xDeltaNew


    def getyDelta(self):
        return self.__yDelta

    def setyDelta(self,yDeltaNew):
        self.__yDelta= yDeltaNew


    def Move(self, x, y):
        self.__x += self.__xDelta
        self.__y += self.__yDelta


    def reflectionHorizontal(self):
        self.__xDelta -= self.__xDelta


    def reflectionVertical(self):
        self.__yDelta -= self.__yDelta
