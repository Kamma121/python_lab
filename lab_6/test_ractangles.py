import unittest

from rectangles import Rectangle
from points import Point


class TestTriangle(unittest.TestCase):

    def test_str(self):
        r = Rectangle(1, 2, 3, 4)
        result = str(r)
        self.assertEqual(result, "[(1, 2), (3, 4)]")

    def test_repr(self):
        r = Rectangle(1, 2, 3, 4)
        result = repr(r)
        self.assertEqual(result, "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1, r2)

    def test_ne(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(2, 2, 3, 3)
        self.assertNotEqual(r1, r2)

    def test_center(self):
        r = Rectangle(1, 2, 3, 4)
        result = r.center()
        self.assertEqual(result, Point(2, 3))

    def test_area(self):
        r = Rectangle(1, 2, 3, 4)
        result = r.area()
        self.assertEqual(result, 4)

    def test_move(self):
        r = Rectangle(1, 2, 3, 4)
        r.move(1, 1)
        self.assertEqual(r, Rectangle(2, 3, 4, 5))


if __name__ == '__main__':
    unittest.main()
