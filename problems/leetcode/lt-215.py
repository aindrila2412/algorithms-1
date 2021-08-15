class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Method 1: Using a quick sort
        def quick_sort(arr):
            if len(arr) <= 1:
                return arr 
            else:
                pivot = arr.pop()
                left = []
                right = []

                for val in arr:
                    if val > pivot:
                        left.append(val)
                    else:
                        right.append(val)
                return quick_sort(left) + [pivot] + quick_sort(right)
        arr = nums
        n = quick_sort(arr)
        return n[k-1]
        
        # Method 2: Using in built sort method
        nums.sort(reverse=True)
        return nums[k-1]
        
        # Method 3: Using a max heap
        heapq.heapify(nums)
        return (heapq.nlargest(k, nums)[-1])