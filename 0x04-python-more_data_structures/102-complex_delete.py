#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    kitto = [x for x in a_dictionary if a_dictionary[x] == value]
    for i in kitto:
        del a_dictionary[i]
    return a_dictionary
