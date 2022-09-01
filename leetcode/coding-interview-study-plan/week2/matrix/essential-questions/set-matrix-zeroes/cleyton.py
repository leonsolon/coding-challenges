#17'

# Runtime: 127 ms, faster than 97.90% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.7 MB, less than 91.19% of Python3 online submissions for Set Matrix Zeroes.
def setZeroes(matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0
        

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
