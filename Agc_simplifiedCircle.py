import math

class Circle:

    def __init__(self, Radius = 1.0 ):
        self.Radius = Radius

    def __str__(self):
        return "Circle[" + \
               "Radius=" + str(self.radius) + "," + \
               "]"

    def getRadius(self):
        return self.Radius

    def setRadius(self, RadiusNew):
        self.Radius= RadiusNew

    def getCircumferenceCircle(self, CircumferenceCircle):
        self.CircumferenceCircle= 2*math.pi*self.Radius
        return Radius

Circle1 = Circle(2)
Circle2 = Circle(5)

print(Circle)

print(Circle1.Radius)
print(Circle2.Radius)
print(("new radius"))
#print(Circle1.Radius(3.0))

#print(Circle1.CircumferenceCircle)
#print(Circle2.CircumferenceCircle)
#print(Circle2.Radius)
#print(Circle1())


#print(Circle2.CircumferenceCircle)
print(Circle)
