# modify MergeSort to count the number of inversions in an array
# sort and merge an array
testArray = [1, 3, 5, 2, 4, 6]
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
        C, leftInv = SortCountInv(leftArray)
        D, rightInv = SortCountInv(rightArray)
        B, splitInv = MergeCountSplitInv(C, D)
        return B, leftInv + rightInv + splitInv

      # left, right = MergeSort(left_array), MergeSort(right_array)
      # return merge(left, right, array.copy())

# merge subroutine
def MergeCountSplitInv(C, D):
    """complexity O(n)"""
    # initialise indices
    i = 0
    j = 0
    splitInv = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[i+j] = left[i]
            i += 1
        else:
            merged[i+j] = right[j]
            j += 1
            splitInv = splitInv + (n/2 - i + 1)

    # copy leftovers
    for i in range(i, len(left)):
        merged[i + j] = left[i]

    for j in range(j, len(right)):
        merged[i + j] = right[j]
    return B, splitInv

# test
if __name__ == '__main__':
    SortCountInv(testArray)
