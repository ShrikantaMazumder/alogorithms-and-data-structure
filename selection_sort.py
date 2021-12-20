# Selection sort

# Time complexity
# (n-1) + (n-2) + (n-3) + (n-4) ...... 2 + 1
# the sum is n(n-1)/2
# O(n2)

# Space complexity O(1)

def selection_sort(array):
    for i in range(0, len(array)):
        min_index = i
        for j in range(i+1, len(array) - 1):
            if array[min_index] > array[j]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])

arr = [40, 43, 20, 33, 53, 34, 32, 67]

selection_sort(arr)

print(arr)
