# Week 2
# Stacks
# Valid Parentheses
# Runtime: 26 ms, faster than 63.60% of Python online submissions for Valid Parentheses.
# Memory Usage: 13.7 MB, less than 31.57% of Python online submissions for Valid Parentheses.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0: # odd number of brackets
            return False
        
        open_list = ['(', '[', '{']
        close_list = [')', ']', '}']
        stack = [] # stack of the index of the open brackets
        
        for e in s:
            if e in open_list:
                stack.append(open_list.index(e)) # save the index of the bracket
            if e in close_list:
                if len(stack) == 0: # testing if there is a open bracket
                    return False 
                if close_list.index(e) == stack[-1]: # testing if the close brackt has the same type of the last opened
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
