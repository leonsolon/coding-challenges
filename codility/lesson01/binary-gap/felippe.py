def solution(N):
    list_sizes=[]
    binario = bin(N).replace('0b','').strip('0').split('1')
    for i in binario:
        size=len(i)
        list_sizes.append(size)
    return max(list_sizes)
