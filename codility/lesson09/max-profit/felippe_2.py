# Lesson 9 EX 01
# MaxProfit
# 66%
# 100% correctness
# 25% performance
# as diferenças podem ser calculadas por combinação das diferenças entre elementos adjacentes
# continua com problema de performance

from itertools import accumulate
def solution(A):
  
  if len(A) < 2: # edge case
    return 0
  
  if len(A) == 2: # edge case
    difference = A[-1] - A[0]
    if difference > 0:
      return difference
    else:
      return 0
  
  difference = 0
  count = 0
  list_dif = []
  profit = [0] # o zero é incluído para não retornar profit negativo
  
  for i in range(len(A)-1):
    difference = A[i+1] - A[i]
    list_dif.append(difference)
  
  list_dif2= list_dif.copy()
  list_dif.reverse() # para utilizar o pop(), para fins de performance
  
  while list_dif:
    profit += list(accumulate(list_dif))
    list_dif.pop()

  profit = profit + list_dif2
  
  return max(profit)
