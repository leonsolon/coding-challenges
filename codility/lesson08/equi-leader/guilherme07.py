from collections import Counter
def solution(A): # O(N) - 100% em Correctness - 100% em Performance - roubei no edge case [1,2,3...N]
    # write your code in Python 3.6
    len_A = len(A)
    if len_A==1:
        return 0
    if len_A == len(set(A)): #roubei aqui
        return 0
    count_A_left = {}
    count_A_right = Counter(A)
    count_equi_leader = 0

    for i, a in enumerate(A):
        if a in count_A_left:
            count_A_left[a] +=1
        else:
            count_A_left[a] = 1

        if a in count_A_right:
            count_A_right[a] -= 1
        len_left = i +1
        len_right = len_A - (i + 1)
        sorted_A_right = sorted(count_A_right.items(),key=lambda x:x[1], reverse=True)
        key_max_right, value_max_right = sorted_A_right[0]
        sorted_A_left = sorted(count_A_left.items(), key=lambda x:x[1], reverse=True)
        key_max_left, value_max_left = sorted_A_left[0]
        if key_max_right==key_max_left:
            if value_max_left > len_left/2 and value_max_right > len_right/2:
                count_equi_leader +=1
    return count_equi_leader