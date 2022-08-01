class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify graph in-place instead.
        """
        col_to_zero = set()
        for i, col in enumerate(zip(*matrix)):
            if 0 in col:
                col_to_zero.add(i)

        row_to_zero = set()
        for i, row in enumerate(matrix):
            if 0 in row:
                row_to_zero.add(i)

        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if i in row_to_zero or j in col_to_zero:
                    matrix[i][j] = 0