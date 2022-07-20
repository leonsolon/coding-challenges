# Lesson 7 Ex 01
# Brackets
# 87%
# 100% correctness
# 80% performance - problema quando há um número elevado de replaces para ser executados

def solution(S):
    
  len_S = len(S)
  if len(S) % 2 != 0:
    return 0
    
  for i in range(len_S//2):
    S = S.replace('()','').replace('[]','').replace('{}','')
   
  if len(S)== 0:
    return 1
  else:
    return 0
