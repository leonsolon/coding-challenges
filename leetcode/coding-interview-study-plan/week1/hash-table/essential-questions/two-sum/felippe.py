# Week 1
# Hash table
# Two Sum
# Runtime: 76 ms, faster than 66.90% of Python online submissions for Two Sum.
# Memory Usage: 14.5 MB, less than 22.77% of Python online submissions for Two Sum.

def twoSum(nums, target):

  d = {}
  for i,e in enumerate(nums):
    d[e] = i
  
  for i,e in enumerate(nums):
    dif = target - e
    if dif in d and i != d[dif]: 
      return [i, d[dif]]
    

assert twoSum([2,7,11,15], 9) == [0,1] or [1,0]
assert twoSum([3,2,4], 6) == [1,2] or [2,1]
assert twoSum([3,3], 6) == [0,1] or [1,0]
assert twoSum([-1,-2,-3,-4,-5], -8) == [2,4] or [4,2]
