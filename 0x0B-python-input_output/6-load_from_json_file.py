#!/usr/bin/python3
"""json file python"""


import json


def load_from_json_file(filename):
    """json file function"""
    with open(filename, "r") as f:
        return json.load(f)
