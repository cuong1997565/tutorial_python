#Special magic/dunder method, operator overloading, polymorphism :
class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def phone_name(self):
        return self.brand +" "+ self.model
    def __str__(self):
        return self.brand +" "+ str(self.price)
    def __repr__(self):
        return self.brand +" "+self.model+" and price is "+ str(self.price)
    def __len__(self):
        return len(self.phone_name())
    def __add__(self,other):
        return self.price + other.price
    def __mul__(self,other):
        return self.price * other.price
class SmartPhone(Phone):
    def __init__(self,brand,model,price,camera):
        Phone.__init__(self,brand,model,price)
        # super().__init__(brand,model_name,price)
        self.camera = camera
    def phone_name(self):
        return self.brand+" "+self.model+"and price is :"+ str(self.price)


my_phone = Phone('nokia', '1100', 1000)
my_phone2 = Phone('nokia', '1100', 1200)
my_smartphone = SmartPhone('oneplus','5t','30000','16 Mp')
print my_phone + my_phone2
print my_phone * my_phone2
print my_smartphone.phone_name()
print my_phone.phone_name()
# print str(my_phone)
# print repr(my_phone)
# print len(my_phone)