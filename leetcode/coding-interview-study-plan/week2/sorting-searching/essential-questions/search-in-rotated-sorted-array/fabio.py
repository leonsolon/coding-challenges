def solution(nums, target):

    # Edge Case
    if len(nums) <= 3:
        if target in nums: return nums.index(target)
        else: return -1
    
    # Finding Pivot
    def find_pivot(nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[left] < nums[middle] < nums[right]: return 0
            elif nums[middle-1] > nums[middle]: return middle
            elif nums[middle] > nums[middle+1]: return middle + 1
            elif nums[middle] < nums[left]: right = middle - 1
            elif nums[middle] > nums[right]: left = middle + 1
    pivot = find_pivot(nums)
    if pivot:
        nums = nums[pivot:] + nums[:pivot]
    
    # Binary Search
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target: return (middle + pivot) % len(nums)
        if nums[middle] < target: left = middle + 1
        if nums[middle] > target: right = middle - 1
    
    return -1

# Runtime: 66 ms, faster than 49.02% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.4 MB, less than 18.13% of Python3 online submissions for Search in Rotated Sorted Array.