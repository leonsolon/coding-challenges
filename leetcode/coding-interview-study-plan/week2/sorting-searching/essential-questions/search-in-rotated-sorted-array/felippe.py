# Week 2
# Sorting and searching
# Search in Rotated Sorted Array
# Runtime: 46 ms, faster than 38.36% of Python online submissions for Search in Rotated Sorted Array.
# Memory Usage: 13.7 MB, less than 39.46% of Python online submissions for Search in Rotated Sorted Array.

def search(nums, target):
        
        if len(nums) <= 3: # edge case
            if target in nums:
                return nums.index(target)
            else:
                return -1
        
        
        def binsearch(nums, target):
  
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
        
        idx = 0
        idx_list = list(range(len(nums)))
        for i,e in enumerate(nums):
            if i == len(nums) - 1:
                break
            if nums[i+1] < nums [i]:
                idx = i + 1
                break
  
        nums_sorted = nums[idx:] + nums[:idx]
        idx_sorted = idx_list[idx:] + idx_list[:idx]
        #print(nums_sorted)
        result = binsearch(nums_sorted, target)
        #print(result, idx)
        if result == -1:
            return -1
  
        return idx_sorted[result]


assert search([4,5,6,7,0,1,2],0) == 4
assert search([4,5,6,7,0,1,2],3) == -1
assert search([4,5,6,7,0,1,2],0) == 4
assert search([7,8,1,2,3,4,5,6], 2) == 3
assert search([8,9,0,1,3,4,6], 7) == -1
