import math


class Circle(object):
    
    radius = 1    

    # All class methods have 'self' as first argument
    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


circle = Circle()

print("Circle area: %f" % circle.area())