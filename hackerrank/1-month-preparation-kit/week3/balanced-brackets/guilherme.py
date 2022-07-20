def isBalanced(s):
    len_s = len(s)
    if len_s == 0:
        return 'YES'
    if len_s % 2 != 0:
        return 'NO'

    open_el = []
    for i, el in enumerate(s):
        if el in '([{':
            open_el.append(el)
        else:
            if len(open_el) <= 0:
                return 'NO'
            else:
                open_caract = open_el.pop()
                if open_caract == '(' and el != ')':
                    return 'NO'
                elif open_caract == '[' and el != ']':
                    return 'NO'
                elif open_caract == '{' and el != '}':
                    return 'NO'

    if len(open_el) > 0:
        return 'NO'
    else:
        return 'YES'