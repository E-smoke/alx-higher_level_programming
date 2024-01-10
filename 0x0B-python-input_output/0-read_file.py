#!/usr/bin/python3
"""read a txt file in utf mode"""


def read_file(filename=""):
    """read function"""
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read(), end="")
