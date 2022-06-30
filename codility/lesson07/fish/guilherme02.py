def solution(A, B): # O(N) - 100% em Correctness - 75% em Performance
    # write your code in Python 3.6
    eating = False
    alive = len(A)
    fish_rigth = []
    for i, fish in enumerate(B):
        if fish == 1:
            fish_rigth.append(A[i])
            eating = True

        elif eating:
            while len(fish_rigth) > 0 and fish_rigth[-1] < A[i]:
                fish_rigth.remove(fish_rigth[-1])
                alive -= 1
            if len(fish_rigth)<=0:
                eating = False
            else:
                if fish_rigth[-1] > A[i]:
                    alive -= 1
    return alive