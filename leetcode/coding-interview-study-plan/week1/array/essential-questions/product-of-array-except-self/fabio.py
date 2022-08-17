'''
FUNCIONOU, MAS NÃO PASSOU NA PERFORMANCE
class Solution():
    def productExceptSelf(self, nums: list) -> list:
        from functools import reduce
        from itertools import chain
        return [reduce(lambda x, y: x*y, chain(nums[:i], nums[i+1:]), 1) for i, _ in enumerate(nums)]
'''

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        N = len(nums)
        
        A = [0 for _ in range(N)]
        temp = 1
        for i, num in enumerate(nums):
            A[i] = temp
            temp *= num
        
        B = [0 for _ in range(N)]
        temp = 1
        for i, num in enumerate(nums[::-1]):
            B[N-i-1] = temp
            temp *= num
        
        return [a*b for a, b in zip(A, B)]

# Runtime: 303 ms, faster than 70.72% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.5 MB, less than 18.46% of Python3 online submissions for Product of Array Except Self.

s = Solution()
print(s.productExceptSelf([1,2,3,4]))