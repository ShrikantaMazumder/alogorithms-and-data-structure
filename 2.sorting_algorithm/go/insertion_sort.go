package main

import "fmt"

// Insertion sort

// Best case time complexity: O(n)
// Worst case time complexity: O(n^2)

// Space complexity: O(1)

func main() {
  numbers := []int{5,4,3,2,1};
  insertion_sort(numbers);
  fmt.Println(numbers);

}

func insertion_sort(arr []int) {
	// Suppose our first element is sorted
    // then start looking from second element
	for i := 1; i < len(arr); i++ {
		// now keep current unsorted element in item var
		item := arr[i];
		// it's time to check the exact postion for the unsorted element
        // in sorted list
        // left elements of current unsorted element are sorted.
        // We should check between them
        j := i - 1;

		for j >= 0 && arr[j] > item {
			// create black to replace the small item
            // and move bigger one to right
            arr[j+1] = arr[j];
            j = j-1;
		}

		// in the blank position, we moved small one
        arr[j+1] = item
	}
}