# Count inversions in an array
# Tells us about how far is the array from being sorted

# NAIVE APPROACH in the O(n^2)

# Initial counter element and final temporary list
tempList = list()
counter = 0

# Function that takes initialArray, counter element and temporary final list


def naiveCountInversion(toDoArray, tempList, counter):
    for i in range(0, len(toDoArray) - 1):
        for j in range(i + 1, len(toDoArray)):
            # if i < j and A[i] > A[j], increment the counter and add a new list to the final list
            if toDoArray[i] > toDoArray[j]:
                counter += 1
                newList = (toDoArray[i], toDoArray[j])
                tempList.append(newList)
    print(tempList)


x = [1, 20, 6, 4, 5]
# print(len(x))
# naiveCountInversion(x, tempList, counter)


"""
    Divide and Conquer appraoch

    ---------
    Parameters
    ---------
    unsorted array

    ---------
    Returns
    ---------
    Sorted array with number of inversions

    ---------
    Time Complexity
    ---------
    O(n*logn)

    ---------
    Test Cases
    ---------
    [1, 20, 6, 4, 5]
    => ([1, 4, 5, 6, 20], 5)

"""


def mergeSortInversions(toDoArray):
    # If length of the array is 1, Return
    if len(toDoArray) == 1:
        return toDoArray, 0
    else:
        # Find the mid element
        midElementIndex = len(toDoArray) // 2
        # Find the left elements and right elements array
        leftElementArray = toDoArray[: midElementIndex]
        rightElementArray = toDoArray[midElementIndex:]

        # Recursively call the mergeSortInversions() method
        leftElementArray, inv_count_left = mergeSortInversions(
            leftElementArray)
        rightElementArray, inv_count_right = mergeSortInversions(
            rightElementArray)
        newArray = []
        i, j = 0, 0

        inversion_count = 0 + inv_count_left + inv_count_right

        while i < len(leftElementArray) and j < len(rightElementArray):
            if leftElementArray[i] <= rightElementArray[j]:
                newArray.append(leftElementArray[i])
                i += 1
            else:
                newArray.append(rightElementArray[j])
                j += 1
                inversion_count += len(leftElementArray) - i
        newArray += leftElementArray[i:]
        newArray += rightElementArray[j:]
    return newArray, inversion_count


print(mergeSortInversions(x))
