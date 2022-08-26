# Week 2
# Matrix
# Set Matrix Zeroes
# Runtime: 115 ms, faster than 83.52% of Python online submissions for Set Matrix Zeroes.
# Memory Usage: 14.2 MB, less than 51.06% of Python online submissions for Set Matrix Zeroes.

def setZeroes(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m =  len(matrix[0])
        zero_row = set()
        zero_col = set()
        

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)

        for i in range(n):
            for j in range(m):
                if i in zero_row or j in zero_col:
                    matrix[i][j] = 0
        return matrix # only for the assert

assert setZeroes([[1,1,1],[1,0,1],[1,1,1]]) == [[1,0,1],[0,0,0],[1,0,1]]
