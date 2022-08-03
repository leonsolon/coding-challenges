# Passou em 309 dos 311 testes


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        diff_dict = {}
        for i, n1 in enumerate(nums):
            for j in range(i + 1, len(nums)):
                n2 = nums[j]
                diff = 0 - n2 - n1
                if diff in diff_dict:
                    diff_dict[diff].append((i, j))
                else:
                    diff_dict[diff] = [(i, j)]

        triples = set()
        for i, n in enumerate(nums):
            if n in diff_dict:
                for (j, k) in diff_dict[n]:
                    if i != j and i != k:
                        if i < j:
                            triples.add((n, nums[j], nums[k]))
                        elif i > k:
                            triples.add((nums[j], nums[k], n))
                        else:
                            triples.add((nums[j], n, nums[k]))
        return triples