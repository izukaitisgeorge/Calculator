import unittest
from formula import *


class MyTestCase(unittest.TestCase):

    delta_value = 0.001

    def test_add(self):
        self.assertEqual(add(-1, -2), -3)
        self.assertEqual(add(1, -2), -1)
        self.assertEqual(add(-1, 2), 1)

        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 1), 1)
        self.assertEqual(add(2, 0), 2)

        self.assertAlmostEqual(add(1.2, 2.3), 3.5, delta=self.delta_value)
        self.assertAlmostEqual(add(1.2, 2), 3.2, delta=self.delta_value)
        self.assertAlmostEqual(add(1, 2.3), 3.3, delta=self.delta_value)
        self.assertEqual(add(1, 2), 3)

        self.assertRaises(ValueError, add, 'x', 'y')
        self.assertRaises(ValueError, add, 'x', 2)
        self.assertRaises(ValueError, add, 1, 'y')

    def test_subtract(self):
        self.assertEqual(subtract(-1, -2), 1)
        self.assertEqual(subtract(1, -2), 3)
        self.assertEqual(subtract(-1, 2), -3)

        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(0, 1), -1)
        self.assertEqual(subtract(2, 0), 2)

        self.assertAlmostEqual(subtract(1.2, 2.3), -1.1, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1.2, 2), -0.8, delta=self.delta_value)
        self.assertAlmostEqual(subtract(1, 2.3), -1.3, delta=self.delta_value)
        self.assertEqual(subtract(1, 2), -1)

        self.assertRaises(ValueError, subtract, 'x', 'y')
        self.assertRaises(ValueError, subtract, 'x', 2)
        self.assertRaises(ValueError, subtract, 1, 'y')

    def test_multiply(self):
        self.assertEqual(multiply(-1, -2), 2)
        self.assertEqual(multiply(1, -2), -2)
        self.assertEqual(multiply(-1, 2), -2)

        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(2, 0), 0)

        self.assertAlmostEqual(multiply(1.2, 2.3), 2.76, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1.2, 2), 2.4, delta=self.delta_value)
        self.assertAlmostEqual(multiply(1, 2.3), 2.3, delta=self.delta_value)
        self.assertEqual(multiply(1, 2), 2)

        self.assertRaises(ValueError, multiply, 'x', 'y')
        self.assertRaises(ValueError, multiply, 'x', 2)
        self.assertRaises(ValueError, multiply, 1, 'y')

    def test_divide(self):
        self.assertEqual(divide(-1, -2), 0.5)
        self.assertEqual(divide(1, -2), -0.5)
        self.assertEqual(divide(-1, 2), -0.5)

        self.assertRaises(ZeroDivisionError, divide, 0, 0)
        self.assertEqual(divide(0, 1), 0)
        self.assertRaises(ZeroDivisionError, divide, 2, 0)

        self.assertAlmostEqual(divide(1.2, 2.3), 0.522, delta=self.delta_value)
        self.assertAlmostEqual(divide(1.2, 2), 0.6, delta=self.delta_value)
        self.assertAlmostEqual(divide(1, 2.3), 0.435, delta=self.delta_value)
        self.assertEqual(divide(1, 2), 0.5)

        self.assertRaises(ValueError, divide, 'x', 'y')
        self.assertRaises(ValueError, divide, 'x', 2)
        self.assertRaises(ValueError, divide, 1, 'y')


if __name__ == '__main__':
    unittest.main()
