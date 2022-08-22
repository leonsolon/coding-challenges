#60'

#Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/


# Runtime: 77 ms, faster than 81.25% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 50.26% of Python3 online submissions for Longest Substring Without Repeating Characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
   
        N = len(s)
        if N == 0 or N == 1: return N
        
        start = 0
        m = {}
        longest = 0
        
        for i in range(N):
            c = s[i]
            if c in m:
                longest = max(longest, i - start)
                start = max(start, m[c] + 1) #start cannot be assigned to a value less than itself. Example: 'abba'
            m[c] = i #always keep the last index of the char 
        
        return max(longest, i - start + 1)



class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        sub = ''
        longest = 0
        for c in s:            
            if c in sub:
                idx = sub.find(c)
                sub = sub[idx+1:] + c
            else:
                sub = sub + c
                longest = max(longest, len(sub))
                
        return longest
