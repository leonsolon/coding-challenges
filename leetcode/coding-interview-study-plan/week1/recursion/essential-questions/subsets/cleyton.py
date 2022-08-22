#32'

#Link: https://leetcode.com/problems/subsets/

#LESSON LEARNED: find all possible combinations of any list with unique elements!!!


#DESCRIPTION:
    # Given an integer array nums of unique elements, return all possible subsets (the power set).
    # The solution set must not contain duplicate subsets. Return the solution in any order.

# Runtime: 37 ms, faster than 90.30% of Python3 online submissions for Subsets.
# Memory Usage: 14.2 MB, less than 35.80% of Python3 online submissions for Subsets.
from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def combine(arr: int, k: int) -> List[List[int]]:
            d = [0] #starts with index 0 of the array (arr)
            res = []
            n = len(arr)
            while d:
                if len(d) == k:
                    res.append([arr[x] for x in d]) #d contains the indices of the elements in arr

                    while d and (x := d.pop()) == n - (k - len(d)): 
                        pass

                    #if d is empty and x >= n - (k - len(d)) means we must stop. Therefore, do not append!
                    if d or x < n - (k - len(d)):
                        d.append(x + 1)    
                else:
                    d.append(d[-1] + 1) #[0] --> [0,1] --> [0,1,2] -->... list d (of indices in arr) is always sorted in ascending order to avoid duplicates!

            return res
        
        out = [[]]
        
        for i in range(1, len(nums) + 1):
            out.extend(combine(nums, i))
        
        return out

# print(combine([1,2,3,4,5],1))
# print(combine([1,2,3,4,5],2))
# print(combine([1,2,3,4,5],3))
# print(combine([1,2,3,4,5],4))
# print(combine([1,2,3,4,5],5))
