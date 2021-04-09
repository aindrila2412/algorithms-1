"""
    In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
    The order of the alphabet is some permutation of lowercase letters.

    Given a sequence of words written in the alien language, and the order of the alphabet, 
    return true if and only if the given words are sorted lexicographicaly in this alien language.

    Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
    Output: false
    Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
"""
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_map = dict()
        index = 1
        
        # Create a hash map for the order values in increasing order 
        for i in order:
            hash_map[i] = index 
            index += 1
        # Loop over the words, and take ith and (i+1)th word to check   
        for i in range(len(words) - 1):
            l1 = len(words[i])
            l2 = len(words[i+1])
            # Loop over the characters of (i)th and (i+1)th word
            for j in range(l1):
                # If the index of the first word is more than the second one, return false
                if j >= l2:
                    return False
                # If characters are not equal
                if words[i][j] != words[i + 1][j]:
                    # If the character in the first word is greater than the character in the second one, return false
                    if hash_map[words[i][j]] > hash_map[words[i + 1][j]]:
                        return False
                    break
        return True