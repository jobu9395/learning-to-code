
# O(log(n)) time, O(log(n)) space
#recursive version
def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    middle = (left + right) //2
    potentialMatch = array[middle]
    if target == potentialMatch:
        return middle
    elif target < potentialMatch:
        return binarySearchHelper(array, target, left, middle - 1)
    else:
        return binarySearchHelper(array, target, middle + 1, right)

print(binarySearch([0, 1, 22, 33, 45, 45, 61, 71, 72, 73], 73))

#ITERATIVE VERSION
#O(log(n)) time, O(1) space (better than recursive)

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)


def binarySearchHelper(array, target, left, right):
    while left <= right:
        middle = (left + right) //2
        potentialMatch = array[middle]
        if target == potentialMatch:
            return middle
        elif target < potentialMatch:
            right = middle - 1
        else:
            left = middle + 1
    return -1

print(binarySearch([0, 1, 22, 33, 45, 45, 61, 71, 72, 73], 73))




