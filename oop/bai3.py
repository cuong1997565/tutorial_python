##method
class Person:
    def __init__(self, first_name, last_name, age):
        #instace variables
        self.first_name = first_name
        self.last_name = last_name
        self.age  = age
    def full_name(self):
        return self.first_name + " " + self.last_name
    def is_above_18(self):
        return self.age > 18
p1 = Person('Harshit', 'Vashistha', 24)
p2 = Person('Harshit 123', 'Vashistha 123', 13)
# print p1.full_name()
print Person.full_name(p2)
print p2.is_above_18()
