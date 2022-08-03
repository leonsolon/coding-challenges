from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        dist_queue = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        len_mat = len(mat)
        len_mat_row = len(mat[0])
        dist_mat = []
        for i in range(0, len_mat):
            dist_mat.append([0] * len_mat_row)

        def get_distance(i, j, dist):
            if (i, j) not in visited:
                visited.add((i, j))
                dist_mat[i][j] = dist
                for add_i, add_j in directions:
                    new_i = i + add_i
                    new_j = j + add_j
                    if (new_i, new_j) not in visited:
                        if new_i >= 0 and new_j >= 0 and new_i < len_mat and new_j < len_mat_row:
                            if mat[new_i][new_j] != 0:

                                # print((new_i, new_j), dist +1 )
                                queue.append((new_i, new_j))
                                dist_queue.append(dist + 1)

        for i, row in enumerate(mat):
            for j, cel in enumerate(row):
                if cel == 0:
                    queue.append((i, j))
                    dist_queue.append((0))

        while len(queue) > 0 :
            i, j = queue.popleft()
            dist = dist_queue.popleft()
            get_distance(i, j, dist)

        return dist_mat