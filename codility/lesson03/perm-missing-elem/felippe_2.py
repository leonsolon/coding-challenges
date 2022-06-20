def solution(A):
  N = len(A)
  A_set = set(A)
  B_set = set(range(1,N+2))
  result = B_set.difference(A_set)
  return result.pop()
