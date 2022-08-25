#24'

#Link: https://leetcode.com/problems/product-of-array-except-self/

# Runtime: 249 ms, faster than 89.28% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.4 MB, less than 18.46% of Python3 online submissions for Product of Array Except Self.

class Solution: 
    def productExceptSelf(self, nums):
        
        N = len(nums)
        left = [1]*(N)
        right = [1]*(N)
        for i in range(1,N):
            left[i] = left[i-1]*nums[i-1]
            right[-i-1] = right[-i]*nums[-i]
        
        return [a*b for a,b in zip(left,right)]
