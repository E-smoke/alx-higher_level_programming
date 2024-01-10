#!/usr/bin/python3
"""write module"""


def write_file(filename="", text=""):
    """write function"""
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
