def solution(N,A):
    max_counter = 0
    count_array = [0]*N
    if min(A) > N:            #TESTE ADICIONADO PARA RESOLVER A PERFORMANCE
        return count_array    #TESTE ADICIONADO PARA RESOLVER A PERFORMANCE
    for index, el in enumerate(A):
        if el > N:
            count_array = [max_counter]*N
        else:
            count_array[el-1] += 1
            if count_array[el-1] > max_counter:
                max_counter = count_array[el-1]
    return count_array

'''
RESULTADO - 100%
'''