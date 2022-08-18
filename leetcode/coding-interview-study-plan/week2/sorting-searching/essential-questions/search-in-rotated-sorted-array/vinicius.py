'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 
Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104

Success
Details 
Runtime: 70 ms, faster than 40.89% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 14.2 MB, less than 56.61% of Python3 online submissions for Search in Rotated Sorted Array.
Next challenges:
Search in Rotated Sorted Array II
Find Minimum in Rotated Sorted Array
Pour Water Between Buckets to Make Water Levels Equal
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        shift = 0
        for i, el in enumerate(nums):
            if i == len(nums) - 1:
                break
            if nums[i] > nums [i+1]:
                shift = i+1
                break
        ajust = nums[shift:] + nums[:shift]
        minidx = 0
        maxidx = len(nums) - 1
        while minidx <= maxidx:
            guess = (minidx + maxidx)//2
            if ajust[guess] == target:
                return guess + shift if guess + shift < len(nums) else guess + shift - len(nums)
            elif ajust[guess] < target:
                minidx = guess + 1
            else:
                maxidx = guess - 1
        return -1 