#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = (-1 * number) % 10
    last = -1 * last
else:
    last = number % 10
print("Last digit of", number, "is", last, end = " ")
if last > 5:
    print('and is greater than 5')
if last == 0:
    print('and is 0')
if last < 6 and last != 0:
    print('and is less than 6 and not 0')
