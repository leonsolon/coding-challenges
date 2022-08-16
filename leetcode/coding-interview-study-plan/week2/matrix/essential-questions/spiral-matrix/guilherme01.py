class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        steps = [(0, 1), (-1, 1), (-1, -1), (0, -1)]

        i = 0
        while len(matrix) > 0:
            # print(matrix, steps[i][0])
            line = matrix[steps[i][0]]
            result += line[::steps[i][1]]
            matrix.pop(steps[i][0])
            matrix = list(zip(*matrix))

            i += 1
            i = i % len(steps)

        return result
