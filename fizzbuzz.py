#!/usr/bin/python

# Classic fuzzbuzz

import sys

for i in range(1, (int(sys.argv[1]) + 1)):
    if (i % 3 == 0) and (i % 5 == 0):
        print("fizzbuzz")
    elif (i % 3 == 0):
        print("fizz")
    elif (i % 5 == 0):
        print("buzz")
    else:
        print(i)
