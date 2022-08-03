# Lesson 9 EX 02
# MaxSliceSum
# 84%
# 100% correctness
# 60% performance
# timeout error

from itertools import accumulate
def solution(A):
  
  if len(A) <= 2: # edge case
    return max(max(A), sum(A))
  
  acc_sum = []
  
  while A:
    acc_sum += list(accumulate(A))
    A.pop(0)
      
  return max(acc_sum)
