def get_leader(A=[]):
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
            return (leader, count)
        else:
            return (None,0)
    else:
        return (None,0)

def get_all_leaders(A):
    leader= None
    next_leader = None
    leaders = []
    for i in range(0,len(A)):

        if i == 0:
            (leader, count) = get_leader(A)
        elif i >0:
            excluido = A[0]
            A = A[1:]
            if next_leader != None:
                leader = next_leader
                count = next_count
                next_leader = None
                leaders.append(leader)
                continue

            if excluido != A[0]:
                next_leader = leader
                next_count = count
                if A[0] == leader or excluido== leader:
                    next_count -= 1

            if leader == excluido:
                count -=1
                if len(A)/2 >= count:
                    (leader,count) = get_leader(A)

            else:
                if leader==None:
                    (leader, count) = get_leader(A)
        leaders.append(leader)
    return leaders[::-1]

def solution(A=[]): # ??? - 100% em Correctness - 50% em Performance
    # write your code in Python 3.6
    set_A = set(A)
    A_sorted = sorted(A)
    last_counted1 = None
    last_counted2 = None
    A2 = A_sorted
    A1 = []
    equi_leader = 0
    count = 0
    if len(set_A) == len(A):
        return 0
    if len(set_A) == 1:
        return len(A)-1

    leaders1 = get_all_leaders(A[::-1])
    leaders1 = leaders1[0:-1]
    leaders2 = get_all_leaders(A)
    leaders2 = leaders2[0:-1]
    leaders2 = leaders2[::-1]
    leaders = zip(leaders1,leaders2)
    for l in leaders:
        if l[0]!= None and l[0] == l[1]:
            equi_leader +=1
    return equi_leader

print(solution([4, 4, 2, 5, 3, 4, 4, 4])) # = 3
print(solution([4, 3, 4, 4, 4, 2])) # = 2
print(solution([1, 2, 3, 4, 5])) # = 0
# #
# import random
# def gera_lista_aleatoria(tamanho, min, max):
#     lista = []
#     for i in range(0, tamanho):
#         lista.append(random.randint(min,max))
#     return lista
#
# print(solution(gera_lista_aleatoria(5000,1,2)))
# print(solution([0]*49 +[1]*51))