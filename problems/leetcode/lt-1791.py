# 1791. Find Center of Star Graph
"""
    There is an undirected star graph consisting of n nodes labeled from 1 to n. 
    A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

    You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. 
    Return the center of the given star graph.
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hash_map = dict()
        count = 0
        for edge in edges:
            count += 1
            if edge[0] not in hash_map:
                hash_map[edge[0]] = 1
            else: 
                hash_map[edge[0]] += 1
                
            if edge[1] not in hash_map:
                hash_map[edge[1]] = 1
            else:
                hash_map[edge[1]] += 1
                
        for value in hash_map:
            if hash_map[value] == count:
                return value
        # One Liner
        # return list(set.intersection(*map(set,edges)))[0]
        
        