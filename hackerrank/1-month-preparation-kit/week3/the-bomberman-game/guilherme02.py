# falha em 10/25 testes time limit exceeded
def print_grid(bombs, rows, cols):
    grid = []
    for r in range(0, rows):
        current_row = ''
        for c in range(0, cols):
            el = '.'
            for key, bombs_set in bombs.items():
                if (r, c) in bombs_set:
                    el = 'O'
                    break
            current_row += el
        grid.append(current_row)
    return grid


def print_grid_even(rows, cols):
    grid = []
    for r in range(0, rows):
        grid.append('O' * cols)
    return grid


def bomberMan(n, grid):
    rows = len(grid)
    cols = len(grid[0])
    bombs = {}
    all_bombs = set()
    adj = [-1, 1]
    if n % 2 == 0:
        return print_grid_even(rows, cols)

    for i, row in enumerate(grid):
        for j, el in enumerate(row):
            all_bombs.add((i, j))
            if el == 'O':
                if 3 in bombs:
                    bombs[3].add((i, j))
                else:
                    bombs[3] = set()
                    bombs[3].add((i, j))

    for t in range(1, n + 1):
        if t % 2 == 0:
            bomb = all_bombs.copy()
            for k, existing_bombs in bombs.items():
                bomb.difference_update(existing_bombs)
            bombs[t + 3] = bomb
        else:
            detonating_bombs = bombs.pop(t, set())
            for key in bombs.keys():
                for (i, j) in detonating_bombs:
                    bombs[key].discard((i, j))
                    bombs[key].discard((i + 1, j))
                    bombs[key].discard((i - 1, j))
                    bombs[key].discard((i, j))
                    bombs[key].discard((i, j + 1))
                    bombs[key].discard((i, j - 1))

    return print_grid(bombs, rows, cols)