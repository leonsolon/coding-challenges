class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        len_grid = len(grid)
        len_grid_row = len(grid[0])

        def visit(i, j):
            visited.add((i, j))
            for d in directions:

                new_i = i + d[0]
                new_j = j + d[1]
                if (new_i, new_j) not in visited:
                    if new_i >= 0 and new_i < len_grid and new_j >= 0 and new_j < len_grid_row:
                        if grid[new_i][new_j] != '0':
                            # print('dentro', grid[new_i][new_j], new_i, new_j)
                            visit(new_i, new_j)

        count = 0
        for i, row in enumerate(grid):
            for j, cel in enumerate(row):
                if (i, j) not in visited:
                    if grid[i][j] != '0':
                        # print(count, i, j)
                        visit(i, j)
                        count += 1
        return count