class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        if len(s) == 1 or s == s[::-1]:
            return s

        dict_pos = {}
        max_len = -float('inf')
        max_palindrome = ''
        for i, caract in enumerate(s):
            if caract in dict_pos:
                dict_pos[caract].append(i)
            else:
                dict_pos[caract] = [i]
        # print(dict_pos)

        for i, caract in enumerate(s):
            for j in dict_pos[caract][::-1]:
                if i > j:
                    break
                else:
                    pal = s[i:j + 1]
                    if pal == pal[::-1]:
                        if j - i + 1 > max_len:
                            max_len = max(max_len, j - i + 1)
                            max_palindrome = pal

        return max_palindrome



