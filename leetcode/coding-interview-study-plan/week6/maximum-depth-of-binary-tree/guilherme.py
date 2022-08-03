# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def get_Depth(node, depth):
            depth_left = depth_right = depth
            if node.left != None:
                depth_left = get_Depth(node.left, depth + 1)
            if node.right != None:
                depth_right = get_Depth(node.right, depth + 1)

            return max(depth_left, depth_right)

        if root == None:
            return 0
        return get_Depth(root, 1)

