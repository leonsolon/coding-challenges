class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = ''
        len_sub_s = 0
        max_len = 0
        for i, el in enumerate(s):
            if el not in sub_s:
                sub_s += el
                len_sub_s += 1
            else:
                idx = sub_s.index(el)
                sub_s = sub_s[idx + 1:] + el
                len_sub_s -= idx
            max_len = max(max_len, len_sub_s)

        return max_len
