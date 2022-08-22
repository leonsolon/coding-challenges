'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

Success
Details 
Runtime: 52 ms, faster than 38.24% of Python3 online submissions for Spiral Matrix.
Memory Usage: 13.9 MB, less than 33.85% of Python3 online submissions for Spiral Matrix.
Next challenges:
Spiral Matrix II
Spiral Matrix III
Spiral Matrix IV
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        linhas = len(matrix)
        colunas = len(matrix[0])
        elements = linhas * colunas
        output = []
        direcoes = ['r','d','l','u']
        direcao = 'r'
        while len(output) < elements:
            if direcao == 'r' and len(output) < elements:
                print(output)
                for i in matrix[0]:
                    output.append(i)
                direcao = 'd'
                matrix.pop(0)
            if direcao == 'd' and len(output) < elements:
                print(output)
                for linha in matrix:
                    output.append(linha[-1])
                    linha.pop()
                direcao = 'l'
            if direcao == 'l' and len(output) < elements:
                print(output)
                for i in matrix[-1][::-1]:
                    output.append(i)
                direcao = 'u'
                matrix.pop()
            if direcao == 'u' and len(output) < elements:
                print(output)
                for linha in matrix[::-1]:
                    output.append(linha[0])
                    linha.pop(0)
                direcao = 'r'
        return output