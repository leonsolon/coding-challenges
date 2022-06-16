def solution(A=[]): # ??? - 80% em Correctness - 50% em Performance
    # write your code in Python 3.6
    print(A)
    A_index = zip(A, range(0,len(A)))
    A_sorted = sorted(A_index)
    len_A = len(A)
    count_list = []
    last_a = None
    index_list =[]
    count = 1
    for i,(a, index) in enumerate(A_sorted):
        if a != last_a:
            if i !=0:
                count_list.append([last_a, count, index_list,index_list[1:]])
            index_list=[]
            count = 1
        else:
            count +=1
        index_list.append(index)
        last_a = a
    else:
        count_list.append([last_a, count, index_list,index_list[1:]])


    equi_leader = 0
    for count in count_list:
        if count[1] ==1:
            pass
        else:
            for i,index in enumerate(count[2]):
                if i + 1 <len(count[2]):
                    folga = min(2*i - index, count[2][i+1] - index -1)
                #     i+1 = Quantidade de elementos
                #     index = Posição do elemento atual
                #     folga = (Quantidade de elementos - 1) - Outros elementos ja na lista
                #     Outros elementos ja na lista = Posição do elemento atual - 1 - Quantidade de elementos
                    folga = max(0,folga)
                else:
                    folga = 0
                len_parte_1 = index + 1 + folga

                len_parte_2 = len_A - len_parte_1

                if i+1 >len_parte_1/2 and (count[1] - (i+1)) > len_parte_2/2:
                    equi_leader+=1
    return equi_leader

import random
def gera_lista_aleatoria(tamanho, min, max):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(min,max))
    return lista

print(solution(gera_lista_aleatoria(500,1,2)))
print(solution([0]*49 +[1]*51))