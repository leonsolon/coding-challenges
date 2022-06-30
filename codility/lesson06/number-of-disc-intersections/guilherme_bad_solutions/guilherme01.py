def solution(A):# O(N**2) - 100% em Correctness - 12% em Performance
    # write your code in Python 3.6
    star_end = []
    intesections =0
    for i,a in enumerate(A):
        star_end.append((i-a,i+a))
    print(star_end)

    len_A = len(A)
    for i in range(0, len_A):
        star_i,end_i = star_end[i]
        for j in range(i+1,len_A):
            star_j,end_j = star_end[j]
            if end_i>=star_j:
                intesections += 1
                print(i,j)
                if intesections > 10000000:
                    return -1

    return intesections
print(solution([1, 1,1]))
print(solution([1, 5, 2, 1, 4, 0]))

