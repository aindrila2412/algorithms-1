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


x = [2, 4, 1, 3, 5]
naiveCountInversion(x, tempList, counter)
