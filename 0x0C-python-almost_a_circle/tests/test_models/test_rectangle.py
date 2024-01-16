#!/usr/bin/python3
"""Unittests for base module"""
import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    """Unit tests for the Base class methods"""

    def setUp(self):
        """Set-up code"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 12)
        self.r3 = Rectangle(10, 2, 0, 0, 12)

    def test_rectangle_id(self):
        """Test id initialization"""
        self.assertEqual(self.r1.id, 1, "incorrect id")
        self.assertEqual(self.r2.id, 2, "incorrect id")
        self.assertEqual(self.r3.id, 12, "incorrect id")

if __name__ == "__main__":
    unittest.main()
