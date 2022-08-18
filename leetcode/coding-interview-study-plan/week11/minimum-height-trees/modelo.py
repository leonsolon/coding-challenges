# Runtime: 1124 ms, faster than 13.87% of Python3 online submissions for Minimum Height Trees.
# Memory Usage: 25.4 MB, less than 41.64% of Python3 online submissions for Minimum Height Trees.
from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        G = defaultdict(set)
        for v,w in edges:
            G[v].add(w)
            G[w].add(v)
        leaves = [v for v in G if len(G[v]) == 1]
        print(G, leaves)
        while n > 2:
            nxt_leaves = []
            for v in leaves:
                w = G[v].pop()
                n -= 1
                G[w].remove(v)
                if len(G[w]) == 1:
                    nxt_leaves.append(w)
                print(v, G, nxt_leaves)
            leaves = nxt_leaves
        return leaves