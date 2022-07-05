def get_factors(N, limit):
    sqr_N = N**(1/2)
    set_factors = set()
    i=1
    while i < sqr_N or i<=limit:
        if N % i == 0:
            set_factors.add(i)
            if (N/i) <= limit:
                set_factors.add(int(N / i))
        i+=1
    return set_factors


def solution(A): # O(N * log(log(N))) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    len_A = len(A)
    if len_A <=2:
        return 0
    peak_set = set()
    for i, a in enumerate(A):
        if i > 0 and i < len_A -1 and a > A[i-1] and a > A[i+1]:
            peak_set.add(i)

    peak_list = list(peak_set)
    peak_list.sort()

    # print(peak_list)

    len_peak_list = len(peak_list)
    blocks = len(peak_list)
    if blocks == 0:
        return 0

    factors = get_factors(len_A, len_peak_list)
    factors_list = list(factors)
    factors_list.sort(reverse=True)

    for blocks in factors_list:
        i = 0
        current_block = 0
        number_elements = len_A / blocks
        peaked_blocks = 0

        while True:
            start = current_block * number_elements
            end = (current_block + 1) * number_elements
            if peak_list[i] >= start and peak_list[i] < end:
                peaked_blocks += 1
                if peaked_blocks == blocks:
                    return blocks
                current_block += 1

            i += 1

            if (i >= len_peak_list
                    or len_peak_list - i < blocks - peaked_blocks):
                break


    return 0

# assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2,4, 1, 2, 3, 4, 6, 2]) == 1
# assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
# assert solution([1]) == 0
# assert solution([1,2]) == 0
# assert solution([1,2,1]) == 1
# assert solution([1,2,3]) == 0
# assert solution([1,2,3,2]) == 1
# assert solution([1,2,1,1,2,1]) == 2
# assert solution([1,2,1,1,1,2,1]) == 1
assert solution([1,2,1,2,1,2,1,1,1]) == 1
assert solution([1,2,1,2,1,1,2,1,1]) == 3

