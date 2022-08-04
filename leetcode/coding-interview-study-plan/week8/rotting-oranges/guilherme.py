from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        len_grid = len(grid)
        len_grid_row = len(grid[0])
        global tempo
        tempo = 0

        def rotten(i, j, t):
            global tempo
            if (i, j) not in visited:
                tempo = t
                visited.add((i, j))
                grid[i][j] = 2
                for add_i, add_j in directions:
                    new_i = i + add_i
                    new_j = j + add_j

                    if new_i >= 0 and new_j >= 0 and new_i < len_grid and new_j < len_grid_row:
                        if (new_i, new_j) not in visited:
                            if grid[new_i][new_j] == 1:
                                queue.append((new_i, new_j, t + 1))

        for i, row in enumerate(grid):
            for j, cel in enumerate(row):
                if cel == 2:
                    queue.append((i, j, 0))

        while len(queue) > 0:
            i, j, t = queue.popleft()
            rotten(i, j, t)

        for i, row in enumerate(grid):
            for j, cel in enumerate(row):
                if cel == 1:
                    return -1

        return tempo