class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binsearch(start, end, target):
            if end - start < 1:
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    return -1
            middle = start + (end - start) // 2
            num_middle = nums[middle]
            if num_middle == target:
                return middle
            elif num_middle > target:
                end = middle - 1
                return binsearch(start, end, target)
            elif num_middle < target:
                start = middle + 1
                return binsearch(start, end, target)

        return binsearch(0, len(nums) - 1, target)