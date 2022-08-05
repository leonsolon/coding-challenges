class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        current_sum = -float('inf')
        for i, n in enumerate(nums):
            current_sum = max(n, current_sum + n)
            max_sum = max(max_sum, current_sum)

        return max_sum