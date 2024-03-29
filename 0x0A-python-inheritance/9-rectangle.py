#!/usr/bin/python3
"""rectangle module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init method"""

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """arear"""

        return self.__width * self.__height

    def __str___(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
