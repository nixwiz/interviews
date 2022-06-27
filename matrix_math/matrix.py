#!/usr/bin/env python

import sys
import yaml

# simple validation function to ensure that incoming yaml matches
# the specification
#
# ---
# matrix:
#  one:
#    - [1, 3, 1]
#    - [1, 0, 0]
#  two:
#    - [0, 0, 5]
#    - [7, 5, 0]

def validate(x):
    if 'matrix' not in x.keys():
        print('top level matrix definition missing from yaml')
        return False

    if 'one' not in x['matrix'].keys():
        print('matrix one definition missing from yaml')
        return False

    if 'two' not in x['matrix'].keys():
        print('matrix two definition missing from yaml')
        return False

    if len(x['matrix']['one']) != len(x['matrix']['two']):
        print('unequal number of rows between matrices one and two')
        return False

    # Since number of columns need to match, pick the first row and make sure the
    # rest are all the same
    ncol = len(x['matrix']['one'][0])
    for row in x['matrix']['one']:
        if len(row) != ncol:
            print('mismatched number of columns in a row of matrix one')
            return False
 
    for row in x['matrix']['two']:
        if len(row) != ncol:
            print('mismatched number of columns in a row of matrix two')
            return False

    return True

def main():
    with open("matrix.yaml", "r") as matrix_file:
        matrix_yaml = yaml.safe_load(matrix_file)
        if not validate(matrix_yaml):
            sys.exit(1)
        for row in range(len(matrix_yaml['matrix']['one'])):
            outstring = "["
            for column in range(len(matrix_yaml['matrix']['one'][row])): 
                outstring += " " + str(matrix_yaml['matrix']['one'][row][column] + matrix_yaml['matrix']['two'][row][column]) + " "
            outstring += "]"
            print(outstring)

if __name__ == '__main__':
    main()

