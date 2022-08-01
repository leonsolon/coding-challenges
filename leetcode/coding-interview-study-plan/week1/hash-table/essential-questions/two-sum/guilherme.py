class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i, n in enumerate(nums):
            if n in diff_dict:
                return [diff_dict[n] , i]
            else:
                diff = target - n
                diff_dict[diff] = i
        print(diff_dict)