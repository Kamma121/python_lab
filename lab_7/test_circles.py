import unittest

from circles import Circle


class TestCircle(unittest.TestCase):
    def test_init_valid(self):
        c = Circle(0, 0, 5)
        self.assertIsInstance(c, Circle)

    def test_init_invalid(self):
        with self.assertRaises(ValueError):
            Circle(0, 0, -5)

    def test_eq(self):
        c1 = Circle(0, 0, 4)
        c2 = Circle(0, 0, 4)
        self.assertEqual(c1, c2)

    def test_ne(self):
        c1 = Circle(0, 0, 4)
        c2 = Circle(1, 1, 4)
        self.assertNotEqual(c1, c2)

    def test_area(self):
        c = Circle(0, 0, 4)
        result = c.area()
        self.assertAlmostEqual(result, 50.26548, places=5)

    def test_move(self):
        c = Circle(0, 0, 4)
        c.move(1, 1)
        self.assertEqual(c, Circle(1, 1, 4))

    def test_cover(self):
        c1 = Circle(0, 0, 4)
        c2 = Circle(4, 0, 4)
        result = c1.cover(c2)
        self.assertEqual(result, Circle(2, 0, 6))


if __name__ == '__main__':
    unittest.main()
