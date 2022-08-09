'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocount = 0
        for i in nums:
            if i == 0:
                zerocount +=1
            if zerocount > 1:
                return [0]*len(nums)
        from itertools import accumulate
        prefix_prods = list(accumulate(nums, operator.mul))
        suffix_prods = list(accumulate(nums[::-1], operator.mul))
        answer = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                answer[i] = suffix_prods[-2]
            elif i == len(nums)-1:
                answer[i] = prefix_prods[-2]
            else:
                if prefix_prods[i] != 0:
                    answer[i] = int(prefix_prods[-1] * prefix_prods[i]**-1 * prefix_prods[i-1])
                else:
                    answer[i] = int(suffix_prods[i-1]*prefix_prods[i-1])
        return answer
