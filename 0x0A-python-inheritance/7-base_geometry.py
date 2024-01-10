#!/usr/bin/python3
"""a module"""


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
        self.name = name
        self.value = value
