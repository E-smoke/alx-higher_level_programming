#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list0 = my_list[:]
    for i in range(len(list0)):
        if list0[i] == search:
            list0[i] = replace
    return list0
