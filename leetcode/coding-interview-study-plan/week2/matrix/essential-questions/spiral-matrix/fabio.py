class Solution:
    def spiralOrder(self, matrix):
        from itertools import cycle
        directions = cycle([(0,1), (1,0), (0,-1), (-1,0)])
        len_row = len(matrix)
        len_col = len(matrix[0])
        row = 0
        col = 0
        result = []
        traversed = set()
        step_row, step_col = next(directions)
                
        for i in range(len_row * len_col):
            result.append(matrix[row][col])
            traversed.add((row, col))
            if (row + step_row in [len_row, -1]) or (col + step_col in [len_col, -1]) or ((row + step_row, col + step_col) in traversed):
                step_row, step_col = next(directions)
            row += step_row
            col += step_col
            
        return result

# Runtime: 70 ms, faster than 5.35% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14 MB, less than 33.85% of Python3 online submissions for Spiral Matrix.

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))