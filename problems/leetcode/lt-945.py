# 945. Minimum Increment to Make Array Unique
"""
    Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.
    Return the least number of moves to make every value in A unique.

    Input: [3,2,1,2,1,7]
    Output: 6
    Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
    It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
"""
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        sum_A = sum(A)
        # create an array with the same length as A array
        check_arr = A
        # Sort the array A
        check_arr.sort()
        
        for i in range(1, len(check_arr)):
            if check_arr[i] <= check_arr[i-1]:
                check_arr[i] = max(check_arr[i], check_arr[i-1] + 1)
                
        return (sum(check_arr) - sum_A)
         
        #O (mn) => won't work
        # if len(A) < 1:
        #     return 0
        # A.sort()
        # check_dict = collections.Counter(A)
        # count = 0
        
        # for i in range(len(A)):
        #     if check_dict[A[i]] > 1:
        #         check_count = 0
        #         check_dict[A[i]] -= 1
        #         k = A[i]
        #         while k in check_dict:
        #             A[i] += 1
        #             check_count += 1
        #             k = A[i]
        #         count += check_count  
        #         check_dict[A[i]] = 1
        # return count 
        