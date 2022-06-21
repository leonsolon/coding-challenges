def solution(A):
  N = len(A)
  A.sort()
  if N == 0:  # caso extremo
    return 1
  if A[0] != 1:  # faltando o primeiro elemento
    return 1
  if N == 1 and A[0] == 1:  # caso extremo
    return 2
  if A[N-1] <= N:  # solução quando está faltando o último elemento
    return (A[N-1]+1)
  for i in range(0,N-1): # caso geral
    if A[i+1] - A[i] == 2:
      return (A[i]+1)
