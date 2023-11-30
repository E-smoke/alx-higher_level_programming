#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv) - 1
    if len == 0:
        print("{} arguments.".format(len))
    elif len == 1:
        print("{} argument:".format(len))
    else:
        print("{} arguments:".format(len))
    index = 0
    i = 1
    for i in sys.argv:
        if index == 0:
            index = index + 1
            continue
        print("{}: {}".format(index, i))
        index = index + 1
