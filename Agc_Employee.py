class Employee:

    def __init__(self, id, FirstName, LastName, Salary):
        self.__id = id
        self.__FirstName = FirstName
        self.__LastName = LastName
        self.__Salary = Salary


    def __str__(self):
        return "Employee [" + \
               "id=" + str(self.__id) + "," + \
               "FirstName=" + self.__FirstName + "," + \
               "LastName=" + self.__LastName + "," + \
               "Salary=" + str(self.__Salary) + \
               "]"


    def getid(self):
        return self.__id


    def getFirstName(self):
        return self.__FirstName


    def getLastName(self):
        return self.__LastName


    def getName(self):
        return self.__FirstName + " " + self.__LastName


    def getSalary(self):
        return self.__Salary


    def setSalary(self, NewSalary):
        self.__Salary = NewSalary


    def getAnnualSalary(self):
        return self.__Salary * 12


    def raiseSalary(self,percent):
        self.__Salary = self.__Salary + self.__Salary * (percent / 100.0)


Ahmet= Employee(1, " AhmetGurcan ", " Capraz ", 1000)

print(Employee)
print(Ahmet.getFirstName())
print(Ahmet.getLastName())
print(Ahmet.getid())
print(Ahmet.getSalary())
print(Ahmet.getAnnualSalary())

Ahmet.setSalary(1200)
print("Ahmet NEW annual salary")
print(Ahmet.getAnnualSalary())

Ahmet.raiseSalary(10)
print(Ahmet.getSalary())
print(Ahmet.getAnnualSalary())
