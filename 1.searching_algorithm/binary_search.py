# Binary search
# Array should be sorted

# It divide the array into two and find the middle index
# Check searched item is bigger or smaller than the middle index item
# if searched item is bigger than it again do the same thing
# it divide the array from mid index to last index
# It will continue till the item found or the array is finished

# Time Complexity
# O(log2 to the power n)
# Best case of this algo is O(1)
# Average case: O(log2 to the power n)
# Worst case: O(log2 to the power n)

# Space complexity
# O(1) => because variables are constant.


def binary_search(sortedList, search):
    left = 0
    right = len(sortedList) - 1

    while left <= right:
        mid = (right + left) // 2
        if sortedList[mid] == search:
            return mid

        if sortedList[mid] < search:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = [2, 4, 6, 8, 9, 12, 15, 20]

result = binary_search(arr, 12)

if result == -1:
    print("Item not found")
else:
    print("Item's index is: " + str(result))
