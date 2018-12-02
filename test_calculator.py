import unittest
import calculator

"""
    Unit tests for the calculator library
"""


class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(4, calculator.add(2, 2))

    def test_subtraction(self):
        self.assertEqual(2, calculator.subtract(4, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)

