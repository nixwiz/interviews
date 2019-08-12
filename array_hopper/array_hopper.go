package main

import "bufio"
import "fmt"
import "os"
import "sort"
import "strconv"

// Structure used to store different iterations while finding the solution
type possible struct {
	list []int
}

func main() {

	// read stdin file into an array
	array_of_ints, err := create_array()
	if err != nil {
		fmt.Println("failure")
		os.Exit(1)
	}

	// run the solution
	solution := array_hopper(array_of_ints)

	if solution == nil {
		fmt.Println("failure")
		os.Exit(1)
	}

	// print the solution (it is returned in reverse order)
	for index := len(solution) - 1; index >= 0; index-- {
		fmt.Printf("%d, ", solution[index])
	}
	fmt.Printf("out\n")
	os.Exit(0)
}

// Create the array from the specified file
func create_array() ([]int, error) {

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanLines)

	var lines []int

	for scanner.Scan() {
		i, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return nil, err
		}
		lines = append(lines, i)
	}

	return lines, nil
}

// actually find the solution
func array_hopper(array []int) []int {

	var solution []int

	array_len := len(array)

	// build a list of possible hops from each index
	possibles := make([]possible, array_len-1)

	for index := 0; index < array_len-1; index++ {
		// can't jump from this index, skip it
		if array[index] == 0 {
			continue
		}
		for jump := 1; jump <= array[index]; jump++ {
			hop := index + jump
			if hop < array_len {
				possibles[index].list = append(possibles[index].list, hop)
			} else {
				// We are past the final index, no need to add it to the list
				break
			}
		}
	}

	// The above creates the follwing from the sample input
	// possibles[0] = [1 2 3 4 5]
	// possibles[1] = [2 3 4 5 6 7]
	// possibles[2] = []
	// possibles[3] = [4 5 6 7]
	// possibles[4] = [5 6]
	// possibles[5] = [6 7 8 9]
	// possibles[6] = [7]
	// possibles[7] = []
	// possibles[8] = []

	// create an intermediate list, starting from the end and going backwards
	// showing the jumps possible from the end
	backhops := make([]possible, array_len)

	for index := array_len - 1; index >= 0; index-- {
		for jump := index - 1; jump >= 0; jump-- {
			if contains(possibles[jump].list, index) {
				backhops[index].list = append(backhops[index].list, jump)
			}
		}
	}

	// The above creates the following from the sample input
	// read as can get to this index from these indices
	// backhops[0] = []
	// backhops[1] = [1 0]
	// backhops[2] = [1 0]
	// backhops[4] = [3 1 0]
	// backhops[5] = [4 3 1 0]
	// backhops[6] = [5 4 3 1]
	// backhops[7] = [6 5 3 1]
	// backhops[8] = [5] 
	// backhops[9] = [5]

	// Build the solution list, starting with the final index
	index := array_len - 1
	solution = append(solution, index)

	// Start going backwards, selecting the smallest index to jump back to (list is sorted)
	for index != 0 {
		// If we can't get there, fail
		if len(backhops[index].list) == 0 {
			return nil
		}
		// Add the rightmost (lowest) value for our index
		// From the sample input with index 9, set to 5 and add to solution
		// Repeat for 5 and get 0
		solution = append(solution, backhops[index].list[len(backhops[index].list)-1])
		index = backhops[index].list[len(backhops[index].list)-1]
	}

	// This creates the following from the sample input
	// solution = [9, 5, 0]
	return solution
}

// See if int in in the provided list of ints (assumes list is sorted)
func contains(list []int, i int) bool {
	index := sort.SearchInts(list, i)
	if index != len(list) {
		return true
	}
	return false
}
