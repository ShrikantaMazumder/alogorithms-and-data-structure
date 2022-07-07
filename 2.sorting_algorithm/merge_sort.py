# Time Complexity

# Each time we split the array in two. That's why it's complexity is: O(log n)
# And then we merge these splitted arrays, it's complexity is: O(n)
# So overall complexity is: O(log n * n) = O(n log n)

# Space Complexity: O(n)

def merge_sort(arr):
    # Do split and merge if there are more than one element in array
    if len(arr) > 1:
        # Divide the length of array
        r = len(arr)//2
        # Keep left half of the array in L
        L = arr[:r]

        # right half of the array in R
        R = arr[r:]

        # We should split the array until array length is 1 or 0
        # So this repeatative job we can do with the help of Recursion

        # Here again split the Left array
        merge_sort(L)

        # And here is Right array
        merge_sort(R)

        # Merge starts from here
        # Taking 3 variables with 0 value to use these later
        i = j = k = 0

        # Iterate both L and R arrays same time 
        # So that it can possible to compare elements between two.
        # This loop will run till both arrays same length
        while i < len(L) and j < len(R):
            # check L(i) is less than R[i]
            if L[i] < R[j]:
                # if true then manipulate the main array, that is passed as argument
                # So K-th index of main array should be the L[i]
                arr[k] = L[i]
                # increament the value of i so that can procced with next element of L array
                i += 1
            else:
                # if false that means R[i] is smaller or equal of L[i]
                # so update main array k element by the value of R[j]
                arr[k] = R[j]

                # increament the value of j so that can procced with next element of R array
                j += 1
            # k should be increament by 1. Because k is keeping track of the position of main array. 
            k += 1

        # If program comes here, it means our both are already merged
        # OR
        # Some elements are left on Left(L) array or Right(R) arrary
        # Because its possible one array bigger or smaller than other array (Between L & R)
        # But out previous loop only run untill common length of both arrays. So something could be missing

        # Here this loop run until i is less than length of L
        # Here may be i is not 0. Because we also increamented i in previous loop. 
        # So it will continue after the element that we already checked.
        while i < len(L):
            # Update main array with L[i]
            arr[k] = L[i]
            # Go to next element
            i += 1
            # Update k for main array trac
            k += 1

        # this one is same as Left(L) array. Now we are doing this for Right(R) array
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Unsorted array
numbers = [31, 34, 21, 53, 5, 6, 1, 45, 76]
# Sort it here
merge_sort(numbers)
# Let's check it sorted or not
print(numbers)
