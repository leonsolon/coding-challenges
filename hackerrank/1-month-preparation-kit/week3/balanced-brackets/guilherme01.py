def isBalanced(s):
    if len(s) == 0:
        return 'YES'
    dict_brackets = dict(zip([')', ']', '}'], ['(', '[', '{']))
    open_brackets = []
    for bracket in s:
        if bracket in '({[':
            open_brackets.append(bracket)
        else:
            if len(open_brackets) == 0:
                return 'NO'
            else:
                if dict_brackets[bracket] != open_brackets[-1]:
                    return 'NO'
                open_brackets.pop()

    if len(open_brackets) == 0:
        return 'YES'
    else:
        return 'NO'