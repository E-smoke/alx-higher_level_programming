#!/usr/bin/python3
"""test base case"""


import unittest
from models.base import Base

class Test(unittest.TestCase):
   def  test_base(self):
       obj = Base(20)
       self.assertEqual(obj.id, 20)
