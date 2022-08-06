def birthday(s, d, m):
    # Write your code here
    current_sum = 0
    count = 0
    for i, el in enumerate(s):
        if i < m:
            current_sum += el
            if i == m - 1 and current_sum == d:
                count += 1
        else:
            current_sum += el - s[i - m]
            if current_sum == d:
                count += 1

    return count