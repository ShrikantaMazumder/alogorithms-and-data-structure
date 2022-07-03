# Bubble sort

# this will compare between two element
# between n and n+1
# if n is bigger than n+1 then they will be swapped (small to large sort)
# second loop will run (n - i - 1).
# because we don't need to check the last one that already sorted

# Time Complexity
# this one similar to selection sort
# O(n^2)

# Space Complexity
# O(1)

# The best case of time complexity for this algo is O(n). If the list is sorted

def bubble_sort(array):
    # let start the loop from the first element
    # and run it till the last element
    for i in range(len(array)):
        # Consider it as a right pointer
        # We won't consider the sorted elements
        # that's why stop the inner loop before sorted elements
        for j in range(0, len(array) - i - 1):
            # check if current element is greater than next one.
            # then swap it with next one
            # The bigger ones will go to the last place respectively
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])

arr = [5,9,23,53,3,39,100,18]
bubble_sort(arr)
print(arr)