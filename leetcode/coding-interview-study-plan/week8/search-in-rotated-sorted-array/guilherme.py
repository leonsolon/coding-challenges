class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        nums, pos = self.corret_nums(nums)
        start = 0
        end = len(nums) - 1
        middle = start + (end - start) // 2
        num = nums[middle]
        while num != target:

            if target > num:
                start = middle + 1
            elif target < num:
                end = middle - 1
            else:
                return pos[middle]
            middle = start + (end - start) // 2

            if end <= start:
                if nums[middle] == target:
                    return pos[middle]
                else:
                    return -1

            num = nums[middle]

        return pos[middle]

    def corret_nums(self, nums):
        pos = list(range(0, len(nums)))
        for i, num in enumerate(nums):
            if i == 0:
                last = num
            else:
                if last > num:
                    break
                last = num
        else:
            i = 0

        nums = nums[i:] + nums[:i]
        pos = pos[i:] + pos[:i]

        return (nums, pos)