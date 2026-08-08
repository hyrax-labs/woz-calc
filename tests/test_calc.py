"""Tests for the arithmetic layer in :mod:`calc`."""

import unittest

from calc import add, divide, multiply, subtract


class AddTests(unittest.TestCase):
    def test_add_positive_operands(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_operands(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_zero_operand(self):
        self.assertEqual(add(0, 5), 5)

    def test_add_float_result(self):
        self.assertEqual(add(1.5, 2.25), 3.75)


class SubtractTests(unittest.TestCase):
    def test_subtract_positive_operands(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_negative_operands(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_zero_operand(self):
        self.assertEqual(subtract(0, 5), -5)

    def test_subtract_float_result(self):
        self.assertEqual(subtract(5.5, 2.25), 3.25)


class MultiplyTests(unittest.TestCase):
    def test_multiply_positive_operands(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_multiply_negative_operands(self):
        self.assertEqual(multiply(-4, 3), -12)

    def test_multiply_zero_operand(self):
        self.assertEqual(multiply(0, 5), 0)

    def test_multiply_float_result(self):
        self.assertEqual(multiply(1.5, 2.0), 3.0)


class DivideTests(unittest.TestCase):
    def test_divide_positive_operands(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_negative_operands(self):
        self.assertEqual(divide(-6, 3), -2)

    def test_divide_zero_numerator(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_float_result(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero_raises_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError) as ctx:
            divide(1, 0)
        self.assertIn("divide by zero", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
