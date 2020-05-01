import math

class Circle:


    def __init__(self, Radius = 1.0 ):
        self.__Radius = Radius


    def __str__(self):
        return "Circle[" + \
               "Radius=" + str(self.__Radius) + "," + \
               "]"


    def getRadius(self):
        return self.__Radius


    def setRadius(self, RadiusNew):
        self.__Radius= RadiusNew


    def getCircumferenceCircle(self):
        return 2 * math.pi * self.__Radius



Circle1 = Circle(2)
Circle2 = Circle(5)


print(Circle)

print(" Circle1 circumference is ")
print(Circle1.getCircumferenceCircle())
print(" Circle2 circumference is ")
print(Circle2.getCircumferenceCircle())
print(Circle)