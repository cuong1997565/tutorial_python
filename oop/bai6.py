class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        if price > 0:
            self.price = price
        else:
            self.price = 0
    #getter, setter
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = max(new_price, 0)

    @property    
    def complete_specification(self):
        return self.brand  +" "+ self.model_name + " and price is "+ str(self.price)
    def make_a_call(self, phone_number):
        print "calling ", phone_number
    def full_name(self):
        return self.brand  
    def send_message(self):
        pass

phone1 = Phone('nokia','1100', 1000)
# print phone1.__dict__
# phone1._price = -2000
# print phone1._price
print phone1.brand
print phone1.model_name
phone1.price = -100
print phone1.price
print phone1.complete_specification