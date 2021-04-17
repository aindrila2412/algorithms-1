# 997. Find the Town Judge
"""
    In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

    Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    Output: 3
"""
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # Handling edge cases 
        if len(trust) == 0 and N == 1:
            return 1 
        
        if len(trust) == 0 and N >= 1:
            return -1 
        flag = 0
        
        # Add all the trusts with the N index 
        hash_map = dict()
        for i in trust:
            if i[1] not in hash_map:
                hash_map[i[1]] = [i[0]]
            else:
                hash_map[i[1]].append(i[0])
        
        # Check if a key in the hash map has a value array of length N - 1 
        for i in hash_map:
            if len(hash_map[i]) == N - 1:
                # If ith key is the judge, we need to confirm that the judge doesn't trust anyone 
                for j in hash_map:
                    if len(hash_map) == 1:
                        return i
                    else:
                        if i in hash_map[j]:
                            return -1
                return i
        return -1 
