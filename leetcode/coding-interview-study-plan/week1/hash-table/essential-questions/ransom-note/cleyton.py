#2'


# Runtime: 99 ms, faster than 43.11% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.2 MB, less than 20.43% of Python3 online submissions for Ransom Note.
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mCount = Counter(magazine)
        rCount = Counter(ransomNote)
        
        return rCount - mCount == {}
