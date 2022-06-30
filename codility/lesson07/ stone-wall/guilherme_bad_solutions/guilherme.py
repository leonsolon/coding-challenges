def solution(H): # O(N) or O(N**2) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    block_list = []
    will_be_cuted = 0
    cuted_blocks = 0
    for h in H:

        while len(block_list) > (will_be_cuted - cuted_blocks) and h < block_list[-1 - (will_be_cuted - cuted_blocks)]:
            will_be_cuted += 1

        if len(block_list)==(will_be_cuted - cuted_blocks) or h != block_list[-1 - (will_be_cuted - cuted_blocks)]:
            if will_be_cuted > cuted_blocks:
                block_list = block_list[0:-(will_be_cuted-cuted_blocks)]
                cuted_blocks = will_be_cuted
            block_list.append(h)

    else:
        if will_be_cuted > cuted_blocks:
            block_list = block_list[0:-(will_be_cuted - cuted_blocks)]
            cuted_blocks = will_be_cuted
        cuted_blocks += len(block_list)
    return cuted_blocks
print(solution([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]))
print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
# print(solution([1,2,3]))
# print(solution([1,2,3,2,1]))
# print(solution([8, 8, 5, 7, 5, 8, 6, 5, 8]))