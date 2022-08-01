from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        visited = set()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        len_mat = len(mat)
        len_mat_row = len(mat[0])
        mat_dist = []
        queue = deque()
        dist_queue = deque()
        for i in range(0, len_mat):
            mat_dist.append([0] * len_mat_row)

        # print(mat_dist)

        def visit(i, j, dist):
            # print(i,j, dist)
            visited.add((i, j))
            mat_dist[i][j] = dist
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if new_i >= 0 and new_j >= 0 and new_i < len_mat and new_j < len_mat_row:
                    if (new_i, new_j) not in visited:
                        if mat[new_i][new_j] != 0:
                            queue.append((new_i, new_j))
                            dist_queue.append(dist + 1)

        for i, row in enumerate(mat):
            for j, cel in enumerate(row):
                if cel == 0:
                    queue.append((i, j))
                    dist_queue.append(0)
        # print(tree)
        while len(queue) > 0:
            (i, j) = queue.popleft()
            dist = dist_queue.popleft()
            if (i, j) not in visited:
                visit(i, j, dist)

        return mat_dist