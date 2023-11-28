#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            char1 = chr(ord(char) - 32)
        else:
            char1 = char
        print(char1, end='')
    print()
