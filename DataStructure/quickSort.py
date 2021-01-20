# Same has merge sort
# Perform better than merge sort in O(n log n)
# Operate in place on the data
# Worst case O(n^2)
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def quickSort(dataset, first, last):
    if first < last:
        # Calculate the split point
        pivotIdx = partition(dataset, first, last)
        # now sort the two partitions
        # Using recursion
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx + 1, last)


def partition(datavalues, first, last):
    # Choose the first item as the pivot
    pivotvalue = datavalues[first]
    # establish  the upper and lower indexes
    lower = first + 1
    upper = last
    # starting searching for the crossing point
    done = False
    while not done:
        # TODO: advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1

        # Advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1

        # If the two index cross, we have found the split point
        if upper < lower:
            done = True
        else:
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # When the split point is found  exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp

    # return the split point  index
    return upper


# test the merge sort with data
print(items)
quickSort(items, 0, len(items) - 1)
print(items)
