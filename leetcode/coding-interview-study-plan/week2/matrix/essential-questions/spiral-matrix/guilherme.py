class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        i = 0
        mode = [1, 2, 3, 4]
        while len(matrix) > 0:
            if mode[i % len(mode)] == 1 or mode[i % len(mode)] == 4:
                next_line = matrix.pop(0)
            else:
                next_line = matrix.pop()

            if mode[i % len(mode)] == 3 or mode[i % len(mode)] == 4:
                next_line = next_line[::-1]

            output += next_line
            matrix = list(zip(*matrix))
            i += 1
        return output