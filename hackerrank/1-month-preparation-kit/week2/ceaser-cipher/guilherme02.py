def caesarCipher(s, k):
    # Write your code here

    alph = 'abcdefghijklmnopqrstuvwxyz'
    alph_upper = alph.upper()
    rotate = k % len(alph)
    alph_rotate = alph[rotate:] + alph[:rotate]
    result = ''
    for i, carct in enumerate(s):
        if carct in alph:
            idx = alph.index(carct)
            result += alph_rotate[idx]
        elif carct in alph_upper:
            idx = alph_upper.index(carct)
            result += alph_rotate[idx].upper()
        else:
            result += carct
    return result