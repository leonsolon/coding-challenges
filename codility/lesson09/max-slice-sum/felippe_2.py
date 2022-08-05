# Lesson 9 EX 02
# MaxSliceSum
# 100%

def solution(A):

  if len(A) <= 2: # edge case
    return max(max(A), sum(A))
  
  max_accumulate = 0
  max_slice_sum = max(A)
  accumulate = 0  
  
  for e in A:
    accumulate = max_accumulate + e
    max_accumulate = max(e, accumulate)
    max_slice_sum = max(max_slice_sum, max_accumulate)
  
  return max_slice_sum
