class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                if n1+n2 == target:
                    return [i, j]