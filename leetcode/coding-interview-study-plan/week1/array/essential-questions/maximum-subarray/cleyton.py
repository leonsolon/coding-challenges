#3'

#Link: https://leetcode.com/problems/maximum-subarray/

# Runtime: 574 ms, faster than 65.74% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 27.9 MB, less than 78.72% of Python3 online submissions for Maximum Subarray.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        localMax = 0
        globalMax = float('-inf')
        
        for n in nums:
            localMax = max(localMax + n, n)
            globalMax = max(globalMax, localMax)
            
        return globalMax
