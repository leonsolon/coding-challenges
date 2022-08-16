class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        dict_nums = {n: i for i, n in enumerate(nums)}
        for i, num in enumerate(nums):
            if ((comp := target - num) in dict_nums) and ((dict_nums[comp]) != i):
                return [i, dict_nums[comp]]

# Runtime: 77 ms, faster than 83.07% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 24.20% of Python3 online submissions for Two Sum.