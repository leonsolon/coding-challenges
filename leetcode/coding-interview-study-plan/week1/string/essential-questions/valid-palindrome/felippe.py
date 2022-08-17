# Week 1
# String
# Valid Palindrome
# Runtime: 2702 ms, faster than 5.01% of Python online submissions for Valid Palindrome.
# Memory Usage: 14.9 MB, less than 41.18% of Python online submissions for Valid Palindrome.

def isPalindrome(s):

  if len(s) == 1:
    return True
  
  s = s.lower()
  
  if s.isalnum():
    if s == s[::-1]: return True
    else: return False
  else:
    for e in s:
      if e.isalnum() == False:
        s = s.replace(e,'')
    
    if s == s[::-1]: return True
    else: return False
  

assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("race a car") == False
assert isPalindrome(" ") == True
