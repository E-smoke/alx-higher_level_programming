#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        maximum = my_list[0]
        for num in my_list:
            if maximum < num:
                maximum = num
        return maximum
    else:
        return None
