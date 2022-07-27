def mark_distance(grid_list, posX, posY, step):
    step += 1
    len_gridX = len(grid)
    len_gridY = len(grid[0])

    for i in range(posX - 1, -1, -1):
        if grid_list[i][posY] == 'X':
            break
        elif grid_list[i][posY] == '.':
            grid_list[i][posY] = step
    for i in range(posX + 1, len_gridX):
        if grid_list[i][posY] == 'X':
            break
        elif grid_list[i][posY] == '.':
            grid_list[i][posY] = step

    for i in range(posY - 1, -1, -1):
        if grid_list[posX][i] == 'X':
            break
        elif grid_list[posX][i] == '.':
            grid_list[posX][i] = step
    for i in range(posY + 1, len_gridY):
        if grid_list[posX][i] == 'X':
            break
        elif grid_list[posX][i] == '.':
            grid_list[posX][i] = step

    return grid_list


def minimumMoves(grid, startX, startY, goalX, goalY):
    grid_list = []
    for row in grid:
        col_list = []
        for col in row:
            col_list.append(col)
        grid_list.append(col_list)

    grid_list[startX][startY] = 0
    # print(grid_list)

    step = 0
    while True:

        for posX, row in enumerate(grid_list.copy()):
            for posY, col in enumerate(row):
                if col == step:
                    grid_list = mark_distance(grid_list, posX, posY, step)
                    if grid_list[goalX][goalY] != '.':
                        return grid_list[goalX][goalY]

        step += 1
        # print(grid_list)

    return grid_list[goalX][goalY]