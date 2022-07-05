def diagonalDifference(arr):
    len_arr = len(arr)
    left_right_diagonal = 0
    right_left_diagonal = 0
    for i in range(0, len_arr):
        left_right_diagonal += arr[i][i]
        right_left_diagonal += arr[i][len_arr- i - 1]

    return (abs(left_right_diagonal - right_left_diagonal))

arr = [[1,2,3],
       [4,5,6],
       [9,8,9]]
assert diagonalDifference(arr) == 2
arr = [[3,2,3],
       [4,5,6],
       [9,8,9]]
assert diagonalDifference(arr) == 0
arr = [[3]]
assert diagonalDifference(arr) == 0
arr = [[3,-2],
       [4,5,]]
assert diagonalDifference(arr) == 6