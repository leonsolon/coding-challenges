def solution(N): # O(sqrt(N)) - 100% em Correctness - 60% em Performance
    prime_list =[]

    original_N = N

    i=2
    add = 1
    while i <= N:
        count = 0
        prime = False
        while N % i ==0:
            if not prime:
                prime = True
            count += 1
            N = N/i
            prime_list.append(i)

        if i == 3:
            add = 2
        i += add

    factors = set([1])
    for i, prime in enumerate(prime_list):
        for factor in factors.copy():
                factors.add(factor*prime)


    factors_list = list(factors)
    factors_list.sort()
    # print(factors_list)

    len_factor_list = len(factors_list)
    if len_factor_list % 2==0:
        min_perimeter = 2*(factors_list[len_factor_list//2] + factors_list[len_factor_list//2-1])
    else:
        min_perimeter = 4 * (factors_list[len_factor_list // 2])

    # min_perimeter = float('inf')
    # for a in factors_list:
    #     perimeter = 2*(a + original_N/a)
    #     if perimeter < min_perimeter:
    #         min_perimeter = perimeter
    return int(min_perimeter)

print(solution(36))