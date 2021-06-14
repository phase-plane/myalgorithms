# sort and merge an array
testArray = [5, 4, 1, 8, 7, 2, 6, 3]
def MergeSort(array):
    """complexity O(n.log(n))"""
    # base case
    if len(array) <= 1:
        return array
    else:
        midpoint = len(array) // 2
        left_array = array[:midpoint]
        right_array = array[midpoint:]
        left, right = MergeSort(left_array), MergeSort(right_array)
        return merge(left, right, array.copy())

# merge subroutine
def merge(left, right, merged):
    """complexity O(n)"""
    # initialise indices
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[i+j] = left[i]
            i += 1
        else:
            merged[i+j] = right[j]
            j += 1

    # copy leftovers
    for i in range(i, len(left)):
        merged[i + j] = left[i]

    for j in range(j, len(right)):
        merged[i + j] = right[j]
    return merged

# test
if __name__ == '__main__':
    print(MergeSort(testArray))
