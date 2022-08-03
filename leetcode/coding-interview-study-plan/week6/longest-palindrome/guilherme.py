from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_s = Counter(s)
        max_len_palindrome = 0
        for k, v in count_s.items():
            max_len_palindrome += (v // 2) * 2

        if max_len_palindrome < len(s):
            max_len_palindrome += 1

        return max_len_palindrome