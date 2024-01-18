#!/usr/bin/python3
"""test base module"""


import unittest
from models.base import Base

class test_base(unittest.TestCase):
    """test base module"""
    def test_init_arg(self):
        """arguments pased"""
        obj = Base(2)
        self.assertEqual(obj.id, 2)

    def test_init_noarg(self):
        """no arg passed"""
        obj = Base()
        self.assertEqual(obj.id, 1)
