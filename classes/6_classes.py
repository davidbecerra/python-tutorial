# Parent class for Quadrilaterals
class Quadrilateral(object):
    def __init__(self, side1, side2, side3, side4):
        self.s1 = side1
        self.s2 = side2
        self.s3 = side3
        self.s4 = side4

    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4


# Subclass - inherits from Quadrilateral
class Square(Quadrilateral):
    def __init__(self, side):
        super(Square, self).__init__(side, side, side, side)


class Rectangle(Quadrilateral):
    def __init__(self, length, width):
        super(Rectangle, self).__init__(length, length, width, width)


square = Square(2)
rect = Rectangle(3, 4)

# We get perimeter for free!
print("Square perimeter: %d" % square.perimeter())
print("Rectangle perimeter: %d" % rect.perimeter())