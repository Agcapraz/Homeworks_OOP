class invoiceItem:

    def __init__(self, id, desc, qty, unitPrice):
        self.id= id
        self.desc= desc
        self.qty= qty
        self.unitPrice= unitPrice

    def __str__(self):
        return "invoiceItem [" + \
               "id=" + self.id + "," + \
               "desc=" +self.desc + "," + \
               "qty=" + str(self.qty) + "," + \
               "unitPrice=" + str(self.unitPrice) + \
               "]"

    def getid(self):
        return self.id

    def getdesc(self):
        return self.desc

    def getqty(self):
        return self.qty

    def setqty(self, Newqty):
        self.qty = Newqty

    def getunitPrice(self):
        return self.unitPrice

    def setunitPrice(self, NewunitPrice):
        self.unitPrice = NewunitPrice

    def getTotal(self):
        return self.qty*self.unitPrice


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
