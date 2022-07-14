def gridChallenge(grid): #100%
    for i, string in enumerate(grid.copy()):
        grid[i] = sorted(string)

    # print(grid)

    for j in range(0, len(grid[0])):
        for i in range(1, len(grid)):
            if grid[i - 1][j] <= grid[i][j]:
                continue
            else:
                return 'NO'
    return 'YES'