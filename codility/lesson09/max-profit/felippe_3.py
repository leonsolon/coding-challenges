# Lesson 9 EX 01
# MaxProfit
# 100% 

def solution(A):
  
  if len(A) < 2:
    return 0
  
  minimo = max(A)
  max_profit = 0
  profit = 0

  for i in range(len(A)):
    minimo = min(minimo, A[i])
    profit = A[i] - minimo
    max_profit = max(max_profit, profit)
  
  return max_profit
