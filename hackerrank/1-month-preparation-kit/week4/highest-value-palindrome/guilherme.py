def highestValuePalindrome(s, n, k):
    # Write your code here
    if k >= n:
        return '9' * n
    s = list(s)
    middle = n // 2

    error_pal = {}
    for i in range(0, middle):
        if s[i] != s[n - i - 1]:
            error_pal[i] = max(s[i], s[n - i - 1])

    len_error_pal = len(error_pal)
    if k < len_error_pal:
        return '-1'

    for i in range(0, middle):
        if k > len_error_pal and k >= 2:
            if s[i] != s[n - i - 1]:
                len_error_pal -= 1
            if s[i] != '9':
                s[i] = '9'
                k -= 1
            if s[n - i - 1] != '9':
                s[n - i - 1] = '9'
                k -= 1
        elif k == len_error_pal:
            if s[i] > s[n - i - 1]:
                s[n - i - 1] = s[i]
                k -= 1
                len_error_pal -= 1
            elif s[i] < s[n - i - 1]:
                s[i] = s[n - i - 1]
                k -= 1
                len_error_pal -= 1

    if k == 1:
        if len(s) % 2 == 1:
            s[middle] = 9

    new_s = ''
    for el in s:
        new_s += str(el)

    return new_s