import math


class Shape:
    def area(self):
        raise NotImplementedError

    def volume(self):
        raise NotImplementedError


class TwoDShape(Shape):
    def volume(self):
        return 0


class ThreeDShape(Shape):
    def area(self):
        raise NotImplementedError


class Square(TwoDShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triangle(TwoDShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Cube(ThreeDShape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3


class Cone(ThreeDShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def area(self):
        return math.pi * self.radius * (self.radius + math.sqrt(self.height ** 2 + self.radius ** 2))

    def volume(self):
        return (1.0 / 3) * math.pi * self.radius ** 2 * self.height


square = Square(4)
triangle = Triangle(3, 5)
cube = Cube(3)
cone = Cone(2, 5)

print('Square area:', square.area())
print('Triangle area:', triangle.area())
print('Cube area:', cube.area())
print('Cube volume:', cube.volume())
print('Cone area:', cone.area())
print('Cone volume:', cone.volume())

