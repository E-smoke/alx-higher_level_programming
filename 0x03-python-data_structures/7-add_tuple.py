#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a) - 1
    b = len(tuple_b) - 1
    list0 = []
    for i in range(2):
        if a < i:
            av = 0
        else:
            av = tuple_a[i]
        if b < i:
            bv = 0
        else:
            bv = tuple_b[i]
        list0.append(av + bv)
    return tuple(list0)
