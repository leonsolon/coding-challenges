class Solution(object):
    def twoSum(self, nums, target):
    
        N = len(nums)
  
        for i in range(N-1):
            for j in range(i+1, N):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]
                    
