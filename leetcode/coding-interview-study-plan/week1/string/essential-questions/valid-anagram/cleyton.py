#1'

#Link: https://leetcode.com/problems/valid-anagram/

# Runtime: 76 ms, faster than 52.67% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.2 MB, less than 11.94% of Python3 online submissions for Valid Anagram.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t) #O(N log N) time, O(log N) space

from collections import Counter
class Solution2(object):
    def isAnagram(self, s, t):

        s = Counter(s)
        t = Counter(t)
        
        return s - t == {} and t - s == {} #O(N) time, O(1) space
