# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B): # O(N) - 100% em Correctness - 100% em Performance
    i = 0
    alive_fish = 0
    while i < len(B) and B[i] == 0:
        i += 1
        alive_fish += 1

    j = len(B) - 1
    while j >= 0 and B[j] == 1:
        j -= 1
        alive_fish += 1

    A = A[i:j + 1]
    B = B[i:j + 1]

    ones = []
    for i, (a, b) in enumerate(zip(A, B)):
        if b == 1:
            ones.append(a)
        else:
            if len(ones) > 0 and ones[-1] > a:
                continue
            else:
                while len(ones) > 0 and a > ones[-1]:
                    ones.pop()
                if len(ones) == 0:
                    alive_fish += 1

    alive_fish += len(ones)
    return alive_fish