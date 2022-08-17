'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order. 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

Success
Details 

Runtime: 36 ms, faster than 92.06% of Python3 online submissions for Subsets.
Memory Usage: 14.1 MB, less than 35.80% of Python3 online submissions for Subsets.

Next challenges:
Subsets II
Generalized Abbreviation
Letter Case Permutation
Find Array Given Subset Sums
Count Number of Maximum Bitwise-OR Subsets
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        from itertools import combinations
        for k in range(len(nums)+1):
            output += (list(i) for i in combinations(nums,k))
        return output

# NÃO CONSEGUI FAZER COM RECURSÃO