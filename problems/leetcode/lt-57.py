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
        # Approach 1, by simply appending the new interval, sorting and then performing the actions 
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

        # Approach 2, doesn't use sorting 
        # Edge case for empty intervals 
        if len(intervals) == 0:
            return [newInterval]
        # Edge case if newInterval has to be prepend to the interval 
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals 
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        
        
        # Edge case for a single list in intervals 
        if len(intervals) == 1:
            if intervals[0][0] < newInterval[0]:
                intervals.append(newInterval)
            else:
                intervals = [newInterval] + intervals 
            newInterval = None 
        updatedInterval = [intervals[0]]
        # Loop over and check for cases 
        for interval in intervals[1:]:
            if newInterval:
                if updatedInterval[-1][1] >= newInterval[0]:
                    updatedInterval[-1] = [
                        min(updatedInterval[-1][0], newInterval[0]), 
                        max(updatedInterval[-1][1], newInterval[1])
                    ]
                    newInterval = None 
                
                elif interval[0] > newInterval[0]:
                    updatedInterval.append(newInterval)
                    newInterval = None 
                elif interval[1] >= newInterval[0]:
                    value = [
                        min(interval[0], newInterval[0]),
                        max(interval[1], newInterval[1])
                    ]
                    updatedInterval.append(value)
                    newInterval = None 
        
            # Now newInterval is empty, check if there is a merge to be made with the next element in intervals[i]
            if updatedInterval[-1][1] < interval[0]:
                updatedInterval.append(interval)
            else:
                updatedInterval[-1][1] = max(updatedInterval[-1][1], interval[1])
                
        return updatedInterval 
        

