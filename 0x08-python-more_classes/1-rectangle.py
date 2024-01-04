#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """class Rectangle"""

    @property
    def width(self):
        """return width"""
        return self._width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """return width"""
        return self._height

    @height.setter
    def height(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._height = value

    def __init__(self, width=0, height=0):
        """init mehtod"""
        self._width = width
        self._height = height
