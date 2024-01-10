#!/usr/bin/python3
"""write module"""


def append_write(filename="", text=""):
    """write function"""
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)
