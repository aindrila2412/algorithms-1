# 658. Find K Closest Elements
"""
    Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

    An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Find the nearest left and right elements to x using binary search or using bisect method 
        low = 0 
        left, right = None, None 
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if x == arr[mid]:
                k -= 1
                left = mid - 1
                right = mid + 1
                break
            elif x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
            
        # If key is not found, then low will be higher than high
        if arr[mid] != x:
            left = high 
            right = low 
            
        # Iterating over using 2 pointers and returning the remaining list 
        while k > 0:
            # When left is -1, we just have to increment the right side 
            if left == -1:
                right += 1
            # If the right is out of array length, we have to decrement the left value
            elif right == len(arr):
                left -= 1
            else:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    left -= 1
                else: 
                    right += 1
            k -= 1
        return arr[left + 1:right] 