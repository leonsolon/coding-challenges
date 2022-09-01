#60'



from typing import List

# Runtime: 37 ms, faster than 81.87% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 13.9 MB, less than 33.85% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        def helper(mat, res):
            m = len(mat) # number of of rows
            n = len(mat[0]) # number of columns

            if m == 1: #Only one row --> return row
                res += mat[0]
                return
            if n == 1: #Only one column --> return column
                res += [mat[i][0] for i in range(m)]
                return

            res += [mat[0][j] for j in range(n)] #left --> right
            res += [mat[i][-1] for i in range(1, m)] #top --> down
            res += [mat[-1][-j-1] for j in range(1, n)] #left --> right
            res += [mat[-i-1][0] for i in range (1, m -1)] #bottom --> up

            if n - 2 > 0 and m - 2 > 0: #Get the 'inner' matrix
                aux = [row[1:-1] for row in mat[1:-1]]
                helper(aux, res)
        
        res = []
        helper(matrix, res)
        return res
    

a = Solution()



a.spiralOrder([[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]])
a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

a.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])

a.spiralOrder([[1,2],[3,4]])
a.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
