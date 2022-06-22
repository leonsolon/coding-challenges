from collections import Counter
def solution(A): # O(N) - 100% em Correctness - 100% em Performance - sem roubar - guilherme07
    # write your code in Python 3.6
    len_A = len(A)
    if len_A==1:
        return 0
    # if len_A == len(set(A)): #roubei aqui
    #     return 0
    count_A = Counter(A)
    count_A_left = {}
    count_A_right = count_A.copy()
    count_equi_leader = 0

    for i, a in enumerate(A):

        len_left = i + 1
        len_right = len_A - (i + 1)
        changed_left  = False
        changed_right = False
        if a in count_A_left:
            if count_A[a] > len_left / 2:
                count_A_left[a] +=1
                changed_left = True
            else:
                count_A_left.pop(a)
        else:
            if count_A[a] > len_left/2:
                count_A_left[a] = 1


        if a in count_A_right:
                count_A_right[a] -= 1
                changed_right = True

        if len(count_A_left)< len(count_A_right):
            if changed_left :
                count_A_left = dict(sorted(count_A_left.items(), key=lambda x: x[1], reverse=True))
            sorted_1 = count_A_left
            len_sorted_1 = len_left
            dict2 = count_A_right
            len_sorted_2 = len_right
        else:
            if changed_right:
                count_A_right = dict(sorted(count_A_right.items(), key=lambda x: x[1], reverse=True))
            sorted_1 = count_A_right
            len_sorted_1 = len_right
            dict2 = count_A_left
            len_sorted_2 = len_left

        key_max_1 = list(sorted_1)[0]
        value_max_1 = sorted_1[key_max_1]
        if value_max_1 > len_sorted_1 / 2 and key_max_1 in dict2:
            value_2 = dict2[key_max_1]
            if value_2 > len_sorted_2 / 2:
                    count_equi_leader += 1

    return count_equi_leader

assert solution([1,2,3,4,5,6,7,8]) ==0
assert solution([4, 3, 4, 4, 4, 2]) == 2
assert solution([4]) == 0
assert solution([3,4]) == 0
assert solution([3,3]) == 1

assert solution([4, 4, 2, 5, 3, 4, 4, 4]) ==3
assert solution([4, 3, 4, 4, 4, 2]) == 2
assert solution([1, 2, 3, 4, 5]) == 0