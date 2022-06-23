## solução com 54%
# 100% correctness
# 0% performance

def solution(X, A):
  set_leaves = set(range(1,X+1))
  for i in range(0,len(A)+1):
    set_A = set(A[:i+1])
    if set_leaves.intersection(set_A) == set_leaves: #todas as folhas caíram
      return i
  return -1 
