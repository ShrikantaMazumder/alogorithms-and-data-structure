# Insertion sort

# Best case time complexity: O(n)
# Worst case time complexity: O(n^2)

# Space complexity: O(1)

def insertion_sort(array):
    # Suppose our first element is sorted
    # then start looking from second element
    for i in range(1, len(array)):
        # now keep current unsorted element in key var
        key = array[i]

        # it's time to check the exact postion for the unsorted element
        # in sorted list
        # left elements of current unsorted element are sorted.
        # We should check between them
        j = i - 1

        while j >= 0 and key < array[j]:
            # create black to replace the small item
            # and move bigger one to right
            array[j + 1] = array[j]
            j = j - 1
        # in the blank position, we moved small one
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertion_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
