# Lesson 8 Ex 01
# Dominator
# 100%

from collections import Counter

def solution(A):
    
    if len(A) == 0:
      return -1
    
    c = Counter(A)
    list_dominator = c.most_common(1)
    dominator = list_dominator[0][0]
    count_dominator = list_dominator[0][1]
    
    if count_dominator <= len(A)//2:
        return -1
       
    return A.index(dominator)
