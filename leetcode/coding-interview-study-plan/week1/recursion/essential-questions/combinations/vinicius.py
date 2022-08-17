'''
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.


Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n


Success
Details 
Runtime: 104 ms, faster than 94.53% of Python3 online submissions for Combinations.
Memory Usage: 15.8 MB, less than 85.75% of Python3 online submissions for Combinations.
Next challenges:
Combination Sum
Permutations
'''

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return [list(i) for i in combinations(range(1,n+1),k)]

# NÃO CONSEGUI FAZER COM RECURSÃO