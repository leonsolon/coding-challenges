# Runtime: 4262 ms, faster than 91.60% of Python3 online submissions for Word Search.
# Memory Usage: 215 MB, less than 12.63% of Python3 online submissions for Word Search.
from collections import Counter


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        global result
        result = False
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        len_board = len(board)
        len_board_row = len(board[0])

        def find_next_letter(x, y, remaining_word, path):
            global result
            if not result:
                if tuple(path) not in visited:
                    # print(path, remaining_word)
                    visited.add(tuple(path))
                    for dx, dy in directions:
                        new_x = x + dx
                        new_y = y + dy
                        if new_x >= 0 and new_y >= 0 and new_x < len_board and new_y < len_board_row:
                            if (new_x, new_y) not in path:
                                if board[new_x][new_y] == remaining_word[0]:
                                    if len(remaining_word) == 1:
                                        result = True
                                        return
                                    else:
                                        find_next_letter(new_x, new_y, remaining_word[1:], path + [(new_x, new_y)])

        count_letters = Counter(word)

        dict_letters = dict()
        for i, row in enumerate(board):
            for j, cel in enumerate(row):
                if cel in dict_letters:
                    dict_letters[cel].append((i, j))
                else:
                    dict_letters[cel] = [(i, j)]

        # print(dict_letters)

        for k, v in count_letters.items():
            if k not in dict_letters:
                return False
            else:
                if v > len(dict_letters[k]):
                    return False

        for i, row in enumerate(board):
            for j, cel in enumerate(row):
                if cel == word[0]:
                    if len(word) == 1:
                        return True
                    else:
                        find_next_letter(i, j, word[1:], [(i, j)])

        return result





