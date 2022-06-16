def solution(A, B): # O(N) - 100% em Correctness - 100% em Performance
    # write your code in Python 3.6
    eating = False
    alive = len(A)
    fish_rigth = []
    for i, fish in enumerate(B):
        if fish == 1:
            fish_rigth.append(A[i])
            eating = True

        elif eating:
            count_eated = 0
            while len(fish_rigth) > count_eated and fish_rigth[-1-count_eated] < A[i]:
                count_eated += 1
            if count_eated >0:
                fish_rigth = fish_rigth[0:-count_eated]

                alive -= count_eated

            if len(fish_rigth)<=0:
                eating = False
            else:
                if fish_rigth[-1] > A[i]:
                    alive -= 1
    return alive

print(solution([8, 3, 6, 7, 5], [1, 0, 1, 0, 0]))

# print(solution([8, 3, 6, 7, 5], [1, 0, 1, 0, 0]))
# print(solution([7, 3, 6, 1, 5], [1, 0, 0, 0, 0]))
# print(solution([4, 3, 6, 1, 5], [1, 1, 1, 1, 1]))
# print(solution([4, 3, 6, 1, 5], [0, 0, 0, 0, 0]))
# print(solution([4, 3, 6, 1, 5], [0, 1, 0, 0, 0]))
print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))