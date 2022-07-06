def merge_sort(arr):
    if len(arr) > 1:
        r = len(arr)//2
        L = arr[:r]
        R = arr[r:]

        merge_sort(L)
        merge_sort(R)

        # merge here
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


numbers = [31, 34, 21, 53, 5, 6, 1, 45, 76]
merge_sort(numbers)
print(numbers)
