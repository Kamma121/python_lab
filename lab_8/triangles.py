from lab_6.points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        if (x1 - x3) * (y2 - y3) == (x2 - x3) * (y1 - y3):
            raise ValueError("Punkty są współliniowe.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

    @classmethod
    def from_points(cls, points):
        if len(points) != 3:
            raise ValueError("Trójkąt musi być zdefiniowany przez trzy punkty.")
        return cls(points[0].x, points[0].y, points[1].x, points[1].y, points[2].x, points[2].y)

    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)

    def __str__(self):
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y}), ({self.pt3.x}, {self.pt3.y})]"

    def __repr__(self):
        return f"Triangle{self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y}"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x + self.pt3.x) / 3, (self.pt1.y + self.pt2.y + self.pt3.y) / 3)

    def area(self):
        return 0.5 * abs((self.pt2.x - self.pt1.x) * (self.pt3.y - self.pt1.y) - (self.pt2.y - self.pt1.y) * (
                self.pt3.x - self.pt1.x))

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        self.pt3.x += x
        self.pt3.y += y

    def make4(self):
        first_mid = Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)
        second_mid = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)
        third_mid = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        return (
            Triangle(self.pt1.x, self.pt1.y, first_mid.x, first_mid.y, third_mid.x, third_mid.y),
            Triangle(third_mid.x, third_mid.y, second_mid.x, second_mid.y, self.pt3.x, self.pt3.y),
            Triangle(third_mid.x, third_mid.y, first_mid.x, first_mid.y, second_mid.x, second_mid.y),
            Triangle(first_mid.x, first_mid.y, self.pt2.x, self.pt2.y, second_mid.x, second_mid.y)
        )
