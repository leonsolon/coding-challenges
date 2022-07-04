def plusMinus(arr):
    # Write your code here
    len_arr = len(arr)
    count_zero = 0
    count_positve = 0
    count_negative = 0
    if len_arr == 0:
        print(f'{count_positve:6f}')
        print(f'{count_negative:6f}')
        print(f'{count_zero:6f}')
        return

    for i, a in enumerate(arr):
        if a == 0:
            count_zero += 1
        elif a > 0:
            count_positve += 1
        elif a < 0:
            count_negative += 1
    print(f'{count_positve / len_arr:6f}')
    print(f'{count_negative / len_arr:6f}')
    print(f'{count_zero / len_arr:6f}')

plusMinus([])