#failed --> took more than 60 minutes to figure out a solution. So I just checked the discussion forum for an optimal solution.

#LINK: https://leetcode.com/problems/generate-parentheses/



#LESSON LEARNED: RECURSION. BACKTRACKING.

""" 
Concept: In every backtracking problem , there are two things to keep in mind , which we will explore here as well :

Base Case: Every problem of backtracking has some base case which tells us at which point we have to stop with the 

recursion process. In our case, when the length of our string has reached the maximum length(n*2), we stop with the 

recursion for that case and that is our base case.

Conditions: On observing carefully we find that there are two conditions present:

 - For adding (: If number of opening brackets(open) is less than the the given length(n) i.e.
    if max<n, then we can add (,else not.
 - For adding ): If number of close brackets(close) is less than the opening brackets(open), i.e.
    if open<close, we can add ), else not """
# Link: https://leetcode.com/problems/generate-parentheses/discuss/1131364/Clear-and-simple-explanation-with-intuition%3A-100-faster


from typing import List

# Runtime: 68 ms, faster than 23.77% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.1 MB, less than 98.06% of Python3 online submissions for Generate Parentheses.
class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def helper(result, curr_str, open, close):
            if open == close == 0:
                result.append(curr_str)
                return

            if open > 0: #There are still open parentheses to be added
                helper(result, curr_str + '(', open - 1, close)

            if close > open: # close > open means more '(' were added then ')'
                helper(result, curr_str + ')', open, close - 1)

        res = []
        helper(res, '', n, n)
        return res


