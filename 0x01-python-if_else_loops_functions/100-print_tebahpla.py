#!/usr/bin/python3
a = 1
for i in range(ord('z'), ord('a') - 1, -1):
    if a == 1:
        print("{}".format(chr(i)), end='')
        a = 0
    else:
         print("{}".format(chr(i - 32)), end='')
         a = 1
