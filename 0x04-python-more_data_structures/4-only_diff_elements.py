#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff = set()
    for num in set_1:
        if num not in set_2:
            diff.add(num)
    for num in set_2:
        if num not in set_1:
            diff.add(num)
    return diff
