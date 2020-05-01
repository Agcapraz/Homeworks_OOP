class Rectangle:


    def __init__(self, Width=1.0, Length=1.0):
        self.__Width = Width
        self.__Length = Length


    def __str__(self):
        return "{width = " + str(self.__Width) +\
               ", length=" + str(self.__Length) + "}"

    def getLength(self):
        return self.__Length

    def getWidth(self):
        return self.__Width

    def setLength(self, newLength):
        self.__Length = newLength

    def setWidth(self, newWidth):
        self.__Width = newWidth


    def getArea(self):
        return self.__Width * self.__Length

    def getPerimeter(self):
        return self.__Width * 2 + self.__Length * 2

rectangle1=Rectangle(2.0, 3.5)
rectangle2=Rectangle( 3, 5)

print(Rectangle)
print(" rectangle1 area is ")
print(rectangle1.getArea())
print("rectangle1 perimeter is")
print(rectangle1.getPerimeter())
print(" rectangle2 area is ")
print(rectangle2.getArea())
print("rectangle2 perimeter is")
print(rectangle2.getPerimeter())

print(Rectangle)


