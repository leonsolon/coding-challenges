#8'

#Link:https://leetcode.com/problems/two-sum/


# Runtime: 75 ms, faster than 82.69% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 24.20% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {nums[i]:i for i in range(len(nums))} #get the indices of each number in nums
        
        for i, a in enumerate(nums):
            b = target - a
            if b in m and m[b] != i: #we can't use the same element twice
                return [m[b], i]
