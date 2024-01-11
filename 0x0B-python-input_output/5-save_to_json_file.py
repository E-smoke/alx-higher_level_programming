#!/usr/bin/python3
"""json file python"""


import json

def save_to_json_file(my_obj, filename):
    """json file function"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
