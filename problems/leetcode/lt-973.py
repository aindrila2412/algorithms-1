# 973. K Closest Points to Origin
"""
    Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
    return the k closest points to the origin (0, 0).

    The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

    Input: points = [[1,3],[-2,2]], k = 1
    Output: [[-2,2]]
    Explanation:
    The distance between (1, 3) and the origin is sqrt(10).
    The distance between (-2, 2) and the origin is sqrt(8).
    Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
    We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
"""
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Method 1: Using Heaps and hashmap
        # Time Complexity: O(n log n)
        # Space complexity: O(n)
        def calculate_distance(x, y):
            a = (0 - x) ** 2
            b = (0 - y) ** 2
            return sqrt(a + b)
    
        hashMap = dict()
        container = list()
        final = list()
        for item in points:
            dist = calculate_distance(item[0], item[1])
            container.append(dist)
            if dist in hashMap:
                hashMap[dist].append(item)
            else:
                hashMap[dist] = [item]
        # container = set(container)
        heapq.heapify(container)
        vals = heapq.nsmallest(k, container)
        vals = set(vals)
        
        for i in vals:
            temp = hashMap[i]
            final += temp
        return final 

        # One liner solution 
        # Time complexity: O(n log n)
        # Space complexity: O(n)
        return heapq.nsmallest(k, points, key=lambda val: sqrt(val[0]**2 + val[1]**2))
    
        # Using sort 
        # Time complexity: O(n log n)
        # Space complexity: O(1)
        points.sort(key = lambda point : sqrt(point[0]**2 + point[1] ** 2))
        return points[:k]