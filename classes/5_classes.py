class Square(object):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        return self.side + self.side + self.side + self.side


class Rectangle(object):
    def __init__(self, length, width):
        self.l = length
        self.w = width

    def perimeter(self):
        return self.l + self.l + self.w + self.w


square = Square(2)
rect = Rectangle(3, 4)

print("Square perimeter: %d" % square.perimeter())
print("Rectangle perimeter: %d" % rect.perimeter())