# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        heights = []

        def get_height(node, height):
            left_height = height
            right_height = height
            # print(node.val, height)
            if node.left == None and node.right == None:
                return max(left_height, right_height)
            if node.left != None:
                left_height = get_height(node.left, height + 1)

            if node.right != None:
                right_height = get_height(node.right, height + 1)

            # print('heights', node.val, left_height, right_height)
            heights.append((left_height - height + right_height - height))
            return max(left_height, right_height)

        if root != None:
            get_height(root, 0)
            if len(heights) == 0:
                return 0
            return max(heights)
        else:
            return 0
