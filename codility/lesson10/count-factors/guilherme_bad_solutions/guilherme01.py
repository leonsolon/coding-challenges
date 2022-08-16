def solution(N): # O(N) - 100% em Correctness - 0% em Performance
    # write your code in Python 3.6
    count =0
    for i in range(1, N+1):
        if N % i ==0:
            count +=1
    return count