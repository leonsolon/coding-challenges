def palindromeIndex(s):
    # Write your code here
    if s == s[::-1]:
        return -1
    for i, el in enumerate(s):
        j = len(s) - i - 1
        if el != s[j]:
            break
    s1 = s[:i] + s[i + 1:]
    if s1 == s1[::-1]:
        return i

    s2 = s[:j] + s[j + 1:]
    if s2 == s2[::-1]:
        return j

    return -1