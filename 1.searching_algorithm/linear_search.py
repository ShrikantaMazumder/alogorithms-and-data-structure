# It will loop though the whole array to get desired number
# May be it can find in first, middle or last
# But the worst case is that it can check the last item of the array

# So the loop/operations are dependent on the length of array
# That's why time complexity is O(n)

# Space complexity is O(1). Because it's constant or not dependent on nth value.


arr = [385, 25, 39, 57, 285, 93, 24]

def linear_search(inputArr, searchItem):
    for i in range(0,len(inputArr)):
        if(inputArr[i] == searchItem):
            return i
    return -1


result = linear_search(arr, 93)

if result == -1:
    print("Item not found")
else:
    print("Item's index is: " + str(result))