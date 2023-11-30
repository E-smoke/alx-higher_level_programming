#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    arg = sys.argv[1:]
    for num in arg:
        result = result + int(num)
    print(result)
