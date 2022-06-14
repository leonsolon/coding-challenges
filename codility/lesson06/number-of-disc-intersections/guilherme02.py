def solution(A):# O(N**2) - 87% em Correctness - 37% em Performance
    # write your code in Python 3.6
    star_end = []
    intesections =0
    len_A = len(A)
    if len_A==0:
        return 0
    starts = [0]*len_A

    min_start = float('inf')
    max_start = -float('inf')
    for i,a in enumerate(A):
        start = i - a
        end = i + a
        star_end.append((start,end))
        if start < min_start:
            min_start = start
        if start > max_start:
            max_start = start
    starts = [0] * (max_start-min_start + 1)
    # print(star_end)


    for start, end in star_end:
        starts[start-min_start] +=1
    # print(f'min_start: {min_start} - max_start: {max_start} - starts: {starts}')

    for i in range(0, len_A):
        star_i,end_i = star_end[i]
        # print(f'end_i: {end_i} - starts_slice: {starts[0:end_i-min_start+1]}')
        # print(starts[0:end_i-min_start+1])
        intesections += sum(starts[0:end_i-min_start+1])-1
        starts[star_i - min_start] -= 1
        # print(f'intesections: {intesections}')
        if intesections > 10000000:
            return -1

    return intesections
print(solution([1, 1,1]))
print(solution([1, 5, 2, 1, 4, 0]))

