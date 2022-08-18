# Week 1 - Array
# Maximum Subarray
# Runtime: 772 ms, faster than 65.40% of Python online submissions for Maximum Subarray.
# Memory Usage: 25.7 MB, less than 47.38% of Python online submissions for Maximum Subarray.

def maxSubArray(nums):

  sum = -float('inf')
  max_sum = -float('inf')

  for e in nums:
    sum = max(e, sum + e)
    max_sum = max(sum, max_sum)

  return max_sum



assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
assert maxSubArray([1]) == 1
assert maxSubArray([5,4,-1,7,8]) == 23
