class Laptop:
    discount_percent = 10
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
        self.laptop_name = brand + ' '+ name
    
    def apply_discount(self):
        off_price = (Laptop.discount_percent * self.price) / 100
        return self.price - off_price

laptop1 = Laptop('hp','au14tx',63000)
laptop2 = Laptop('hp 12','au14tx 12',63000)

laptop1.discount_percent = 50
print laptop2.__dict__
print laptop1.apply_discount()

