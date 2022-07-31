from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, len(nums)+1):
            ans += combinations(nums, i)
        return ans
