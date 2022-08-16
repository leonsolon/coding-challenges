class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        # for i,caract in enumerate(s):
        #     if caract != ' ':
        #         break
        # s = s[i:]
        if len(s) == 0:
            return 0
        positive = True
        if s[0] in '+-':
            if s[0] == '-':
                positive = False
            s = s[1:]

        if len(s) == 0 or not s[0].isdigit():
            return 0

        for i, caract in enumerate(s):
            # print(i, caract)
            if not caract.isdigit():
                break
        else:
            i += 1

        # print(i, caract)
        s = s[:i]
        if len(s) == 0:
            return 0
        else:
            s_int = int(s)
            print(s_int)
            if not positive:
                s_int *= -1
            s_int = max(min(2 ** 31 - 1, s_int), -2 ** 31)
        return s_int



