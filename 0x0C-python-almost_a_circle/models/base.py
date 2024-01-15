#!/usr/bin/python3
"""base class model"""


class base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            base.__nb_objects = base.__nb_objects + 1
            self.id = base.__nb_objects
