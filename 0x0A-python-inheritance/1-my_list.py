#!/usr/bin/python3
"""module"""


class MyList(list):
    """class"""

    def print_sorted(self):
        """method"""
        sorted_list = sorted(self)
        print(sorted_list)
