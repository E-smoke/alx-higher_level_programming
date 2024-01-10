#!/usr/bin/python3
"""rectangle module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init method"""

        self.nteger_validator(self, "width", width)
        self.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """arear"""

        return self.__width * self.__height

    def __string__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
