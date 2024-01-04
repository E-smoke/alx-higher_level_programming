#!/usr/bin/python3
"""rectangle class"""


class Rectangle:
    """class Rectangle"""

    number_of_instances = 0

    print_symbol = "#"

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return width"""
        return self.__height

    @height.setter
    def height(self, value):
        """set width"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """init mehtod"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        """area"""
        return self.width * self.height

    def perimeter(self):
        """perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return 2 * self.height + 2 * self.width

    def __str__(self):
        """str rep method"""
        rep = ""
        append = "\n"
        if self.width == 0 or self.height == 0:
            return rep
        else:
            for i in range(self.height):
                if i == self.height - 1:
                    append = ""
                for j in range(self.width):
                    rep = "{}{}".format(rep, self.print_symbol)
                rep += append
            return rep

    def __repr__(self):
        """repr"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
