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

        A1 = A[0:i+1]
        len_A1 = len(A1)
        if last_counted1 == A[i]:
            count1 +=1
        set_A1 = set(A1)
        while len(set_A1) > 1:
            A1.remove(set_A1.pop())
            A1.remove(set_A1.pop())
            set_A1 = set(A1)
        if len(A1)>0:
            leader1 = A1[0]
        else:
            leader1 = None


        A2 = A[i+1:]
        len_A2 = len(A2)
        if last_counted2 == A[i]:
            count2 -=1
        set_A2 = set(A2)
        while len(set_A2) > 1:
            A2.remove(set_A2.pop())
            A2.remove(set_A2.pop())
            set_A2 = set(A2)
        if len(A2)>0:
            leader2 = A2[0]
        else:
            leader2 = None

        if leader1 == leader2 and leader2 != None:
            if last_counted1 != leader1:
                count1 = A[0:i+1].count(leader1)
                last_counted1 = leader1
            if count1 > len_A1/2:
                if last_counted2 != leader2:
                    count2 = A[i+1:].count(leader2)
                    last_counted2 = leader2
                if count2 > len_A2/2:
                    equi_leader += 1


    return equi_leader

print(solution([4, 4, 2, 5, 3, 4, 4, 4])) # = 3
print(solution([4, 3, 4, 4, 4, 2])) # = 2
print(solution([1, 2, 3, 4, 5])) # = 0
#
# import random
# def gera_lista_aleatoria(tamanho, min, max):
#     lista = []
#     for i in range(0, tamanho):
#         lista.append(random.randint(min,max))
#     return lista
#
# print(solution(gera_lista_aleatoria(500,1,2)))
# print(solution([0]*49 +[1]*51))