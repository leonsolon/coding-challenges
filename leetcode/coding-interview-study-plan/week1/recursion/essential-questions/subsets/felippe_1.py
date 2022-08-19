# Week 1
# Recursion
# Subsets
# Runtime: 32 ms, faster than 47.58% of Python online submissions for Subsets.
# Memory Usage: 13.7 MB, less than 45.75% of Python online submissions for Subsets.

from itertools import combinations
def subsets(nums):
  N = len(nums)
  result = [[]]
  for k in range(1, N+1):
    c = combinations(nums, k)
    result += list(c)
  
  return result
