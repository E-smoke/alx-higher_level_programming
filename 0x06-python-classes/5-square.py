#!/usr/bin/python3
"""this module defines an empty class name square"""


class Square:
    """this is an empty class called Square"""
    def __init__(self, size=0):
        """initfunction to initialize size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns area of a square"""
        return self.__size ** 2

    @property
    def size(self):
        """To retrieve value of size"""
        return self.__size

    @size.setter
    def size(self, new_size):
        """To set the value of size"""
        if type(new_size) != int:
            raise TypeError("size must be an integer")
        if new_size < 0:
            raise ValueError("size must be >= 0")
        self.__size = new_size

    def my_print(self):
        """prints the square"""
        if self.__size = 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end='')
            print()
