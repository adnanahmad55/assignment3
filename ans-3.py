import math


class Shape:
    def area(self):
        """Abstract method to be overridden by subclasses"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Area of Circle (radius 5): {circle.area():.2f}")
print(f"Area of Rectangle (4x6): {rectangle.area()}")

