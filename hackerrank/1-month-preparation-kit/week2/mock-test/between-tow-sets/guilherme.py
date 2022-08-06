def getTotalX(a, b):
    # Write your code here
    max_a = max(a)
    min_b = min(b)

    multiplus_a = set(range(max_a, min_b + 1))
    for el in a:
        for m in range(max_a, min_b + 1):
            if m % el != 0:
                multiplus_a.discard(m)

    multiplus_a_list = list(multiplus_a)
    for m in multiplus_a_list:
        for el in b:
            if el % m != 0:
                multiplus_a.discard(m)
                break

    return len(multiplus_a)