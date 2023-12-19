#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += pow(a, b) / i
        except Exception as e:
            pass
    if b > a:
        result += b + a
    return result
