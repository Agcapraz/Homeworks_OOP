import math

class Circle:
    def __init__(self, Radius = 1.0 , Color = "Red"):
        self.Radius = Radius
        self.Color = Color

    def __str__(self):
        return "Circle[" + \
               "Radius=" + str(self.radius) + "," + \
               "Color=" + self.color + \
               "]"

    def getRadius(self):
        return self.Radius

    def setRadius(self, RadiusNew):
        self.Radius= RadiusNew

    def getColor(self):
        return self.Color

    def setColor(self, ColorNew):
        self.Color= ColorNew

    def getAreaCircle(self):
        return math.pi*self.Radius**2
