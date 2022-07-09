package main

import (
	"fmt"
)

func main() {
	// Unsorted array
	numbers := []int{23, 2, 34, 54, 13, 64, 31, 86}
	// Sort it here
	merge_sort(numbers)
	// Let's check it sorted or not
	fmt.Println(numbers)
}

func merge_sort(arr []int) {
	if len(arr) > 1 {
		// Divide the array
		// NB: it always floor the value
		r := len(arr) / 2
		L := []int{}
		R := []int{}

		// assign left half of the array in L
		for i := 0; i < r; i++ {
			L = append(L, arr[i])
		}

		// assign right half of the array in R
		for i := r; i < len(arr); i++ {
			R = append(R, arr[i])
		}

		// We should split the array until array length is 1 or 0
		// So this repeatative job we can do with the help of Recursion
		merge_sort(L)
		merge_sort(R)

		// Merge starts from here
		// Taking 3 variables with 0 value to use these later
		var i, j, k int = 0, 0, 0

		// Iterate both L and R arrays same time
		// So that it can possible to compare elements between two.
		// This loop will run till both arrays same length
		for i < len(L) && j < len(R) {
			// check L(i) is less than R[i]
			if L[i] < R[j] {
				// if true then manipulate the main array, that is passed as argument
				// So K-th index of main array should be the L[i]
				arr[k] = L[i]
				// increament the value of i so that can procced with next element of L array
				i++
			} else {
				// if false that means R[i] is smaller or equal of L[i]
				// so update main array k element by the value of R[j]
				arr[k] = R[j]
				// increament the value of j so that can procced with next element of R array
				j++
			}
			// k should be increament by 1. Because k is keeping track of the position of main array.
			k++
		}

		// If program comes here, it means our both are already merged
		// OR
		// Some elements are left on Left(L) array or Right(R) arrary
		// Because its possible one array bigger or smaller than other array (Between L & R)
		// But out previous loop only run untill common length of both arrays. So something could be missing

		// Here this loop run until i is less than length of L
		// Here may be i is not 0. Because we also increamented i in previous loop.
		// So it will continue after the element that we already checked.
		for i < len(L) {
			// Update main array with L[i]
			arr[k] = L[i]
			// Go to next element
			i++
			// Update k for main array trac
			k++
		}

		// this one is same as Left(L) array. Now we are doing this for Right(R) array
		for j < len(R) {
			arr[k] = R[j]
			j++
			k++
		}
	}
}
