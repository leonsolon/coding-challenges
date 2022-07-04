def lonelyinteger(a=[]):
    a.sort()
    len_a = len(a)
    if len_a ==0:
        return -1
    list_range = range(0, len_a, 2)
    for i in list_range:
        if ((i+1)< len_a and a[i] != a[i+1]) or i+1 == len_a:
            return a[i]

assert lonelyinteger([1,2,3,4,3,2,1]) == 4
assert lonelyinteger([1,2,3,1,3,2,1]) == 1
assert lonelyinteger([1,1]*10000 + [2]) == 2
assert lonelyinteger([0,2,3,1,3,2,1]) == 0