def sumXor(n):
    if n == 0:
        return 1
    else:
        bin_n = bin(n)[2:]
        zeros_in_bin_n = bin_n.count('0')
        return 2**zeros_in_bin_n
