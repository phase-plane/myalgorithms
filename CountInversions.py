# modify MergeSort to count the number of inversions in an array
# sort and merge an array
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
        # left, right = MergeSort(left_array), MergeSort(right_array)
        # return merge(left, right, array.copy())
        sortedLeft, leftInv = SortCountInv(leftArray)
        sortedRight, rightInv = SortCountInv(rightArray)
        mergedResult, splitInv = MergeCountSplitInv(sortedLeft, sortedRight, array.copy())
        return mergedResult, leftInv + rightInv + splitInv


# merge and count split inversions subroutine
def MergeCountSplitInv(C, D, merged):
    """complexity O(n)"""
    # initialise indices
    i = 0
    j = 0
    n = len(C) + len(D)
    splitInv = 0
    while i < len(C) and j < len(D):
        if C[i] <= D[j]:
            merged[i + j] = C[i]
            i += 1
        else:
            merged[i + j] = D[j]
            j += 1
            splitInv = splitInv + (n / 2 - i + 1)

    # copy leftovers
    for i in range(i, len(C)):
        merged[i + j] = C[i]

    for j in range(j, len(D)):
        merged[i + j] = D[j]
    return merged, splitInv


# test
if __name__ == '__main__':
    with open("testArray.txt", "r") as file:
        lines = file.readlines()  # lines is now a list with 100 000 elements
        print(SortCountInv(lines))
    file.close()
