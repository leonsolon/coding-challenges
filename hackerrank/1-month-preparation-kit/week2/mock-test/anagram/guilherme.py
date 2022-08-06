from collections import Counter
def anagram(s):
    # Write your code here
    len_s = len(s)
    if len_s % 2 == 1:
        return -1
    s1 = s[:len_s//2]
    count_s1 = Counter(s1)
    s2 = s[len_s//2:]
    count_s2 = Counter(s2)
    sum_diff = 0
    for el in set(s):
        sum_diff += abs(count_s1[el] - count_s2[el])