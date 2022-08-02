import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''
        alphabet = string.ascii_lowercase + string.digits
        for el in s:
            if el in alphabet:
                new_s += el

        if new_s == new_s[::-1]:
            return True
        else:
            return False
