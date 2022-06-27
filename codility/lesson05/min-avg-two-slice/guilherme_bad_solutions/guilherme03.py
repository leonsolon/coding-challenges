def solution(A): # O(N) - 100% em Correctness - 80% em Performance
    len_A = len(A)
    p = 0
    q = 1
    avg = max(A)
    minimal_avg = avg
    minimal_p = p
    # set_2 = False
    # if len(set(A))==1:
    #     return 0
    # elif len(set(A))==2:
    #     set_2 = True

    while True:
        avg = (A[p]+A[q])/2
        # print(f'i - slice:{A[p:q+1]} - avg{avg}')
        while q+1<len_A and A[q+1] <= avg:
            # if A[q+1] == avg and set_2:
            #     break
            avg = (avg * (q - p + 1) + A[q+1]) / (q - p + 2)
            q += 1
            # print(f'q - slice:{A[p:q+1]} - avg{avg}')
        while A[p] > avg and p<q-1:
            avg = (avg * (q - p + 1) - A[p]) / (q - p)
            p+=1
            # print(f'p - slice:{A[p:q+1]} - avg{avg}')
        if avg < minimal_avg:
            minimal_avg = avg
            minimal_p = p
            # print(p, q)
            # print(minimal_avg)
        p+=1
        q=p+1
        if q>=len_A:
            break
    return minimal_p

print(f'solução:{solution([-3, -5, -8, -4, -10])}')
# print(f'solução:{solution([4, 2, 2, 5, 1,5,8])}')