#!/usr/bin/python3
"""Unittests for rectangle module"""
import sys
import json
import unittest
from io import StringIO
from models.base import Base
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

    def test_rectangle_init(self):
        """Test init method"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(2, 10)
        self.assertIsInstance(r2, Rectangle)

    def test_rectangle_nb_objects(self):
        """Test __nb_objects attribute"""
        Base._Base__nb_objects = 0
        r3 = Rectangle(10, 2, 0, 0)
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.id, 2)

    def test_rectangle_getters_and_setters(self):
        """Test getters and setters"""
        Base._Base__nb_objects = 0
        r5 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r5.width, 10)
        self.assertEqual(r5.height, 2)
        self.assertEqual(r5.x, 0)
        self.assertEqual(r5.y, 0)

    def test_rectangle_errors(self):
        """Test with invalid attributes"""
        Base._Base__nb_objects = 0
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.width = "2"
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "2"
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3, 1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.y = {}
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_rectangle_area(self):
        """Test area method"""
        Base._Base__nb_objects = 0
        r6 = Rectangle(3, 2)
        self.assertEqual(r6.area(), r6.width * r6.height)

    def test_rectangle_display(self):
        """Test display method"""
        Base._Base__nb_objects = 0
        r7 = Rectangle(4, 6)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r7.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string,
                         "####\n####\n####\n####\n####\n####\n")

    def test_rectangle_str(self):
        """Test __str__ method"""
        Base._Base__nb_objects = 0
        r8 = Rectangle(4, 6, 2, 1, 12)
        r9 = Rectangle(5, 5, 1)
        string1 = r8.__str__()
        string2 = r9.__str__()
        self.assertEqual(string1,
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(string2,
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_rectangle_display_xy(self):
        """Test display method with (x, y) offsets"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3, 2, 2)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r1.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, "\n\n  ##\n  ##\n  ##\n")
        r2 = Rectangle(3, 2, 1, 0)
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        r2.display()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        self.assertEqual(result_string, " ###\n ###\n")

    def test_rectangle_update(self):
        """Test update method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 4/5 - 2/3")

    def test_rectangle_update_kwargs(self):
        """Test update with kwargs"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        string = r1.__str__()
        self.assertEqual(string, "[Rectangle] (89) 1/3 - 4/2")

    def test_rectangle_to_dictionary(self):
        """Test to_dictionary method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        a_dict = {'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}
        self.assertTrue(r1_dictionary == a_dict)

    def test_empty_args(self):
        """Test with empty arguments"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = None
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r1.width = ""

    def tearDown(self):
        """Clean-up code"""
        Base._Base__nb_objects = 0


if __name__ == "__main__":
    unittest.main()
