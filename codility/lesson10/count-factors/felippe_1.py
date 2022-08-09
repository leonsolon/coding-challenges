# Lesson 10 EX 01
# CountFactors
# 85%
# 100% correctness
# 66% performance 
# timeout: N=780291637(prime) and N=MAX_INT, ou seja, dois casos que são necessários percorrer a lista (quase) inteira

from math import sqrt
def solution(N):

  count = 0
  list_factors = [N]
  i = 1
  
  # a lógica é contar duas vezes a divisão por i e incluir os maiores fatores do número em uma lista
  # e sair do loop quando i for maior do que o último fator incluído
  
  while i <= list_factors[-1]: 
    if (N % i == 0):
      count += 2
      list_factors.append(N//i) 
    i += 1
  
  sqrt_N = sqrt(N)
  if sqrt_N.is_integer(): # casos de quadrados perfeitos, como 16 (4*4)
    return count - 1
  else:
    return count - 2 
