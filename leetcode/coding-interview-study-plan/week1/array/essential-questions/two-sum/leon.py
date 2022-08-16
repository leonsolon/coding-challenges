from bisect import bisect_left


class Solution:
    def twoSum(self, nums, target):
        dict_nums = {num: index for index, num in enumerate(nums)}

        ordered_nums = sorted(nums)

        for num in ordered_nums:
            remainder = target - num
            remainder_position = bisect_left(ordered_nums, remainder)

            if remainder_position == len(ordered_nums):
                continue

            if num == remainder:
                first_index = nums.index(num)
                nums[first_index] += 1
                second_index = nums.index(num)
                return [first_index, second_index]

            if ordered_nums[remainder_position] == remainder:
                return [dict_nums[num], dict_nums[remainder]]


sol = Solution()

assert sol.twoSum(nums=[0, 4, 3, 0], target=0) == [0, 3]
assert sol.twoSum(nums=[3, 2, 3], target=6) == [0, 2]
assert sol.twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1]
assert sol.twoSum(nums=[3, 2, 4], target=6) == [1, 2]
assert sol.twoSum(nums=[3, 3], target=6) == [0, 1]
