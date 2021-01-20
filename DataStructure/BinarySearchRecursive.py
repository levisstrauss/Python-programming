# In binary search, the table has to be sorted
# This is a method called recursion
def binarySearch(A, key, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if key == A[mid]:
            return True
        elif key < A[mid]:
            return binarySearch(A, key, low, mid - 1)
        else:
            return binarySearch(A, key, mid + 1, high)


A = [15, 21, 47, 84, 96]
found = binarySearch(A, 47, 0, 5)
print(found)
