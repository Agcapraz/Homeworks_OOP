class invoiceItem:

    def __init__(self, id, desc, qty, unitPrice):
        self.__id= id
        self.__desc= desc
        self.__qty= qty
        self.__unitPrice= unitPrice

    def __str__(self):
        return "invoiceItem [" + \
               "id=" + self.__id + "," + \
               "desc=" + self.__desc + "," + \
               "qty=" + str(self.__qty) + "," + \
               "unitPrice=" + str(self.__unitPrice) + \
               "]"

    def getid(self):
        return self.__id

    def getdesc(self):
        return self.__desc

    def getqty(self):
        return self.__qty

    def setqty(self, Newqty):
        self.__qty = Newqty

    def getunitPrice(self):
        return self.__unitPrice

    def setunitPrice(self, NewunitPrice):
        self.__unitPrice = NewunitPrice

    def getTotal(self):
        return self.__qty * self.__unitPrice


product1=invoiceItem("computer","sonyvoio",1,1000)
product2=invoiceItem("computer", "asus",5,1500)
product3=invoiceItem("keybord", "abc", 10,15)

print(invoiceItem)
print(product1.getid())
print(product1.getdesc())
print(product1.getqty())
print(product1.getunitPrice())
print(product2)

product1.setunitPrice(1100)
product1.setqty(100)
print("product1 NEW Total")
print(product1.getTotal())
