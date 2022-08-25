# Runtime: 229 ms, faster than 47.64% of Python3 online submissions for Find All Anagrams in a String.
# Memory Usage: 15.2 MB, less than 80.92% of Python3 online submissions for Find All Anagrams in a String.
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count_p = Counter(p)
        len_p = len(p)
        len_s = len(s)

        def is_in(big_dict, small_dict):
            for k, v in small_dict.items():
                if k not in big_dict:
                    return False
                elif big_dict[k] < v:
                    return False

            return True

        if not is_in(Counter(s), count_p):
            return []

        result = []
        count_slice_s = dict()
        for i, caract in enumerate(s):
            if caract in count_slice_s:
                count_slice_s[caract] += 1
            else:
                count_slice_s[caract] = 1
            if i >= len_p:
                caract_remove = s[i - len_p]
                if caract_remove in count_slice_s:
                    count_slice_s[caract_remove] -= 1

            if is_in(count_slice_s, count_p):
                result.append(i - len_p + 1)

        return result

