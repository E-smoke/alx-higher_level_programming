#!/usr/bin/python3
"""rectangle module"""


class BaseGeometry:
    """base geometry"""

    def area(self):
        """a function"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a function"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """init method"""

        self.integer_validator(self, "width", width)
        self.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
