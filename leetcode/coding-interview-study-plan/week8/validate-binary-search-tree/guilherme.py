# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        global valid
        valid = True

        def isValidNode(node, min_limit, max_limit):
            global valid
            # print(valid, node.val, min_limit, max_limit)
            if valid:
                if node.left != None:
                    if node.left.val < node.val and node.left.val > min_limit and node.left.val < max_limit:
                        isValidNode(node.left, min_limit, node.val)
                    else:
                        valid = False

                if node.right != None:
                    if node.right.val > node.val and node.right.val > min_limit and node.right.val < max_limit:
                        isValidNode(node.right, node.val, max_limit)
                    else:
                        valid = False

        if root != None:
            isValidNode(root, -float('inf'), float('inf'))

        return valid



