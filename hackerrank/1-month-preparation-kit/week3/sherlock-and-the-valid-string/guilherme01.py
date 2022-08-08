from collections import Counter


def isValid(s):
    count_s = Counter(s)
    min_count_s = min(count_s.items(), key=lambda x: x[1])
    max_count_s = max(count_s.items(), key=lambda x: x[1])
    if min_count_s[1] == max_count_s[1]:
        return 'YES'
    else:
        count_s_try1 = count_s.copy()
        count_s_try1[max_count_s[0]] += -1
        min_count_s_try1 = min(count_s_try1.items(), key=lambda x: x[1])
        max_count_s_try1 = max(count_s_try1.items(), key=lambda x: x[1])
        if min_count_s_try1[1] == max_count_s_try1[1]:
            return 'YES'
        else:
            if min_count_s[1] == 1:
                del (count_s[min_count_s[0]])
                min_count_s = min(count_s.items(), key=lambda x: x[1])
                max_count_s = max(count_s.items(), key=lambda x: x[1])
                if min_count_s[1] == max_count_s[1]:
                    return 'YES'

    return 'NO'