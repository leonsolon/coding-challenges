import heapq
def cookies(k, A):
    len_A = len(A)
    if len_A<=1:
        return -1
    heapq.heapify(A)
    count = 0
    while A[0] <= k:
        if len_A<=1:
            return -1
        least_sw = heapq.heappop(A)
        second_least_sw = heapq.heappop(A)
        new_sw = least_sw + 2*second_least_sw
        heapq.heappush(A, new_sw)
        len_A -= 1
        count += 1
    return count