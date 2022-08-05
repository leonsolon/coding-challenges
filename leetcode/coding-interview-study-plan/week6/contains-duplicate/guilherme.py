class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        len_set_nums = len(set(nums))
        if len_nums > len_set_nums:
            return True
        else:
            return False