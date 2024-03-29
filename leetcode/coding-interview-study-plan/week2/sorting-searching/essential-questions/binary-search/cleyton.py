#7'

#Link:https://leetcode.com/problems/binary-search/


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        beg = 0
        end = len(nums) - 1
        
        while (beg <= end):
            mid = beg + (end - beg)//2
            if nums[mid] == target:
                return mid
            if target < nums[mid] :
                end = mid - 1
            else:
                beg = mid + 1
        
        return -1
