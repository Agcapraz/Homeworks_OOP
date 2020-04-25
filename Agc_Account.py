class Account:
    def __init__(self, id, Name, Balance=0):
        self.id = id
        self.Name = Name
        if Balance>=0:
            self.Balance = Balance

    def __str__(self):
        return "Account[" + \
               "id=" + str(self.id) + "," + \
               "name=" + self.Name +"," +\
               " Balance=" + str(self.Balance) +\
               "]"

    def getID(self):
        return self.id

    def getName(self):
        return self.Name

    def getBalance(self):
        return self.Balance

    def credit(self, Amount):
        if Amount>=0:
            self.Balance = self.Balance + Amount
        return self.Balance

    def debit(self, Amount):
        if Amount <= self.Balance:
            self.Balance= self.Balance-Amount
        else:
            print ("amount exceeded")
        return self.Balance

    def transferTo(self, AnotherAccount, Amount):
        if self.Balance >= Amount :
            self.Balance -= Amount
            AnotherAccount.credit(Amount)
        else:
            print("Amount exceeded")
        return self.Balance


# ===================== Running classes ===============
ahmet = Account (1, "Ahmet Gurcan" )
ramazan=Account(2, "Ramazan", 1000)
serkan=Account(3, "Serkan", 5000)
print(ahmet)
print(ramazan)
print(serkan)
print("After credit Ahmet New Balance")
print(ahmet.credit(750))
print("After debit Ahmet New Balance")
print(ahmet.debit(350))
print("After credit Ahmet New Balance")
print(ahmet.credit(100))
print("After transfer Ahmet New Balance")
print(ahmet.transferTo(ramazan, 300))
print("After transfer Ramazan New Balance")
print(ramazan.transferTo(serkan, 500))
print(Ahmet)
