from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
    
        aux = {')': '(', '}': '{', ']': '['}
        deq = deque()
        for char in s:
            if char in "({[":
                deq.append(char)
            elif not len(deq):
                return False
            elif deq.pop() != aux[char]:
                return False
                
        if len(deq):
            return False
        
        return True

# Runtime: 38 ms, faster than 80.77% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14 MB, less than 26.29% of Python3 online submissions for Valid Parentheses.