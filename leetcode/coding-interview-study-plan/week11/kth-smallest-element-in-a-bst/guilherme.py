# Runtime: 80 ms, faster than 52.61% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 18.1 MB, less than 45.87% of Python3 online submissions for Kth Smallest Element in a BST.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []

        def get_most_left(node):
            path.append(node)
            while node.left != None:
                path.append(node.left)
                node = node.left

        def ordered(node):
            get_most_left(node)
            count = 0
            while count < k:
                # print(smallest)
                current_small = path.pop()
                count += 1
                if current_small.right != None:
                    get_most_left(current_small.right)

            return current_small.val

        return ordered(root)
