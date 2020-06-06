# Implementation of Merge Sort Algorithm 1
def merge_sort(unsortedList):
    # If the length of the list is 1, print it and exit
    if len(unsortedList) == 1:
        exit
    # If the length is more than that, pass
    if len(unsortedList) > 1:
        # Find the mid term of the unsorted array
        midTerm = len(unsortedList) // 2
        # Split the left side
        leftSideArray = unsortedList[:midTerm]
        # Split the right side
        rightSideArray = unsortedList[midTerm:]
        # Recursive call to merge_sort function
        merge_sort(leftSideArray)
        merge_sort(rightSideArray)
        # Initialise 3 variables
        i, j, k = 0, 0, 0
        while i < len(leftSideArray) and j < len(rightSideArray):
            if leftSideArray[i] < rightSideArray[j]:
                unsortedList[k] = leftSideArray[i]
                i += 1
            else:
                unsortedList[k] = rightSideArray[j]
                j += 1
            k += 1

        while i < len(leftSideArray):
            unsortedList[k] = leftSideArray[i]
            i += 1
            k += 1
        while j < len(rightSideArray):
            unsortedList[k] = rightSideArray[j]
            j += 1
            k += 1


# Implementation of Merge Sort Algorithm 2

def merge_sorts(unsortedList):
    def merge_list(leftSideArray, rightSideArray):
        sorted_array = []
        while leftSideArray and rightSideArray:
            sorted_array.append(
                (leftSideArray if leftSideArray[0] <= rightSideArray[0] else rightSideArray).pop(0))
        return sorted_array + leftSideArray + rightSideArray
    if len(unsortedList) <= 1:
        return unsortedList
    midTerm = len(unsortedList) // 2
    return merge_list(merge_sorts(unsortedList[:midTerm]), merge_sorts(unsortedList[midTerm:]))


if __name__ == "__main__":
    user_input = input("Enter the list of numbers: \n").strip()
    unsortedArray = [int(item) for item in user_input.split(",")]
    print(merge_sorts(unsortedArray))
    # print(unsortedArray)m
