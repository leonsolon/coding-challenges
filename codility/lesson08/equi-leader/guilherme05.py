def leader(A=[]):
    len_A = len(A)
    count_leader = 0
    for a in A:
        if count_leader==0:
            count_leader +=1
            leader = a
        else:
            if leader == a:
                count_leader +=1
            else:
                count_leader -=1
    if count_leader >0:
        count = A.count(leader)
        if count > len_A/2:
            return leader
        else:
            return None
    else:
        return None

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
        leader1 = leader(A1)
        if leader1 == None:
            continue

        A2 = A[i+1:]
        leader2 = leader(A2)

        if leader1 == leader2 and leader2 != None:
            equi_leader += 1


    return equi_leader

print(solution([4, 4, 2, 5, 3, 4, 4, 4])) # = 3
print(solution([4, 3, 4, 4, 4, 2])) # = 2
print(solution([1, 2, 3, 4, 5])) # = 0
#
import random
def gera_lista_aleatoria(tamanho, min, max):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(min,max))
    return lista

print(solution(gera_lista_aleatoria(5000,1,2)))
# print(solution([0]*49 +[1]*51))