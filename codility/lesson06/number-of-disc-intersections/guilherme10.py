def solution(A):# O(N**2) - 87% em Correctness - 37% em Performance
    # write your code in Python 3.6
    starts = []
    ends =[]
    intesections = 0
    len_A = len(A)
    for i,a in enumerate(A):
        starts.append(i - a)
        ends.append(i + a)
    sorted_starts = sorted(starts)
    sorted_ends = sorted(ends)
    min_end = min(ends)
    count_starts = 0
    count_ends = 0
    print(sorted_starts)
    print(sorted_ends)
    while count_ends< len_A:
        while count_starts < len_A and sorted_starts[count_starts] <= sorted_ends[count_ends]:
            count_starts += 1
        print(sorted_ends[count_ends], count_starts)
        intesections += count_starts -1
        count_ends += 1

    return intesections
print(solution([1, 1,1]))
print(solution([1, 5, 2, 1, 4, 0]))

