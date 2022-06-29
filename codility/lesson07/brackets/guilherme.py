# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    len_S = len(S)
    if len_S < 1:
        return 1
    if len_S % 2 != 0:
        return 0

    open_carac = ''

    for i, s in enumerate(S):
        if s in '([{':
            open_carac += s
        else:
            if len(open_carac) <= 0:
                return 0
            else:
                if s == ')' and open_carac[-1] != '(':
                    return 0
                if s == ']' and open_carac[-1] != '[':
                    return 0
                if s == '}' and open_carac[-1] != '{':
                    return 0
                open_carac = open_carac[:-1]

    if len(open_carac) > 0:
        return 0
    else:
        return 1