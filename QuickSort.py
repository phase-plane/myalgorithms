# sort an array and count no. of comparisons
testArray = [5, 4, 1, 8, 7, 2, 6, 3]

def QuickSort(array, track=False, count=0, idx=0):
    """complexity: best O(n.log(n)) /  average O(n.log(n)) / worst O(n**2)"""
    n = len(array)
    count += max(n - 1, 0)
    # base case
    if n <= 1:
        if track:
            return array, count
        else:
            return array
    else:
        index = pivotIndex(idx)
        if index != 0:
            array[0], array[index] = array[index], array[0]
        partitioned, i = partition(array, index, n - 1)
        partitioned[:i - 1], count = QuickSort(partitioned[:i - 1], True, count)
        partitioned[i:], count = QuickSort(partitioned[i:], True, count)
    if track:
        return array, count
    else:
        return array

def pivotIndex(idx):
    if idx == "median":
        return 0
    elif idx == "last":
        return -1
    else:
        return 0

# partition subroutine given array A[l,...,r]
def partition(array, l, r):
    p = array[l]  # set pivot as first element (for now)
    i = l + 1
    for j in range(l + 1, r):
        if array[j] < p:
            array[i], array[j] = array[j], array[i]
            i += 1
    # swap pivot
    array[l], array[i - 1] = array[i - 1], array[l]
    return array, i


# test
if __name__ == '__main__':
    print(QuickSort(testArray, track=True)[0])
#   with open("QuickSort.txt", "r") as file:
#      integers = [int(i.strip()) for i in file.readlines()]  # integers is now a list with 10 000 elements
#      QuickSort(integers)
#   file.close()
