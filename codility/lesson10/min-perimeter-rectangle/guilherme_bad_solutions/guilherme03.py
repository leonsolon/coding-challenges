def get_primes(N):
    primes = set([2])

    for i in range(2, N + 1):
        is_prime = True
        j = 2
        while j**2 <= i:
            if i % j == 0:
                is_prime = False
                break
            j +=1
        if is_prime:
            primes.add(i)
    return (primes)


def solution(N): # O(sqrt(N)) - 100% em Correctness - 60% em Performance

    prime_factors = [1]
    primes = get_primes(N)
    for prime in primes:
        while N % prime==0:
            prime_factors.append(prime)
            N = N/prime


    factors = set([1])
    for i, prime in enumerate(prime_factors):
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

    return min_perimeter

print(solution(36))