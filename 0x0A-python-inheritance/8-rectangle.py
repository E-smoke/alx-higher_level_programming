#!/usr/bin/python3
"""rectangle module"""


from 7-base_geometry.py import BaseGeometry as BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init method"""

        integer_validator(self, "width", width)
        integer_validator(self, "height", height)
        self.__width = width
        self.__height = height