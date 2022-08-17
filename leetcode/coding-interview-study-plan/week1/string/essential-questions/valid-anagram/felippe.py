# Week 1
# String
# Valid Anagram
# Runtime: 94 ms, faster than 18.93% of Python online submissions for Valid Anagram.
# Memory Usage: 14.7 MB, less than 40.07% of Python online submissions for Valid Anagram.

def isAnagram(s, t):
    
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False
