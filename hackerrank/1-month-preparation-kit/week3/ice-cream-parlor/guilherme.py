from itertools import combinations
def icecreamParlor(m, arr):
    possib = combinations(arr, 2)
    for p in possib:
        if sum(p)==m:
            break
    # Write your code here
    result = []
    result.append(arr.index(p[0])+1)
    if p[1] == p[0]:
        arr[result[0]-1] = 'used'
    result.append(arr.index(p[1])+1)
    return result
