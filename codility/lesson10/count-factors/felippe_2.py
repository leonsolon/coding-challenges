# Lesson 10 EX 01
# CountFactors
# 100%

N = 24
def solution(N):

  count = 0
  i = 1
  while (i * i < N): # fatores simétricos
    if (N % i == 0):
      count += 2
    i += 1
  if (i * i == N): # quando o fator simétrico é do k^2, deve ser contado uma vez. Por exemplo, 6 * 6 = 36
    count += 1
  
  return count
