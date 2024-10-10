"""
    Testing functions
"""

from unittest import TestCase

from functions import divide


class TestFunctions(TestCase):
    """TestFunctions"""

    def test_divide_result(self):
        """test equality: positive"""
        dividend = 15
        divisor = 3
        expected_result = 5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_negative(self):
        """test equality: negative"""
        dividend = 15
        divisor = -3
        expected_result = -5.0
        self.assertAlmostEqual(divide(dividend, divisor), expected_result, delta=0.0001)

    def test_divide_dividend_zero(self):
        """test equality: zero"""
        dividend = 0
        divisor = 5
        expected_result = 0
        self.assertEqual(divide(dividend, divisor), expected_result)

    # def test_divide_error_on_zero(self):
    #     with self.assertRaises(ValueError):
    #         divide(25, 0)

    # def test_multiply_empty(self):
    #     with self.assertRaises(ValueError):
    #         multiply()

    # def test_multiply_single_value(self):
    #     expected = 15
    #     self.assertEqual(multiply(expected), expected)

    # def test_multiply_zero(self):
    #     expected = 0
    #     self.assertEqual(multiply(expected), expected)

    # def test_multiply_result(self):
    #     inputs = (3, 5)
    #     expected = 15
    #     self.assertEqual(multiply(*inputs), expected)

    # def test_multiply_results_with_zero(self):
    #     inputs = (3, 5, 0)
    #     expected = 0
    #     self.assertEqual(multiply(*inputs), expected)

    # def test_multiply_negative(self):
    #     inputs = (3, -5, 2)
    #     expected = -30
    #     self.assertEqual(multiply(*inputs), expected)

    # def test_multiply_floats(self):
    #     inputs = (3.0, 2)
    #     expected = 6.0
    #     self.assertEqual(multiply(*inputs), expected)
