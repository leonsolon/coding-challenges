### TapeEquilibrium 
## Solução com 53% de resultado: 100% correta, mas com problemas de performance
def solution(A):
  N = len(A)
  difference = []
  for p in range(1,N):
    A_first = A[:p]
    A_second = A[p:]
    difference.append(abs(sum(A_first)-sum(A_second)))
  return min(difference)
