#!/usr/bin/python

# Draw a tree of hashes using supplied number of levels
# Second revision, using function

import sys


def tree(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "#" * ((i * 2) - 1))

    print(" " * (n - 1) + "#")

if __name__ == "__main__":
    tree(int(sys.argv[1]))
