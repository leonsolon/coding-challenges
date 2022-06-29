def solution(A):
  N = len(A)
  A.sort()
  set_A = set(A)
  if len(set_A) < len(A):
    return 0
  if A[N-1] > N:
    return 0
  else:
    return 1
