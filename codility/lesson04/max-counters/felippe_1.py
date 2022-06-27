## resultado 66%:  correctness = 100%; performance = 40%

def solution(N, A):
  counter = [0]*N
  for element in A:
    if element <= N:
      counter[element-1] +=1
    if element == N+1:
      counter = [max(counter)]*N
  return counter
