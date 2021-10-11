# 49. Group Anagrams
"""
    Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
    typically using all the original letters exactly once.

    Input: strs = ["eat","tea","tan","ate","nat","bat"]
    Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Init a hashmap to calculate the frequency
        hashMap = dict()
        # final = []
        
        # Iterate and append to the haspMap in groups (arrays)
        for val in strs:
            temp = "".join(sorted(val))
            if temp not in hashMap:
                hashMap[temp] = [val]
            else:
                hashMap[temp].append(val)
            
        # for val in hashMap:
        #     final.append(hashMap[val])
        # return final 
        return (list(hashMap.values()))