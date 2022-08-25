# Week 2
# Sorting and searching
# Binary Search
# Runtime: 258 ms, faster than 67.71% of Python online submissions for Binary Search.
# Memory Usage: 14.6 MB, less than 78.86% of Python online submissions for Binary Search.

def search(nums, target):
  
  if len(nums) <= 3: # edge case
    if target in nums:
      return nums.index(target)
    else:
      return -1

  first = 0
  last = len(nums) - 1
  middle = len(nums) // 2
  
  while target != nums[middle]:
    
    if last <= first: # target not finded
      return -1

    if target < nums[middle]: # left side
      last = middle - 1
      middle = first + (last - first) // 2

    if target > nums[middle]: # right side
      first = middle + 1
      middle = first + (last - first) // 2
 
  
  return middle

assert search([-1,0,3,5,9,12], 9) == 4
assert search([-1,0,3,5,9,12], 2) == -1
