def solution(A):
  N = len(A)
  sum_A = sum(A)
  difference = []
  sum_A_first = 0
  for i in range(0,N-1):
    sum_A_first = sum_A_first + A[i]
    difference.append(abs(2*sum_A_first - sum_A))
  return min(difference)
