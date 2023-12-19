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
