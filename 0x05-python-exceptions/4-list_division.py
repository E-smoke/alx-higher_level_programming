#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    for idx in range(list_length):
        try:
            q = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            q = 0
        except TypeError:
            print("wrong type")
            q = 0
        except IndexError:
            print("out of range")
            q = 0
        finally:
            nl.append(q)
    return nl
