# O(N + M), 88% task score, 100% correctness, 80% performance

def solution(N, A):
    # write your code in Python 3.6
    counters = [0] * N
    max_element = 0

    for element in A:
        if element <= N:
            counters[element-1] += 1

            if counters[element-1] > max_element:
                max_element = counters[element-1]
        else:
            counters = [max_element] * N

    return counters
