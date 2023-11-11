import unittest

from points import Point


class TestPoint(unittest.TestCase):

    def test_str(self):
        point = Point(1, 1)
        result = str(point)
        self.assertEqual(result, "(1, 1)")

    def test_repr(self):
        p = Point(1, 1)
        result = repr(p)
        self.assertEqual(result, "Point(1, 1)")

    def test_eq(self):
        p1 = Point(1, 1)
        p2 = Point(1, 1)
        self.assertEqual(p1, p2)

    def test_ne(self):
        p1 = Point(2, 2)
        p2 = Point(3, 4)
        self.assertNotEqual(p1, p2)

    def test_add(self):
        p1 = Point(2, 2)
        p2 = Point(3, 4)
        result = p1 + p2
        self.assertEqual(result, Point(5, 6))

    def test_sub(self):
        p1 = Point(2, 2)
        p2 = Point(3, 4)
        result = p1 - p2
        self.assertEqual(result, Point(-1, -2))

    def test_mul(self):
        p1 = Point(2, 2)
        p2 = Point(3, 4)
        result = p1 * p2
        self.assertEqual(result, 14)

    def test_cross(self):
        p1 = Point(2, 2)
        p2 = Point(3, 4)
        result = p1.cross(p2)
        self.assertEqual(result, 2)

    def test_length(self):
        point = Point(3, 4)
        result = point.length()
        self.assertEqual(result, 5)

    def test_hash(self):
        p = Point(1, 2)
        self.assertEqual(hash(p), hash((1, 2)))


if __name__ == '__main__':
    unittest.main()
