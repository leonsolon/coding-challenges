#8'

#Link: https://leetcode.com/problems/valid-palindrome/

# Runtime: 68 ms, faster than 63.43% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.7 MB, less than 42.11% of Python3 online submissions for Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        s = ''.join([c for c in s if c.isalnum()]).lower()        
        return s == s[::-1]
