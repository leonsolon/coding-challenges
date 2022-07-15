def gridChallenge(grid): #100%
    # Write your code here
    if len(grid) > 0:
        len_line = len(grid[0])
    else:
        len_line = 0

    sorted_grid = []
    for line in grid:
        sorted_line = sorted(line)
        sorted_grid += sorted_line

    for i, carac in enumerate(sorted_grid):
        if i + len_line < len(sorted_grid) and carac > sorted_grid[i + len_line]:
            return 'NO'

    return 'YES'