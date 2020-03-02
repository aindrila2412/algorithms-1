# Implementation of Merge Sort Algorithm
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


if __name__ == "__main__":
    user_input = input("Enter the list of numbers: \n").strip()
    unsortedArray = [int(item) for item in user_input.split(",")]
    merge_sort(unsortedArray)
    print(unsortedArray)
