def solution(A=[]): # ??? - 100% em Correctness - 50% em Performance
    # write your code in Python 3.6
    set_A = set(A)
    A_sorted = sorted(A)
    last_counted1 = None
    last_counted2 = None
    A2 = A_sorted
    A1 = []
    equi_leader = 0
    if len(set_A) == len(A):
        return 0
    if len(set_A) == 1:
        return len(A)-1
    for i in range(0,len(A)-1):

        A1.append(A[i])
        if last_counted1 == A[i]:
            count1 +=1
        A1_copy = A1.copy()
        set_A1_copy = set(A1_copy)
        while len(set_A1_copy) > 1:
            A1_copy.remove(set_A1_copy.pop())
            A1_copy.remove(set_A1_copy.pop())
            set_A1_copy = set(A1_copy)
        if len(A1_copy)>0:
            leader1 = A1_copy[0]
        else:
            leader1 = None


        A2.remove(A[i])
        if last_counted2 == A[i]:
            count2 -=1
        A2_copy = A2.copy()
        set_A2_copy = set(A2_copy)
        while len(set_A2_copy) > 1:
            A2_copy.remove(set_A2_copy.pop())
            A2_copy.remove(set_A2_copy.pop())
            set_A2_copy = set(A2_copy)
        if len(A2_copy)>0:
            leader2 = A2_copy[0]
        else:
            leader2 = None

        if leader1 == leader2 and leader2 != None:
            if last_counted1 != leader1:
                count1 = A1.count(leader1)
                last_counted1 = leader1
            if count1 > len(A1)/2:
                if last_counted2 != leader2:
                    count2 = A2.count(leader2)
                    last_counted2 = leader2
                if count2 > len(A2)/2:
                    equi_leader += 1


    return equi_leader

# print(solution([4, 4, 2, 5, 3, 4, 4, 4])) # = 3
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