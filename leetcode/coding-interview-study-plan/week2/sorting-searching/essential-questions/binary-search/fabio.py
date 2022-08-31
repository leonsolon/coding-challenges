class Solution:
    def search(self, nums: list, target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target: return middle
            if nums[middle] < target: left = middle + 1
            if nums[middle] > target: right = middle - 1

        return -1
    
# Runtime: 368 ms, faster than 51.67% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 97.43% of Python3 online submissions for Binary Search.