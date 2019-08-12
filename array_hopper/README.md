ArrayHopper
==========

## Problem Description

You are given an array of integers with values greater than or equal to 0, for example: 
 
> [5, 6, 0, 4, 2, 4, 1, 0, 0, 4] 
 
You will develop and implement an algorithm to traverse the array in the shortest number of “hops” 
starting at index 0, where traversal is defined as follows: 
 
- Start at the first (0th) index of the array, look at the array value there, and you can hop forward to any 
array index that is no farther than that value away. So in this example, you start at index 0 containing 
the value 5 and can now consider hopping to any of indices 1 through 5 inclusive. 
- If you choose to hop to index 3, it contains the value 4 and you can next hop up to 4 more spots from 
your current index (3)—so you now consider indices 4 through 7 as next steps in your sequence. 
- Once you can legally hop beyond the last array element, you have successfully traversed the array. 
 
Your job is to compute the minimum-length sequence of hops that successfully traverses the 
array starting from index 0, or determine that there is no such sequence. 
 
Your algorithm must identify a minimum-hops solution, but can choose arbitrarily among solutions with the 
same number of hops. 
 
Your program will implement the algorithm and write a solution to the standard output stream on a single 
line identifying the array indices that comprise a solution path, with the indices separated by commas. 
 
For this example, the following would be valid output: 
 
> 0, 5, 9, out 

(Note that your output is a sequence of array indices, not a sequence of hop lengths.)

- Your program may be written in the language of your choice. 
- It must accept its input file on STDIN
- The input file will contain the array for a single problem. 
	- One integer per line, with no brackets or commas. 
	- The input array will likely be large in our testing, so performance is important. 
- If there is no solution, the program should write the string “failure” to the standard output stream, 
followed by a newline character.  

