# Week 1 - Array
# Two Sum
# Runtime: 2395 ms, faster than 39.20% of Python online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 45.09% of Python online submissions for Two Sum.

class Solution(object):
    def twoSum(self, nums, target):
    
        N = len(nums)
  
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                    
