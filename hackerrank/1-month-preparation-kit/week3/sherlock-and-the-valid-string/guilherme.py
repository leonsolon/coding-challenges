from collections import Counter

def isValid(s):
    count_s = Counter(s)
    min_count = min(count_s.items(), key=lambda x: x[1])
    max_count = max(count_s.items(), key=lambda x: x[1])
    if min_count[1] == max_count[1]:
        return 'YES'
    else:
        if min_count[1] == 1:
            count_s_exclude_min = count_s.copy()
            count_s_exclude_min.pop(min_count[0])
            new_min_count = min(count_s_exclude_min.items(), key=lambda x: x[1])
            new_max_count = max(count_s_exclude_min.items(), key=lambda x: x[1])
            if new_min_count[1] == new_max_count[1]:
                return 'YES'

        error = 0
        for key, value in count_s.items():
            if value > min_count[1]:
                error += value - min_count[1]
                if error > 1:
                    return 'NO'

        return 'YES'