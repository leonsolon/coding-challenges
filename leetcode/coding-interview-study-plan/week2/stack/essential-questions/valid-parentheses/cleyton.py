#5'

# Runtime: 60 ms, faster than 22.46% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.8 MB, less than 71.96% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        
        
        mapp = {')':'(', '}': '{', ']': '['}
        stack = []
        for c in s:
            
            if c in mapp:
                if not stack or not (mapp[c] == stack.pop()):
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
