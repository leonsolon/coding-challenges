# Week 1
# Recursion
# Combinations
# Runtime: 123 ms, faster than 84.86% of Python online submissions for Combinations.
# Memory Usage: 14.7 MB, less than 83.64% of Python online submissions for Combinations.

from itertools import combinations
def combine(n, k):
  c = combinations(range(1,n+1), k)
  return list(c)
