"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloned_node = set()
        cloned_node_neighbors = set()
        global head_node
        head_node = None
        dict_node = {}

        def cloneNode(node):
            global head_node
            if node.val not in cloned_node:
                cloned_node.add(node.val)
                clone_node = Node(node.val)
                if head_node == None:
                    head_node = clone_node
                dict_node[node.val] = clone_node
                if head_node == None:
                    head_node = clone_node

                for neighbor in node.neighbors:
                    if neighbor.val not in cloned_node:
                        cloneNode(neighbor)

        def cloneNodeNeighbors(node):
            if node.val not in cloned_node_neighbors:
                cloned_node_neighbors.add(node.val)
                clone_node = dict_node[node.val]
                if node.neighbors != None:
                    clone_node.neighbors = []
                for neighbor in node.neighbors:
                    clone_node.neighbors.append(dict_node[neighbor.val])
                    if neighbor.val not in cloned_node_neighbors:
                        cloneNodeNeighbors(neighbor)

        if node != None:
            cloneNode(node)
            cloneNodeNeighbors(node)
            return head_node
        else:
            return node
