#!/usr/bin/python3
def pow(a, b):
    if b == 0 and a != 0:
        return 1
    elif b != 0 and a == 0:
        return 0
    elif b > 0:
        r = 1
        for i in range(b):
            r = r * a
        return r
    else:
        r = 1
        for i in range(-1 * b):
            r = r * a
        return 1 / r
