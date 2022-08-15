import heapq
def cookies(k, A):
    heapq.heapify(A)
    len_A = len(A)
    count = 0
    while A[0] < k:
        if len_A <= 1:
            return -1
        least_sw = heapq.heappop(A)
        second_least_sw = heapq.heappop(A)
        heapq.heappush(A, least_sw+ 2*second_least_sw)
        count += 1
        len_A -= 1
    return count