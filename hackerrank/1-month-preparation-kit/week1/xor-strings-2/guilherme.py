def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        # if s[i] = t[i]:
        if s[i] == t[i]:
            # res = '0';
            res += '0';
        else:
            # res = '1';
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))