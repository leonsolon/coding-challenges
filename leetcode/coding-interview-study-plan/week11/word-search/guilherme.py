# Runtime: 1814 ms, faster than 96.71% of Python3 online submissions for Word Search.
# Memory Usage: 14.1 MB, less than 12.63% of Python3 online submissions for Word Search.
from collections import Counter


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        len_board = len(board)
        len_board_row = len(board[0])

        def is_possible(board, word):
            dict_letters = dict()
            for i, row in enumerate(board):
                for j, cel in enumerate(row):
                    if cel in dict_letters:
                        dict_letters[cel].append((i, j))
                    else:
                        dict_letters[cel] = [(i, j)]

            # print(dict_letters)
            count_letters = Counter(word)
            for k, v in count_letters.items():
                if k not in dict_letters:
                    return False
                else:
                    if v > len(dict_letters[k]):
                        return False

            return True

        def find_next_letter(x, y, remaining_word, path):

            if (x, y) not in path:
                path.add((x, y))
                # print(path, remaining_word)
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if new_x >= 0 and new_y >= 0 and new_x < len_board and new_y < len_board_row:
                        if (new_x, new_y) not in path:
                            if board[new_x][new_y] == remaining_word[0]:
                                if len(remaining_word) == 1:
                                    return True
                                else:
                                    if find_next_letter(new_x, new_y, remaining_word[1:], path.copy()):
                                        return True

        if is_possible(board, word):
            for i, row in enumerate(board):
                for j, cel in enumerate(row):
                    if cel == word[0]:
                        if len(word) == 1:
                            return True
                        else:
                            if find_next_letter(i, j, word[1:], set()):
                                return True

        return False





