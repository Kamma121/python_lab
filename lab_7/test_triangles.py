import unittest

from triangles import Triangle
from lab_6.points import Point


class TestTriangle(unittest.TestCase):
    def test_init_valid(self):
        t = Triangle(-1, 3, -3, -3, 2, 1)
        self.assertIsInstance(t, Triangle)

    def test_init_invalid(self):
        with self.assertRaises(ValueError):
            Triangle(0, 0, 1, 1, 2, 2)

    def test_str(self):
        t = Triangle(-1, 3, -3, -3, 2, 1)
        result = str(t)
        self.assertEqual(result, "[(-1, 3), (-3, -3), (2, 1)]")

    def test_repr(self):
        t = Triangle(-1, 3, -3, -3, 2, 1)
        result = repr(t)
        self.assertEqual(result, "Triangle(-1, 3, -3, -3, 2, 1)")

    def test_eq(self):
        t1 = Triangle(-1, 3, -3, -3, 2, 1)
        t2 = Triangle(-1, 3, -3, -3, 2, 1)
        self.assertEqual(t1, t2)

    def test_ne(self):
        t1 = Triangle(-1, 3, -3, -3, 2, 1)
        t2 = Triangle(-10, 31, -3, -3, 2, 1)
        self.assertNotEqual(t1, t2)

    def test_center(self):
        t = Triangle(0, 0, 2, 0, 1, 2)
        result = t.center()
        self.assertEqual(result, Point(1, 2 / 3))

    def test_area(self):
        t = Triangle(-1, 3, -3, -3, 2, 1)
        result = t.area()
        self.assertEqual(result, 11)

    def test_move(self):
        t = Triangle(-1, 3, -3, -3, 2, 1)
        t.move(1, 1)
        self.assertEqual(t, Triangle(0, 4, -2, -2, 3, 2))

    def test_make4(self):
        t = Triangle(2, 2, 4, 0, 0, 0)
        result = t.make4()
        self.assertEqual(result, (
            Triangle(2, 2, 3.0, 1.0, 1.0, 1.0),
            Triangle(1.0, 1.0, 2.0, 0.0, 0, 0),
            Triangle(1.0, 1.0, 3.0, 1.0, 2.0, 0.0),
            Triangle(3.0, 1.0, 4, 0, 2.0, 0.0)))


if __name__ == '__main__':
    unittest.main()
