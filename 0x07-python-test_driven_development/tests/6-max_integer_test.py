#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test max_integer function.
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([10, -20, 30, -40]), 30)
        self.assertEqual(max_integer([50]), 50)
        self.assertEqual(max_integer([0, 0.5, -5, -10]), 0.5)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-2, -6, -8, -4]), -2)
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer({0: 23, 1: 1, 2: 10, 3: 0, 4: -1}), 23)

        with self.assertRaises(TypeError):
            max_integer(3)
        with self.assertRaises(TypeError):
            max_integer([1, 2, 1000, "string"])
        with self.assertRaises(KeyError):
            max_integer({"zero": 23, 1: 1, 2: 10, 3: 0, 4: -1})

if __name__ == "__main__":
    unittest.main()
