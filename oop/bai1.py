class Person:
    def __init__(self, first_name, last_name, age):
        #instace variables
        self.first_name = first_name
        print 'init method constructor get callbel'
        self.last_name = last_name
        self.age  = age
p1 = Person('Harshit', 'Vashistha', 24)
p2 = Person('Mohit', 'Vashistha', 19)

# print p1.first_name
# print p2.first_name