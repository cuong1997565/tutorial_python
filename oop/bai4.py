#class variable
class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi
    def calc_circumference(self):
        return 2 * self.pi * self.radius
c = Circle(4, 3.14)
print c.calc_circumference()
print c.__dict__