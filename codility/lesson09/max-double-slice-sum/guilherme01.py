def solution(A=[]): # O(N) - 100% em Correctness - 85% em Performance
    # large_sequence
    # many the same small sequences, length = ~100,000 ✘WRONG ANSWER
    # got 11 expected 20 (Não consegui detectar a causa)
    len_A = len(A)
    if len(A) <=3:
        return 0
    if max(A) <= 0:
        return 0

    sliced = False
    start = 1
    while A[start] <= 0 and start < len_A:
        start += 1
    if start == len_A -1:
        return 0

    end = len_A-2
    while A[end] <= 0 and end >= start:
        end -= 1
    if start > end:
        return 0

    if len_A - (end - start + 1) >=3:
        sliced = True

    curent_sum = 0
    min_a = float('inf')
    max_sum = -float('inf')
    min_a_sliced = float('inf')

    for i,a in enumerate(A[start:end+1]):

        if a < min_a:
            min_a = a
            if sliced:
                min_a_sliced = min(0, min_a)
            else:
                min_a_sliced = min_a

        if i == 0:
            curent_sum = a
        elif (curent_sum < 0 and a > curent_sum) :
            curent_sum = a
            min_a = a
            min_a_sliced = min(0, min_a)
            sliced = True
        else:
            curent_sum = curent_sum + a

        curent_slice_sum = curent_sum - min_a_sliced


        if max_sum < curent_slice_sum:
            max_sum = curent_slice_sum

    return max_sum

print(solution( [ 2, 3, 5,-10]*50)) # = 20
print(solution( [1, 2, 3, 4,5,-15]*50)) # = 30
print(solution( [ 2, 3,-3,-2, 4,5,-15]*50))
print(solution( [6, 1, 5, 6, 4, 2, 9, 4]))
print(solution( [0, 10, -5, -2, 0]))
print(solution( [-8, 10, 20, -5, -7, -4]))
print(solution([3,2,6,-8,4,-8,5,-1,2]))
print(solution([3,2,6,-8,2,-8,5,-1,2]))
print(solution([3,2,6,-1,4,5,-1,2]))
print(solution([1,2,3]))
print(solution([1,2,3,4]))
print(solution([0, 10, -5, -2, 0]))
print(solution([5, 17, 0, 3]))


print(solution([-10,-10,8,-1,3,-20,7,-1,4,-10,-10,-10,-10,8,-1,3,-20,7,-1,4,-10,-10,-10,-10,8,-1,3,-20,7,-1,4,-10,-10,-10,-10])) # = 20