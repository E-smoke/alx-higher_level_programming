#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    nl = []
    ln = len(my_list_2)
    if ln < len(my_list_1):
        ln = len(my_list_1)
    for idx in range(ln):
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
