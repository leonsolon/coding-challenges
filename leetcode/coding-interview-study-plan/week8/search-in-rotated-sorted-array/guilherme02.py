class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bin_search(start, end, target):
            print(start, end)
            if end - start <= 1:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1
            middle = start + (end - start) // 2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                start = middle + 1
                return bin_search(start, end, target)
            elif target < nums[middle]:
                end = middle - 1
                return bin_search(start, end, target)

        len_nums = len(nums)
        idx = list(range(0, len_nums))
        for i, n in enumerate(nums):
            if i + 1 < len_nums:
                if n > nums[i + 1]:
                    break

        nums = nums[i + 1:] + nums[:i + 1]
        idx = idx[i + 1:] + idx[:i + 1]

        start = 0
        end = len_nums - 1
        i = bin_search(start, end, target)
        if i == -1:
            return -1
        else:
            return idx[i]





