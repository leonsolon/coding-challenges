def solution(X, A):
  set_leaves = set(range(1,X+1))
  for index, element in enumerate(A):
    set_leaves.discard(element)
    if len(set_leaves) == 0:
      return index
  return -1 
