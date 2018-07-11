#!/usr/bin/python

# Originally written in a live on-line coding session
#
# Objective, given an array, test for duplicate entries
#
# The first two solutions were ones I did immediately online
# The third was what I came up with after a few minutes of offline
# further learning


def testdupes(a):
    exists = []
    for member in a:
        if member in exists:
            return True
        else:
            exists.append(member)

    return False


def testdupes2(a):
    exists2 = {}
    for member in a:
        if member in exists2.keys():
            return True
        else:
            exists2[member] = 1

    return False


def testdupes3(a):
    for member in a:
        if a.count(member) > 1:
            return True
    return False


array_a = ["sun", "moon", "stars", "sun"]
array_b = ["sun", "moon", "stars"]

if testdupes(array_a):
    print ("True")
else:
    print ("False")

if testdupes(array_b):
    print ("True")
else:
    print ("False")

if testdupes2(array_a):
    print ("True")
else:
    print ("False")

if testdupes2(array_b):
    print ("True")
else:
    print ("False")

print(testdupes3(array_a))
print(testdupes3(array_b))
