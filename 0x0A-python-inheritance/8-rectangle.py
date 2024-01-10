#!/usr/bin/python3
"""rectangle module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init method"""

        self.integer_validator(self, "width", width)
        self.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
