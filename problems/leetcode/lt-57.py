# 57. Insert Interval
"""
    Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

    You may assume that the intervals were initially sorted according to their start times.

    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]
    Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        target = [newInterval] 
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        updated_list = list()
        for interval in intervals:
            if len(updated_list) == 0 or updated_list[-1][1] < interval[0]:
                updated_list.append(interval)
            else:
                updated_list[-1][1] = max(updated_list[-1][1], interval[1])
        return updated_list