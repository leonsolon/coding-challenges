# Lesson 9 EX 03
# MaxDoubleSlice
# 100%

def solution(A):

  if len(A) == 3: # edge case
    return 0
  
  A.pop() # o primeiro e o último elemento de A nunca estarão no slice
  A.pop(0)
    
  max_slice1 = [0] # primeira iteração
  accumulate1 = 0  
    
  for e in A:
    accumulate1 = max(accumulate1 + e, 0) # retirar os números negativos do accumulate
    max_slice1.append(accumulate1)
    
  max_slice1.pop() # o último elemento é o slice do vetor completo e não é possível ao cortar dois slices

  A.reverse()
  max_slice2 = [] 
  accumulate2 = 0  
    
  for e in A:
    accumulate2 = max(accumulate2 + e, 0) # retirar os números negativos do accumulate
    max_slice2.append(accumulate2)
 
  max_slice2.pop() # o último elemento é o slice do vetor completo e não é possível ao cortar dois slices
  max_slice2.reverse()
  max_slice2.append(0) # primeira iteração
  
  max_slice_sum = []
  
  for i in range(len(max_slice1)):
    max_slice_sum.append(max_slice1[i] + max_slice2[i]) 

  return max(max_slice_sum)
