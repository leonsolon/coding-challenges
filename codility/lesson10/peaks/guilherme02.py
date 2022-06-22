def solution(A): # ??? - 100% em Correctness - 40% em Performance
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



    while True:
        while len_A % blocks != 0:
            blocks -= 1
            if blocks <= 1:
                return blocks

        i = 0
        current_block = 0
        number_elements = len_A / blocks
        peaked_blocks = set()

        while True:
            start = current_block*number_elements
            end = (current_block+1)*number_elements
            if peak_list[i] >= start and peak_list[i] < end:
                peaked_blocks.add(current_block)
                if len(peaked_blocks) == blocks:
                    return blocks
                current_block += 1

            i +=1

            if i >= len_peak_list:
                blocks -= 1
                if blocks<= 0:
                    return 0
                i =0
                current_block = 0
                peaked_blocks = set()

    return 0

assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2,4, 1, 2, 3, 4, 6, 2]) == 1
assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
assert solution([1]) == 0
assert solution([1,2]) == 0
assert solution([1,2,1]) == 1
assert solution([1,2,3]) == 0
assert solution([1,2,3,2]) == 1
assert solution([1,2,1,1,2,1]) == 2
assert solution([1,2,1,1,1,2,1]) == 1
assert solution([1,2,1,2,1,2,1,1,1]) == 2

