class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

circle = Circle(5)
rectangle = Rectangle(4, 6)
square = Square(3)

print("Area of Circle:", circle.area())
print("Area of Rectangle:", rectangle.area())
print("Area of Square:", square.area())
