'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

Success
Details 
Runtime: 372 ms, faster than 50.12% of Python3 online submissions for Binary Search.
Memory Usage: 15.5 MB, less than 24.09% of Python3 online submissions for Binary Search.
Next challenges:
Search in a Sorted Array of Unknown Size
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minindex = 0
        maxindex = len(nums)-1
        while minindex <= maxindex:
            guess = (maxindex+minindex)//2
            if nums[guess] == target:
                return guess
            elif nums[guess] < target:
                minindex = guess+1
            else:
                maxindex = guess-1
        return -1