# # 1498. Number of Subsequences That Satisfy the Given sum Condition
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # Approach 1: Checking all subsets (TLE)
        def recursive_subset_check_count(ip, op, final, target):
            if ip == []:
                if op != [] and min(op) + max(op) <= target:
                    final.append(op)
                return
            recursive_subset_check_count(ip[1:], op, final, target)
            recursive_subset_check_count(ip[1:], op + [ip[0]], final, target)
        
        final = []
        recursive_subset_check_count(nums, [], final, target)
        return len(final)
    
        
        # Approach 2: Using 2 pointers and binary search (Again TLE)
        nums.sort()
        count = 0
        right = len(nums) - 1
        for left in range(len(nums)):
            while left <= right and nums[left] + nums[right] > target:
                right -= 1
            if left <= right:
                count += (2 ** (right - left)) % (10 ** 9 + 7)
        return count % (10 ** 9 + 7)
    
        
        # Approach 3: Using Binary Search 
        # Works
        counts = 0
        mod = 10 ** 9 + 7
        length = len(nums)
        nums.sort()
        def binary_search(left, t, values):
            right = length - 1
            while left < right:
                mid = left + (right - left) // 2 + 1
                if values[mid] <= t:
                    left = mid
                else:
                    right = mid - 1
            return right

        for i in range(length):
            if 2 * nums[i]  > target:
                break
            right_value = binary_search(i, target - nums[i], nums)
            # count += binary_search(i, len(nums) - 1, nums) - i + 1
            if nums[i] + nums[right_value] <= target:
                counts += pow(2 , right_value - i, mod)
        return counts % mod