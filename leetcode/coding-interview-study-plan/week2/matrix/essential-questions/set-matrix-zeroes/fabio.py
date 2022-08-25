class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_cols = set()
        for i, row in enumerate(matrix):
            for j, _ in enumerate(row):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        zero_row = [0 for _ in range(len(matrix[0]))]
        for row in zero_rows:
            matrix[row] = zero_row

        for row in matrix:
            for j in zero_cols:
                row[j] = 0

# Runtime: 193 ms, faster than 57.63% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 14.7 MB, less than 54.27% of Python3 online submissions for Set Matrix Zeroes.

s = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
s.setZeroes(matrix)
print(matrix)