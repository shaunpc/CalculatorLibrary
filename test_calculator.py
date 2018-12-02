import unittest
import calculator

"""
    Unit tests for the calculator library
"""


class TestCalculator(unittest.TestCase):

    def test_addition1(self):
        self.assertEqual(4, calculator.add(2, 2))

    def test_addition2(self):
        self.assertNotEqual(6, calculator.add(6, 2))

    def test_subtraction1(self):
        self.assertEqual(2, calculator.subtract(4, 2))

    def test_subtraction2(self):
        self.assertNotEqual(3, calculator.subtract(8, 3))

    def test_multiplication1(self):
        self.assertEqual(12, calculator.multiply(2, 6))

    def test_multiplication2(self):
        self.assertNotEqual(22, calculator.multiply(3, 6))


if __name__ == '__main__':
    unittest.main(verbosity=2)

