# 46. Permutations
"""
    Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
    
    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def generate_permutations(final, values, index=0):
            if index == len(values):
                final.append(values.copy())
            else:
                # Looping over the array from the index element to the end 
                for i in range(index, len(values)):
                    # Swapping the ith element to the index element
                    values[index], values[i] = values[i], values[index]
                    # Recursively updating the elements
                    generate_permutations(final, values, index + 1)
                    # Swapping the elements back to get back to the previous iteration
                    values[index], values[i] = values[i], values[index]

        final = []
        generate_permutations(final, nums)
        return final 