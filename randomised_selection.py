# Implementation of Randomised Selection

"""
    Naive Approach

    ---------
    Parameters
    ---------
    An arry with n distinct numbers

    ---------
    Returns
    ---------
    i(th) order statistic, i.e: i(th) smallest element of the input array

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
import random


def randomised_selection(unsorted_array, length_of_array, i_order_statistic):
    if length_of_array == 1:
        return unsorted_array
    else:
        # pivot = random.choice(unsorted_array)
        pivot_range = random.randrange(length_of_array)
        pivot = unsorted_array[pivot_range]
        pivot_left = []
        pivot_right = []

        for value in unsorted_array:
            if pivot_range == i_order_statistic:
                return pivot
            if pivot_range > i_order_statistic:
                return randomised_selection(unsorted_array[:pivot_range], pivot_range - 1, i_order_statistic)
            if pivot_range < i_order_statistic:
                return randomised_selection(unsorted_array[pivot_range + 1:], length_of_array - pivot_range, i_order_statistic - pivot_range)



if __name__ == "__main__":
    # user_input = input("Enter the list of numbers: \n").strip()
    # unsorted_array = [int(item) for item in user_input.split(",")]
    print(randomised_selection([1, 23, 3, 43, 5], 5, 3))
