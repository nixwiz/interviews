#!/usr/bin/python

# Draw a tree of hashes using supplied number of levels

import sys

n = int(sys.argv[1])

for i in range(1, n + 1):
    print(" " * (n - i) + "#" * ((i * 2) - 1))

print(" " * (n - 1) + "#")
