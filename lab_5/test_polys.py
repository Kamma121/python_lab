import unittest
from polys import add_poly, sub_poly, mul_poly, is_zero, eq_poly, eval_poly, combine_poly, pow_poly, diff_poly


class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]
        self.p2 = [0, 0, 1]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])

    def test_mul_poly(self):
        self.assertEqual(mul_poly(self.p1, self.p2), [0, 0, 0, 1])

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 0, 0]))
        self.assertFalse(is_zero(self.p1))

    def test_eq_poly(self):
        self.assertTrue(eq_poly([1, 2, 3], [1, 2, 3]))
        self.assertFalse(eq_poly([0, 1, 2], [1, 2]))

    def test_eval_poly(self):
        self.assertEqual(eval_poly([1, 2, 3, 4], 2), 49)
        self.assertEqual(eval_poly([0, 0, 0], 1), 0)

    def test_combine_poly(self):
        self.assertEqual(combine_poly(self.p2, self.p2), [0, 0, 0, 0, 1])
        self.assertEqual(combine_poly([5, 8, 2, 1], [0, 0, 1]), [5, 0, 8, 0, 2, 0, 1])
        self.assertEqual(combine_poly(self.p1, self.p2), self.p2)

    def test_pow_poly(self):
        self.assertEqual(pow_poly([0, 0, 1], 2), [0, 0, 0, 0, 1])
        self.assertEqual(pow_poly([1, 1], 2), [1, 2, 1])

    def test_diff_poly(self):
        self.assertEqual(diff_poly([5, 2, 4, 5]), [2, 8, 15])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()  # uruchamia wszystkie testy
