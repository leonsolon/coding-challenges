class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
                return middle
            middle = start + (end - start) // 2

            if end <= start:
                if nums[middle] == target:
                    return middle
                else:
                    return -1

            num = nums[middle]

        return middle