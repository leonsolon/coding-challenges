def place_bombs(grid, i):
    bombs = []
    for j, string in enumerate(grid):
        for k, caracter in enumerate(string):
            if caracter == -1:
                bombs.append((j, k))

    for (j, k) in bombs:
        grid[j][k] = i
    return grid


def fix_result(grid):
    new_grid = []
    for string in grid:
        new_string = ''
        for caracter in string:
            if caracter != -1:
                new_string = new_string + 'O'
            else:
                new_string = new_string + '.'
        new_grid.append(new_string)
    return new_grid


def detonate_bombs(grid, i):
    pos = i - 3
    bombs = []
    for j, string in enumerate(grid):
        if pos in string:
            for k, s in enumerate(string):
                if s == pos:
                    bombs.append((j, k))
    for (j, k) in bombs:
        grid[j][k] = -1
        if j - 1 >= 0:
            grid[j - 1][k] = -1
        if j + 1 < len(grid):
            grid[j + 1][k] = -1
        if k - 1 >= 0:
            grid[j][k - 1] = -1
        if k + 1 < len(grid[j]):
            grid[j][k + 1] = -1
    return grid


def place_inital_bombs(grid, i):
    new_grid = []
    for string in grid:
        new_string = []
        for caracter in string:
            if caracter == 'O':
                new_string.append(i)
            else:
                new_string.append(-1)
        new_grid.append(new_string)

    return new_grid


def bomberMan(n, grid):
    grid = place_inital_bombs(grid, 0)
    # print(grid)
    for i in range(2, n + 1, 2):
        if (i - 1 - 3) >= 0:
            # print(i-1,'detonate')
            grid = detonate_bombs(grid, i - 1)
        # print(i,'place_bombs')
        grid = place_bombs(grid, i)
        # print(grid)

    if n % 2 == 1:
        grid = detonate_bombs(grid, n)
        # print(grid)

    grid = fix_result(grid)
    return grid
