## resultado 100%

def solution(N, A):
  counter = [0]*N
  max_counter = set()
  for element in A:
    if 1 <= element <= N:
      counter[element-1] +=1
      max_counter.add(counter[element-1])
    if element == N+1 and len(max_counter) > 0: #teste do tamanho do max_counter: se o elemento N+1 estiver na primeira posição
      counter = [max(max_counter)]*N
      max_counter.clear() #necessário limpar o contador para fins de performance
  return counter
