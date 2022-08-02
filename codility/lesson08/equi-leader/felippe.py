from collections import Counter

def solution(A):

    # o equileader deve ser o dominator da lista
    N = len(A)
    if N == 1:
      return 0
    
    # encontrando o dominator
    c = Counter(A)
    list_dominator = c.most_common(1)
    dominator = list_dominator[0][0]
    count_dominator = list_dominator[0][1]
    
    if count_dominator <= N//2: # a lista não tem um dominator
        return 0
    
    eq_left = 0
    eq_right = 0
    equileader = 0
       
    for i in range(N-1):
      left_size = i + 1
      right_size = N - left_size
      
      if A[i] == dominator: # percorrendo a lista e contando os dominators parciais (left)
        eq_left +=1
      eq_right = count_dominator - eq_left # o número de dominators do lado direito será o total menos os do lado esquerdo

      if eq_left > left_size // 2 and eq_right > right_size // 2: # os dominators de cada lado de fato são equileaders 
        equileader += 1
    
    return equileader
