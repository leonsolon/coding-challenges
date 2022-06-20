def solution(A): # O(N) - 100% em Correctness - 28% em Performance
    if len(A) <=3:
        return 0

    A = A[1:-1]
    current_sum = 0
    min_a = float('inf')
    last_min_a = float('inf')
    max_slice = 0
    pos_start_slice = -1
    pos_end_slice = -1
    last_max_sum = 0
    max_sum = 0
    qtd_slices = 1
    slices = []
    for i, a in enumerate(A):
        if a < min_a:
            min_a = a

        if i==0:
            current_sum = a
            max_sum = 0
            pos_start_slice = 0
            pos_end_slice = 0

        elif a >= current_sum + a:
            slices.append([max_sum, pos_start_slice, pos_end_slice, last_min_a])
            pos_start_slice = i
            pos_end_slice = i
            qtd_slices +=1

            max_slice = max(max_slice, last_max_sum + max_sum)
            last_max_sum = max_sum
            current_sum = a
            max_sum = max(0,a)
        else:
            current_sum += a
            if current_sum >= max_sum:
                max_sum = current_sum
                pos_end_slice = i
                last_min_a = min_a


    else:
        slices.append([max_sum, pos_start_slice, pos_end_slice])
        if len(slices)==1 and pos_end_slice == len(A)-1:
            slices[0][0] -= min_a
        elif len(slices)==1:
            slices[0][0] -= min(0,last_min_a)
        # print(slices)


    last_sum = 0
    max_sum_double_slice = 0

    for i, slice in enumerate(slices):
        if i-1 >= 0 and slices[i-1][2] + 2 == slice[1]:
            last_sum = slices[i-1][0]
            # print(slices[i-1], slice)
        else:
            last_sum = 0

        if max_sum_double_slice < slice[0]+ last_sum:
            max_sum_double_slice = slice[0]+ last_sum
            # print(slice, last_sum, slices[i-1])

    return max_sum_double_slice

print(solution([1,3,4,2,-3,4,-10,1,1,4,-2,4,1])) # = 18
print(solution([-2, -3, -4, 1, -5, -6, -7])) # = 1
print(solution([5, 5, 5])) # = 0
print(solution([-8, 10, 20, -5, -7, -4])) # = 30
print(solution([5, 17, 0, 3])) # = 17
print(solution([-10,-10,8,-1,3,-20,7,-1,4,-10,-10])) # = 20
print(solution([3,2,6,-1,4,5,-1,2])) # = 17
print(solution([3,2,6,-1,4,5,1,2])) # = 18
print(solution( [ 2, 3, 5,-10]*3)) # = 20
print(solution( [1, 2, 3, 4,5,-15]*50)) # = 30
print(solution( [ 2, 3,-3,-2, 4,5,-15]*50)) # = 14
print(solution( [6, 1, 5, 6, 4, 2, 9, 4])) # = 26
print(solution( [0, 10, -5, -2, 0])) # = 10
print(solution( [-8, 10, 20, -5, -7, -4])) # = 30
#
# print(solution([3,2,6,-8,2,-8,5,-1,2]))
# print(solution([3,2,6,-1,4,5,-1,2]))
# print(solution([1,2,3]))
# print(solution([1,2,3,4]))
# print(solution([0, 10, -5, -2, 0]))
# print(solution([5, 17, 0, 3]))
print(solution([-24, -12, -27, -6, 10, -8, -11, 14, -12, -16, -19, 10, -7, 18, 27, 19, 1, -5, -30, -15, -2, -30, 15, 28, -18, 5, -22, -29, -2, 28, -1, 29, 21, -5, -14, -5, -8, -11, 9, -7, -26, 8, -12, -11, -30, -8, -8, 25, -1, -25, 9, -26, -1, 2, -28, 13, 22, -3, 4, -5]))

# print(solution([-10,-10,8,-1,3,-20,7,-1,4,-10,-10,-10,-10,8,-1,3,-20,7,-1,4,-10,-10,-10,-10,8,-1,3,-20,7,-1,4,-10,-10,-10,-10])) # = 20

import random
def gera_lista_aleatoria(tamanho, min, max):
    lista = []
    for i in range(0, tamanho):
        lista.append(random.randint(min,max))
    print(lista)
    return lista

# print(solution(gera_lista_aleatoria(60, -30,30)))


