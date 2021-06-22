# 56. Merge Intervals
"""
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
    and return an array of the non-overlapping intervals that cover all the intervals in the input.

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        new_list = list()
        
        for value in intervals:
            if len(new_list) == 0 or new_list[-1][1] < value[0]:
                new_list.append(value)
            else:
                new_list[-1][1] = max(new_list[-1][1], value[1])
            
        return new_list
