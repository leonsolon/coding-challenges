def solution(A, K):
  N = len(A) 
  if N == 0: # teste de array vazio - score inicial foi 87%, sem este teste
    return (A)
  else:
    for i in range(1,K+1):
      B = []
      last = A[N-1]
      for i in range(N):
        B.append(A[i-1])
      B[0] = last
      A = B.copy()
    return (A)
