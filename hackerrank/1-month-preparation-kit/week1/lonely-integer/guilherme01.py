from collections import Counter
def lonelyinteger(a):
    # Write your code here
    count_a = Counter(a)
    lonelyinteger = min(count_a.items(), key=lambda x:x[1])
    return lonelyinteger[0]