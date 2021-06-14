# modify MergeSort to count the number of inversions in an array
def SimpleInvCount(array):
    """complexity O(n**2)"""
    count = 0
    n = len(array)
    for l in range(0, n - 1):
        for k in range(l + 1, n):
            if array[l] > array[k]:
                count += 1
    return count

# sort and count inversions
def SortCountInv(array):
    """complexity O(n.log(n))"""
    # base case
    n = len(array)
    if n <= 1:
        return array, 0
    else:
        midpoint = len(array) // 2
        leftArray = array[:midpoint]
        rightArray = array[midpoint:]
        left, leftInv = SortCountInv(leftArray)
        right, rightInv = SortCountInv(rightArray)
        mergedResult, splitInv = MergeCountSplitInv(left, right, array.copy())
        return mergedResult, leftInv + rightInv + splitInv

# merge and count split inversions subroutine
def MergeCountSplitInv(left, right, merged):
    """complexity O(n)"""
    # initialise indices
    i = 0
    j = 0
    splitInv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[i + j] = left[i]
            i += 1
        else:
            merged[i + j] = right[j]
            splitInv += (len(left) - i)
            j += 1

    # copy leftovers
    for i in range(i, len(left)):
        merged[i + j] = left[i]

    for j in range(j, len(right)):
        merged[i + j] = right[j]

    return merged, splitInv

# test
if __name__ == '__main__':
    with open("IntegerArray.txt", "r") as file:
        integers = [int(i.strip()) for i in file.readlines()]  # integers is now a list with 100 000 elements
        print(SortCountInv(integers)[1])
    file.close()
