# Definition for a sum-of-two-integers tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def invertNode(node):
            if node != None:
                node.left, node.right = node.right, node.left
                invertNode(node.left)
                invertNode(node.right)
            else:
                return

        if root != None:
            invertNode(root)
        return root