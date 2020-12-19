# 11. Container With Most Water
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, 
together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialise the start, end, and area of the container
        start = 0
        end = len(height) - 1 
        container_area = 0 
        # Use two pointer and loop over 
        while start != end:
            # If the left side is less, increment it and update area
            if height[start] < height[end]:
                area = height[start] * (end - start)
                container_area = max(container_area, area)
                start += 1
            # Else, decrement the right side and update the area
            else:
                area = height[end] * (end - start)
                container_area = max(container_area, area)
                end -= 1 
                
        return container_area
                
            
        