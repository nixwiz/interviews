# interviews
Code from whiteboard (physical or virtual) interviews or otherwise, even after the fact

* Tree programs produce hash trees based on specified number of levels

```
    └─▪ ./tree1.py 6
         #
        ###
       #####
      #######
     #########
    ###########
         #
```
* The old standy, fizzbuzz
```
└─▪ ./fizzbuzz.py 20
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
```
* Test for duplicate members of an array (3 different methods)
```
    Given arrays:
    array_a = ["sun", "moon", "stars", "sun"]
    array_b = ["sun", "moon", "stars"]

    └─▪ ./dupes.py 
    True
    False
    True
    False
    True
    False
```
* Report on active IAM user keys over 60 days old
```
    └─▪ ./expired_keys.sh 
    todd.campbell keys over 60 days old
```
* Please add two matrix together using the yaml file as input and display the result:
 
```
---
matrix:
  one:
    - [1, 3, 1]
    - [1, 0, 0]
  two:
    - [0, 0, 5]
    - [7, 5, 0]
```
