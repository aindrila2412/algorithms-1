"""
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
    Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters. 

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""
class Solution:
        # Helper method to recursively call by incrementing the index and adding to the current values
        def letterCombinations_helper(self, current, index, numbersMap, digits, result)
            # If the index is equal to the length of digits, means we have a complete string to append
            if index == len(digits):
                result.append(current)
                return 
            
            # Current letter items to check
            letters = numbersMap[digits[index]]
            
            # Loop over the current letter items and send character after character to the recursive function
            for i in range(len(letters)):
                self.letterCombinations_helper(current + letters[i], index + 1, numbersMap, digits, result)
                
        def letterCombinations(self, digits: str) -> List[str]:
            # Handling edge case 
            if digits == "":
                return []

            # Hash map for digits and respective keywords
            numbersMap = {
                "2": ["a", "b", "c"],
                "3": ["d", "e", "f"],
                "4": ["g", "h", "i"],
                "5": ["j", "k", "l"],
                "6": ["m", "n", "o"],
                "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"],
                "9": ["w", "x", "y", "z"]
            }

            # Initial variables and result values
            result = []
            index = 0
            current = ""

            # Call the helper method with the initial parameters
            self.letterCombinations_helper(current, index, numbersMap, digits, result)
            return result 
        