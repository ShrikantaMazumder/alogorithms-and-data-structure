// Selection sort

// Time complexity
// (n-1) + (n-2) + (n-3) + (n-4) ...... 2 + 1
// the sum is n(n-1)/2
// O(n^2)

// Space complexity O(1)

package main;
import "fmt";

func main()  {
	numbers := []int{40, 43, 20, 33, 53, 34, 32, 67};
	selection_sort(numbers);
	fmt.Println(numbers);
}

func selection_sort(arr []int) {
	// to achieve this algorithm we need two algorithm.
	// Outer one for first pointer which help us to keep smallest number's index respectively.
	// start from 0 and end it to second last element
	// because next loop will go to last element
	for i := 0; i < len(arr)-1; i++ {
		// Let's think our i is the smallest number currently
		min_index := i;

		// Here we start the loop from the next element of i index and run untill last element
		for j := i+1; j < len(arr); i++ {
			// here comparing current minimum element with current iterating element of inner loop
            // if current iterating element if smaller than current min element then 
            // we considering current iterating element is the min element
			if arr[min_index] > arr[j] {
				min_index = j;
			}
		}
		 // at the end, if current min is same as i index. we don't need to swap
        // Because both are in same position
        // Else swap it
		if min_index != i {
			temp := arr[i];
			arr[i] = arr[min_index];
			arr[min_index] = temp;
		}
	}
}