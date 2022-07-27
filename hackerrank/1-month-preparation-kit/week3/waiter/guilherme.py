def getQprimes(q):
    n = 2
    count = 0;
    out = []
    while (count < q):
        isPrime = True
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            out.append(n)
            count += 1
        n += 1
    return out


def waiter(number, q):
    primes = getQprimes(q)
    primes.sort(reverse=True)
    answer = []
    for i in range(0, q):
        prime = primes.pop()
        temp_number = []
        temp_answer = []
        for n in number:
            if n % prime == 0:
                temp_answer.append(n)
            else:
                temp_number.append(n)

        number = temp_number[::-1]

        answer += temp_answer

    answer += number[::-1]
    return answer