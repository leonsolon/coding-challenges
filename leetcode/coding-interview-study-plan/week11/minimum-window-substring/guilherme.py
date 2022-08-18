# Runtime: 1558 ms, faster than 5.02% of Python3 online submissions for Minimum Window Substring.
# Memory Usage: 14.9 MB, less than 10.91% of Python3 online submissions for Minimum Window Substring.
from collections import Counter, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        count_down_t = count_t.copy()
        set_t = set(t)
        dict_last_pos = dict()
        missing_caract = len(t)
        min_sub_string = s + 'a'
        key_start = ''
        len_s = len(s)
        for i, caract in enumerate(s):
            if caract in set_t:
                if caract not in dict_last_pos:
                    dict_last_pos[caract] = deque()
                else:
                    if len(dict_last_pos[caract]) == count_t[caract]:
                        dict_last_pos[caract].popleft()

                dict_last_pos[caract].append(i)
                # print(dict_last_pos)

                if caract in count_down_t and count_down_t[caract] > 0 and missing_caract > 0:
                    count_down_t[caract] -= 1
                    missing_caract -= 1
                    # print(missing_caract, count_down_t)

                if missing_caract == 0 and (key_start == caract or key_start == ''):
                    start = len_s
                    for k, v in dict_last_pos.items():
                        for j in v:
                            if j < start:
                                start = j
                                key_start = k

                    sub_string = s[start:i + 1]
                    # print(sub_string)
                    min_sub_string = min([sub_string, min_sub_string], key=len)

        if min_sub_string == s + 'a':
            return ''
        else:
            return min_sub_string






