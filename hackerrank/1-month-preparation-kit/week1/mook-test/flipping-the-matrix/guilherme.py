def flippingMatrix(matrix):
    # Write your code here
    len_matrix = len(matrix)
    n = int(len_matrix/2)
    sum_values = 0
    for i in range(0,n):
        for j in range(0,n):
            sum_values += max(matrix[i][j], matrix[i][len_matrix-1-j], matrix[len_matrix-1-i][j], matrix[len_matrix-1-i][len_matrix-1-j])
    return sum_values