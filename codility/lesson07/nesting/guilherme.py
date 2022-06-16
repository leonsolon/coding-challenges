def solution(S):
    # write your code in Python 3.6
    len_S = len(S)
    if len_S == 0:
        return 1
    elif len_S % 2 ==1:
        return 0

    count_open = 0

    for s in S:
        if s == '(':
            count_open +=1
        if s==')':
            count_open -= 1
            if count_open<0:
                return 0
    else:
        if count_open != 0:
            return 0

    return 1
