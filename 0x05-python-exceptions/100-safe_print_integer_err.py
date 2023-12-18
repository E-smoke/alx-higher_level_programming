#!/usr/bin/python3
import sys
def safe_print_integer_err(value):def safe_print_integer(value):
    try:
        print("Exception: {:d}".format(value), file=sys.stderr)
    except Exception:
        return False
    return True
