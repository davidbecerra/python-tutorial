import math


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    # All class methods have 'self' as first argument
    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius


c1 = Circle(radius=1)
c2 = Circle(2)

print("c1 circumference: %f" % c1.circumference())
print("c2 circumference: %f" % c2.circumference())