# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = []

        def get_depth(node, level):
            if node == None:
                depths.append(level)
                return
            if node.left == None and node.right == None:
                depths.append(level)
                return
            if node.left != None:
                get_depth(node.left, level + 1)
            if node.right != None:
                get_depth(node.right, level + 1)

        if root == None:
            return 0
        else:
            get_depth(root, 1)
            return max(depths)
