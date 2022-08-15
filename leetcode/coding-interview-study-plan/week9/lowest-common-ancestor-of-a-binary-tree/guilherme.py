# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

dict_ancestor = {}


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def Ancestor(node, ancestor):
            if ancestor == None:
                dict_ancestor[node.val] = [node]
            else:
                dict_ancestor[node.val] = [node] + dict_ancestor[ancestor.val]

            if node.left != None:
                Ancestor(node.left, node)
            if node.right != None:
                Ancestor(node.right, node)

        # print(dict_ancestor)
        if root == None:
            return root
        Ancestor(root, None)

        for a in dict_ancestor[p.val]:
            if a in dict_ancestor[q.val]:
                return a