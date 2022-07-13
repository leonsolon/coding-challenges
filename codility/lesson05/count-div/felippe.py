def solution(A, B, K):
  if B == 0:
    return 1
  if K > B:
    return 0
  if A == B:
    if A % K == 0:
      return 1
    else:
      return 0
  first = 0
  last = 0
  for i in range(A, B+1):
    if i % K == 0:
      first = i # primeiro elemento da PA
      break
  for j in range(B, -1, -1):
    if j % K == 0:
      last = j # último elemento da PA
      break
  N = ((last - first)//K) + 1 # número de elementos em uma PA
  return N
