# Implementation of Quick Sort Algorithm

"""
    Naive Approach

    ---------
    Parameters
    ---------
    An Unsorted array

    ---------
    Returns
    ---------
    A sorted array

    ---------
    Time Complexity
    ---------
    O(n.logn)

    ---------
    Test Cases
    ---------
    [1, 20, 6, 4, 5]
    => [1, 4, 5, 6, 20]

"""

def quick_sort(unsorted_array):
    if len(unsorted_array) <= 1:
        return unsorted_array
    else:
        # In each recursive call, make pivot the last element
        pivot = unsorted_array.pop()
        pivot_left = []
        pivot_right = []

        # Loop over the values of unsorted array
        for value in unsorted_array:
            if value < pivot:
                pivot_left.append(value)
            else:
                pivot_right.append(value)

        return quick_sort(pivot_left) + [pivot] + quick_sort(pivot_right)


if __name__ == "__main__":
    user_input = input("Enter the list of numbers: \n").strip()
    unsorted_array = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted_array))










