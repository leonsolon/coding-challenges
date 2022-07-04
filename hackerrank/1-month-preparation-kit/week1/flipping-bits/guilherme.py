def flippingBits(n):
    bin_n = bin(n)[2:]

    len_bin_n = len(bin_n)
    flip_bin_n = '1'*(32-len_bin_n)

    for s in bin_n:
        if s =='0':
            flip_bin_n += '1'
        else:
            flip_bin_n += '0'

    return int(flip_bin_n, 2)

assert flippingBits(9) == 4294967286
assert flippingBits(0) == 4294967295