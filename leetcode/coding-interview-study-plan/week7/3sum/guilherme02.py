from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        comb_nums = combinations(nums, 3)
        comb_sum_0 = set()
        for comb in comb_nums:
            comb = tuple(sorted(comb))
            if sum(comb) == 0:
                # comb = tuple(sorted(comb))
                comb_sum_0.add(comb)

        return comb_sum_0