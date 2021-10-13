# 784. Letter Case Permutation
"""
    Given a string s, we can transform every letter individually to be lowercase or uppercase to create another string.
    Return a list of all possible strings we could create. You can return the output in any order.

    Input: s = "a1b2"
    Output: ["a1b2","a1B2","A1b2","A1B2"]
"""
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def permutation_case_change_helper(input_val, output_val):
            # Base condition to return when input string is empty
            if len(input_val) == 0:
                final.append(output_val)
                return
            # Recursively call the helper function with both uppercase and lowercase
            temp = input_val[0]
            # If the current index value is a number, only lowercase
            if temp.isnumeric() == True:
                permutation_case_change_helper(input_val[1:], output_val + temp.upper())
            else:
                # Recursively call the helper function with both uppercase and lowercase
                permutation_case_change_helper(input_val[1:], output_val + temp.lower())
                permutation_case_change_helper(input_val[1:], output_val + temp.upper())

        def permutation_case_change(input_val):
            # If the current index value is a number, only lowercase
            if input_val[0].isnumeric() == True:
                permutation_case_change_helper(input_val[1:], input_val[0].upper())
            else:
                # Recursively call the helper function with both uppercase and lowercase
                permutation_case_change_helper(input_val[1:], input_val[0].lower())
                permutation_case_change_helper(input_val[1:], input_val[0].upper())

        final = list()
        permutation_case_change(s)
        return final