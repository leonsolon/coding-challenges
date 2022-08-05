from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count_nums = Counter(nums)
        triples = set()
        for i, n1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                n2 = nums[j]
                need = 1
                if n1 == n2:
                    need = 2
                sum2 = n1 + n2
                diff = 0 - n2 - n1
                if diff in count_nums:
                    need = 1
                    if diff == n1:
                        need += 1
                    if diff == n2:
                        need += 1
                    if count_nums[diff] >= need:
                        if diff < n1:
                            triples.add((diff, n1, n2))
                        elif diff > n2:
                            triples.add((n1, n2, diff))
                        else:
                            triples.add((n1, diff, n2))

        return triples