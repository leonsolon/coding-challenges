# Time Limit Exceeded
# 48 / 71 test cases passed.
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if len(edges) == 0:
            return [0]
        if len(edges) == 1:
            return [0, 1]

        possib_roots = set()
        dict_roots = dict()
        for edge in edges:
            for el in edge:
                possib_roots.add(el)
                if el in dict_roots:
                    dict_roots[el] += 1
                else:
                    dict_roots[el] = 1

        for k, v in dict_roots.items():
            if v == 1:
                possib_roots.discard(k)

        print(possib_roots)
        possib_trees = dict()
        for root in possib_roots:
            # print('root', root)
            tree = [[root]]
            current_edges = edges.copy()
            i = 0
            while len(current_edges) > 0:
                level = []
                for node in tree[i]:
                    # print('node', node, tree[i])
                    len_current_edges = len(current_edges)
                    inv_current_edges = current_edges[::-1]
                    for j, edge in enumerate(inv_current_edges):
                        if node in edge:
                            el = set(edge)
                            el.discard(node)
                            level.append(el.pop())
                            # print('before pop', len_current_edges - j - 1, current_edges)
                            current_edges.pop(len_current_edges - j - 1)
                            # print('after pop', current_edges)
                tree.append(level)
                i += 1
            possib_trees[root] = len(tree)
            # print(root, tree)

        # print(possib_trees)
        result = []
        min_len = min(possib_trees.items(), key=lambda x: x[1])
        # print(min_len)
        for k, v in sorted(possib_trees.items(), key=lambda x: x[1]):
            if v > min_len[1]:
                break
            else:
                result.append(k)

        return result