'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

Success
Details 
Runtime: 197 ms, faster than 55.28% of Python3 online submissions for Set Matrix Zeroes.
Memory Usage: 14.6 MB, less than 91.19% of Python3 online submissions for Set Matrix Zeroes.
Next challenges:
Game of Life
Number of Laser Beams in a Bank
Minimum Operations to Remove Adjacent Ones in Matrix
Remove All Ones With Row and Column Flips II
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        dictzeros = dict()
        for line, arr in enumerate(matrix):
            if 0 in arr:
                dictzeros[line] = []
                for idx, el in enumerate(arr):
                    if el == 0:
                        dictzeros[line].append(idx)
        #print(dictzeros)
        colstozero = []
        for key in dictzeros:
            colstozero += dictzeros[key]
        colstozero = set(colstozero)
        for line, arr in enumerate(matrix):
            if line in dictzeros.keys():
                matrix[line] = [0]*len(arr)
                continue
            for idx, el in enumerate(arr):
                if idx in colstozero:
                    matrix[line][idx] = 0