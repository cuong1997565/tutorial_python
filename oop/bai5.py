class Person:
    count_instance = 0
    def __init__(self,first_name,last_name,age):
        Person.count_instance = 1 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    @classmethod
    def count_instance(cls):
        return "You have created ",cls.count_instance , " isinstance of ",cls.__name__
    
    @classmethod
    def form_string(cls, string):
        first_name,last_name,age = string.split(',')
        return cls(first_name,last_name,age)
    
    @staticmethod
    def hello():
        print ('hello, static method called')
    
    def full_name(self):
        return self.first_name + " " + self.last_name
p1 = Person('Harshit','Vashisth',24)
p2 = Person('Harshit 2','Vashisth 2',24)
p3 = Person.form_string('Harshit, Vashisth, 24')
print p3.full_name()