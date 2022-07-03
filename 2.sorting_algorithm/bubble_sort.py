# Bubble sort

# this will compare between two element
# between n and n+1
# if n is bigger than n+1 then they will be swapped (small to large sort)
# second loop will run (n - i - 1).
# because we don't need to check the last one that already sorted

# Time Complexity
# this one similar to selection sort
# O(n square)

# Space Complexity
# O(1)

# The best case of time complexity for this algo is O(n). If the list is sorted

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                (array[j], array[j+1]) = (array[j+1], array[j])

arr = [5,9,23,53,3,39,100,18]
bubble_sort(arr)
print(arr)