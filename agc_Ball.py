class Ball:
    def __init__(self, x, y, Radius, xDelta , yDelta):
        self.x= x
        self.y= y
        self.Radius= Radius
        self.xDelta= xDelta
        self.yDelta= yDelta
    def __str__(self):
        return("Ball[" + \
               "(x,y)= " + (" + str(self.x) + "," + str(self.y) + ") + \
               "speed=" + (" + str(self.xDelta) + "," + str(self.yDelta) + ") +\
               "]")

    def getx(self):
        return self.x

    def setx(self,xNew):
        self.x= xNew

    def gety(self):
        return self.y

    def sety(self, yNew):
        self.y= yNew

    def getRadius(self):
        return self.Radius

    def setRadius(self, RadiusNew):
         self.Radius= RadiusNew

    def getxDelta(self):
        return self.xDelta

    def setxDelta(self, xDeltaNew):
        self.xDelta= xDeltaNew

    def getyDelta(self):
        return self.yDelta

    def setyDelta(self,yDeltaNew):
        self.yDelta= yDeltaNew

    def Move(self, x, y):
        self.x += xDelta
        self.y += yDelta

    def reflectionHorizontal(self):
        self.xDelta -= self.xDelta

    def reflectionVertical(self):
        self.yDelta -= self.yDelta
