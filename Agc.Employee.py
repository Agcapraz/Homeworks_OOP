class Employee:

    def __init__(self, id, FirstName, LastName, Salary):
        self.id= id
        self.FirstName= FirstName
        self.LastName= LastName
        self.Salary= Salary

    def __str__(self):
        return "Employee [" + \
               "id=" + str(self.id) + "," + \
               "FirstName=" +self.FirstName + "," + \
               "LastName=" + self.LastName + "," + \
               "Salary=" + str(self.Salary) + \
               "]"

    def getid(self):
        return self.id

    def getFirstName(self):
        return self.FirstName

    def getLastName(self):
        return self.LastName

    def getName(self):
        return self.FirstName + " " + self.LastName

    def getSalary(self):
        return self.Salary

    def setSalary(self, NewSalary):
        self.Salary= NewSalary

    def getAnnualSalary(self):
        return self.Salary * 12

    def raiseSalary(self,percent):
        self.Salary = self.Salary + self.Salary * (percent/100.0)

Ahmet= Employee(1,"AhmetGurcan","Capraz",1000)

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
