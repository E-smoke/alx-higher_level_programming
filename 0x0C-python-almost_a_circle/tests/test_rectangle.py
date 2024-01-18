#!/usr/bin/python3
"""test rectangle module"""


import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    """test rectangle class"""
    def test_init(self):
        """init no arg"""
        obj = Rectangle(2, 4)
        self.assertEqual(obj.width, 2)
        self.assertEqual(obj.height, 4)

    def test_width_getter(self):
        """test width getter"""
        obj = Rectangle(3, 5)
        self.assertEqual(obj.width, 3)

    def test_height_getter(self):
        """test height getter"""
        obj = Rectangle(3, 5)
        self.assertEqual(obj.height, 5)

    def test_x_getter(self):
        """test x getter"""
        obj = Rectangle(3, 5)
        self.assertEqual(obj.x, 0)

    def test_y_getter(self):
        """test y getter"""
        obj = Rectangle(3, 5)
        self.assertEqual(obj.y, 0)

    def test_setter(self):
        """test getter"""
        obj = Rectangle(3, 5)
        obj.width = 5
        obj.height = 7
        obj.x = 2
        obj.y = 2
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 7)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 2)

    def test_isinstance(self):
        """check instance"""
        self.assertIsInstance(Rectangle(4, 5), Rectangle)

    def test_TypeError(self):
        """Type error"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_AttributeError(self):
        """Attribute Error"""
        with self.assertRaises(AttributeError):
            obj = Rectangle(3, 5)
            obj.__width

    def test_area(self):
        """test area"""
        obj = Rectangle(3, 5)
        self.assertEqual(obj.area(), 15)
