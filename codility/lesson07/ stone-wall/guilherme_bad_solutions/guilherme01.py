def solution(H): # O(N) or O(N**2) - 100% em Correctness - 88% em Performance
    # write your code in Python 3.6
    last_h =0
    block_list = []
    num_blocks = 0
    for h in H:
        cuted_blocks = 0
        while len(block_list) > cuted_blocks and h < block_list[-1 - cuted_blocks]:
            cuted_blocks += 1
        if cuted_blocks > 0:
            block_list = block_list[0:-cuted_blocks]
            num_blocks += cuted_blocks

        if len(block_list)==0 or h !=  block_list[-1]:
            block_list.append(h)

    else:
        num_blocks += len(block_list)
    return num_blocks
print(solution([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]))
# print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
# print(solution([1,2,3]))
# print(solution([1,2,3,2,1]))
# print(solution([8, 8, 5, 7, 5, 8, 6, 5, 8]))