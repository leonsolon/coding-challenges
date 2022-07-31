class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        visited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        len_img = len(image)
        len_img_row = len(image[0])
        initial_collor = image[sr][sc]

        def change_color(i, j):
            visited.add((i, j))
            image[i][j] = color
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if new_i >= 0 and new_j >= 0 and new_i < len_img and new_j < len_img_row:
                    if (new_i, new_j) not in visited and image[new_i][new_j] == initial_collor:
                        # print(new_i, new_j)
                        change_color(new_i, new_j)

        change_color(sr, sc)
        return image