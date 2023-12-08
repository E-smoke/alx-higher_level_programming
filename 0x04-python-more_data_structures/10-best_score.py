#!/usr/bin/python3
def best_score(a_dictionary):
    max = ""
    maxv = 0
    if a_dictionary:
        for k in a_dictionary:
            if a_dictionary[k] > maxv:
                maxv = a_dictionary[k]
                max = k
        return max
    return None
