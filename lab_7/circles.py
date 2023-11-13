import math

from lab_6.points import Point


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):
        return f"Circle({self.pt.x}, {self.pt.y}, {self.radius})"

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):
        return math.pi * self.radius ** 2

    def move(self, x, y):
        self.pt.x += x
        self.pt.y += y

    def cover(self, other):
        distance = ((self.pt.x - other.pt.x) ** 2 + (self.pt.y - other.pt.y) ** 2) ** 0.5
        new_radius = (self.radius + other.radius + distance) / 2
        new_x = (self.pt.x + other.pt.x) / 2
        new_y = (self.pt.y + other.pt.y) / 2
        return Circle(new_x, new_y, new_radius)
