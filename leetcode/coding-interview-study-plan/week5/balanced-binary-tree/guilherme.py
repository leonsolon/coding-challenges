# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        global result
        result = True

        def get_height(node, height):
            global result
            if result == True:
                if node.left == None and node.right == None:
                    return height
                else:
                    left_height = right_height = height
                    if node.left != None:
                        left_height = get_height(node.left, height + 1)

                    if node.right != None:
                        right_height = get_height(node.right, height + 1)

                    if abs(right_height - left_height) > 1:
                        result = False
                    return max(left_height, right_height)

            return 0

        if root == None:
            return True

        get_height(root, 0)
        return result


