def solution(S):
    len_S = len(S)
    if len_S == 0:
        return 1
    if len_S %2 ==1:
        return 0

    open_list = ''

    for s in S:
        if s in '{[(':
            open_list+= s
            open_list.join()
        else:
            close = s

            if len(open_list) <= 0:
                return 0
            else:
                open = open_list[-1]

            if open == '(' and close != ')':
                return 0
            elif open == '[' and close != ']':
                return 0
            elif open == '{' and close != '}':
                return 0
            else:
                open_list = open_list[0:-1]
    if len(open_list) > 0:
        return 0
    return 1