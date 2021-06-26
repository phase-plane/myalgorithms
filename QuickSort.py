# sort an array and count no. of comparisons
testArray = [3, 8, 2, 5, 1, 4, 7, 6]

def QuickSort(array, idx=0):
    """complexity: best O(n.log(n)) /  average O(n.log(n)) / worst O(n**2)"""
    l = array[idx]
    r = array[len(array)-1]
    # base case
    if l >= r:
        return array, 0
    else:
        i = ChoosePivot(array, l, r, idx)
        if i != 0:
            array[l], array[i] = array[i], array[l]
        j = partition(array, l, r)
        array[:j - 1], a = QuickSort(array[:j - 1], idx)
        array[j + 1:], b = QuickSort(array[j + 1:], idx)
        return array, a + b

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
    return i-1

def ChoosePivot(array, l, r, idx):
    if idx == "median":
        return 0
    elif idx == "last":
        return -1
    else:
        return 0

# test
if __name__ == '__main__':
    print(QuickSort(testArray)[0])
#   with open("QuickSort.txt", "r") as file:
#      integers = [int(i.strip()) for i in file.readlines()]  # integers is now a list with 10 000 elements
#      QuickSort(integers)
#   file.close()
