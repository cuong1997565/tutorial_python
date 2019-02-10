class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
    def full_name(self):
        return self.brand +" "+ self.model_name
    def make_a_call(self,number):
        return "calling "+number

class Smartphone(Phone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera):
        Phone.__init__(self,brand,model_name,price)
        # super().__init__(brand,model_name,price)
        self.ram = ram
        self.ininternal_memory = internal_memory
        self.rear_camera = rear_camera
    def full_name(self):
        return self.brand +" "+self.model_name +" and price is " + str(self.price)

class FlagshipPhone(Smartphone):
    def __init__(self,brand,model_name,price,ram,internal_memory,rear_camera,front_camera):
        Smartphone.__init__(self,brand,model_name,price,ram,internal_memory,rear_camera)
        self.front_camera = front_camera
    def full_name(self):
        return self.brand +" "+self.model_name +" FlagshipPhone and price is " + str(self.price) + "and front_camera ="+ self.front_camera

phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('onePlus', '5', 30000, '6 GB', '64 GB', '20 MP')
oneplus    = FlagshipPhone('onePlus 123 ', '5', 30000, '6 GB', '64 GB', '20 MP','sad')
print phone.full_name()
# print smartphone.full_name() + " and price is :" + str(smartphone.price)
print smartphone.full_name()
print oneplus.full_name()
print isinstance(smartphone, Smartphone)
# print help(FlagshipPhone)
print issubclass(Smartphone, Phone)