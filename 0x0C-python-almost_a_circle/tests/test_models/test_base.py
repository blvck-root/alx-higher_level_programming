#!/usr/bin/python3
"""Unittests for base module"""
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    """Unit tests for the Base class methods"""

    def setUp(self):
        """Set-up code"""
        self.b1 = Base()
        self.b2 = Base(12)
        self.b3 = Base()

    def test_base_id(self):
        """Test id initialization"""
        self.assertEqual(self.b1.id, 1, "incorrect id")
        self.assertEqual(self.b2.id, 12, "incorrect id")
        self.assertEqual(self.b3.id, 2, "incorrect id")

    def test_base_init(self):
        """Test the init method"""
        self.assertIsInstance(self.b1, Base)

    def test_base_nb_objects(self):
        """Test __nb_objects attribute"""
        self.assertEqual(Base._Base__nb_objects, self.b3.id)

    def test_base_to_json_string(self):
        """Test to_json_string method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        a_dict = r1.to_dictionary()
        json_string = json.dumps([a_dict])
        json_listdict = r1.to_json_string([a_dict])
        self.assertEqual(json_string, json_listdict)

    def test_base_save_to_file(self):
        """Test save_to_file method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        a_dict = [r1.to_dictionary(), r2.to_dictionary()]
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            list_dict = json.loads(file.read())
        self.assertEqual(a_dict, list_dict)

    def test_base_from_json_string(self):
        """Test from_json_string method"""
        Base._Base__nb_objects = 0
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_base_create(self):
        """Test the create method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)

    def test_base_load_from_file(self):
        """Test load_from_file method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertIsInstance(list_rectangles_output, list)
        for rect in list_rectangles_input:
            self.assertIsInstance(rect, Rectangle)
        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertIsInstance(list_squares_output, list)
        for sqr in list_squares_input:
            self.assertIsInstance(sqr, Square)
        for sqr in list_squares_output:
            self.assertIsInstance(sqr, Square)

    def tearDown(self):
        """Clean-up code"""
        Base._Base__nb_objects = 0


if __name__ == "__main__":
    unittest.main()
