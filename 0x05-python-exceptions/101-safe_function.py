#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    r = None
    try:
        r = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
    return r
