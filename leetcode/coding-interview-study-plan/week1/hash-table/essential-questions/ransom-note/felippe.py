# Week 1
# Hash table
# Ransom Note
# Runtime: 148 ms, faster than 24.49% of Python online submissions for Ransom Note.
# Memory Usage: 13.9 MB, less than 15.19% of Python online submissions for Ransom Note.

from collections import Counter
def canConstruct(ransomNote, magazine):

  C_ransom = Counter(ransomNote)
  C_magazine = Counter(magazine)
  dict_magazine = dict(C_magazine)
  
  for key, elem in C_ransom.items():
    if key not in C_magazine.elements():
      return False
    else:
      if elem > dict_magazine[key]:
        return False
  
  
  return True
  
  assert canConstruct("a", "b") == False
  assert canConstruct("aa", "ab") == False
  assert canConstruct("aa", "aab") == True
