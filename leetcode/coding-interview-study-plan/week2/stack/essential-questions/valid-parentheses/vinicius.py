'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

Success
Details 
Runtime: 40 ms, faster than 75.35% of Python3 online submissions for Valid Parentheses.
Memory Usage: 13.9 MB, less than 71.96% of Python3 online submissions for Valid Parentheses.
Next challenges:
Longest Valid Parentheses
Remove Invalid Parentheses
Check If Word Is Valid After Substitutions
Check if a Parentheses String Can Be Valid
Move Pieces to Obtain a String
'''
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i in '({[':
                stack+=i
            elif i == ')':
                if stack:
                    if stack.pop() != '(':
                        return False
                else:
                    return False
            elif i == ']':
                if stack:
                    if stack.pop() != '[':
                        return False
                else:
                    return False
            else:
                if stack:
                    if stack.pop() != '{':
                        return False
                else:
                    return False
        if not stack:
            return True
        else:
            return False