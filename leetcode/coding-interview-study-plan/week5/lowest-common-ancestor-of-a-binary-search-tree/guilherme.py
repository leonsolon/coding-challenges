# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def get_lowestCommonAncestor(node):
            if node.val == p.val or node.val == q.val:
                return node
            elif (node.val > p.val) != (node.val > q.val):
                return node
            else:
                if node.val < p.val and node.val < q.val:
                    return get_lowestCommonAncestor(node.right)
                elif node.val > p.val and node.val > q.val:
                    return get_lowestCommonAncestor(node.left)

        if root != None:
            return get_lowestCommonAncestor(root)
        else:
            return root