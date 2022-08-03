# Lesson 9 EX 01
# MaxProfit
# versão força-bruta
# 66% 
# 100% correctness
# 25% performance


def solution(A):
  
  if len(A) < 2:
    return 0
  
  profit = [0] # o zero é incluído para não retornar profit negativo
  
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      profit.append(A[j]-A[i])
  
  return max(profit)
  
