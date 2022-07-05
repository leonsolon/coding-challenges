def solution(A):
  if sum(A) == len(A) or sum(A) == 0: # testando se há apenas 1 ou 0
    return 0
  count_zero = 0
  count_cars = 0
  for index, element in enumerate(A): # percorrendo a lista e contando os zeros e os carros que passaram
    if element == 0:
      count_zero +=1
    else:
      count_cars = count_cars + count_zero  
      if count_cars > 1000000000:
          return -1
  return count_cars
