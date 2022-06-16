def solution(A=[]): # ??? - 80% em Correctness - 50% em Performance
    # write your code in Python 3.6
    print(A)
    set_A = set(A)
    A_sorted = sorted(A)
    count_leader_A1 = 0
    leader1 = None
    last_counted = None
    A2 = A_sorted
    equi_leader = 0
    if len(set_A) == len(A):
        return 0
    if len(set_A) == 1:
        return len(A)-1
    for i in range(0,len(A)-1):

        A2.remove(A[i])
        len_A2 = len(A2)
        leader2 = A2[len_A2 // 2]
        if last_counted == A[i]:
            count -= 1
        else:
            count = A2.count(leader2)
            last_counted = leader2

        if count <= len_A2 / 2:
            leader2 = None



        if leader1== None:
            count_leader_A1 =1
            leader1 = A[i]
        elif A[i] == leader1:
            count_leader_A1 +=1
        elif A[i] != leader1:
            count_leader_A1 -=1
            if count_leader_A1 == 0:
                leader1 = None

        if leader1 == leader2 and leader2 != None:
            equi_leader += 1


    return equi_leader

# print(solution([4, 4, 2, 5, 3, 4, 4, 4])) # =3
# print(solution([4, 3, 4, 4, 4, 2])) # = 2
# print(solution([1, 2, 3, 4, 5])) # = 0

import random
def gera_lista_aleatoria(tamanho, min, max):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(min,max))
    return lista

print(solution(gera_lista_aleatoria(500,1,2)))
# print(solution([0]*49 +[1]*51))