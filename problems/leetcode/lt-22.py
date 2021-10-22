# 22. Generate Parentheses
"""
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Input: n = 3
    Output: ["((()))","(()())","(())()","()(())","()()()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParenthesis_helper(output, left, right):
            if left == 0 and right == 0:
                final.append(output)
                return
            # If left value is not equal to zero, create a left branch with a "(" decision
            if left != 0:
                generateParenthesis_helper(output + '(', left - 1, right)
            # If left value is not equal to right value, create a right branch with a ")" decision
            if left != right:
                generateParenthesis_helper(output + ')', left, right - 1)

        final = []
        generateParenthesis_helper("", n, n)
        return final
        