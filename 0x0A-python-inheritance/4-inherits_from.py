#!/usr/bin/python3
"""a module"""


def inherits_from(obj, a_class):
    """a function"""

    return type(obj) != a_class and isinstance(obj, a_class)
