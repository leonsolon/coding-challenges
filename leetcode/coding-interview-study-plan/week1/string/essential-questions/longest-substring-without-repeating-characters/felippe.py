# Week 1
# String
# Longest Substring Without Repeating Characters
# Runtime: 115 ms, faster than 33.54% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 14.1 MB, less than 48.29% of Python online submissions for Longest Substring Without Repeating Characters.


def lengthOfLongestSubstring(s):

  if len(s) == 1: return 1
  max_sub = 0
  substring = str()
  
  for i in range(len(s)):
    if s[i] in substring:
      idx = substring.index(s[i])
      substring = substring[idx + 1:] + s[i]
      #print(substring)
      max_sub = max(max_sub, len(substring))
    else:
      substring += s[i]
      #print(substring)
      max_sub = max(max_sub, len(substring))
  
  return max_sub

assert lengthOfLongestSubstring("abcabcbb") == 3
assert lengthOfLongestSubstring("bbbbb") == 1
assert lengthOfLongestSubstring("pwwkew") == 3
assert lengthOfLongestSubstring("anviaj") == 5
assert lengthOfLongestSubstring("ckilbkd") == 5
assert lengthOfLongestSubstring("wobgrovw") == 6
