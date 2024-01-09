#!/usr/bin/python3
"""this module contains a function lookup()"""


def lookup(obj):
    """this function returns a list of methods and attribute that belongs
    to a function"""
    return dir(obj)
