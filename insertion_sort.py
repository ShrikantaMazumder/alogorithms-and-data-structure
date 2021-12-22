# Insertion sort

# Best case time complexity: O(n)
# Worst case time complexity: O(n square)

# Space complexity: O(1)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

data = [9, 5, 1, 4, 3]
insertion_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
        