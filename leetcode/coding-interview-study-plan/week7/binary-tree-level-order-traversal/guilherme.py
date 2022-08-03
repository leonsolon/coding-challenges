# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict_level = {}

        def get_level(node, level):
            if level in dict_level:
                dict_level[level].append(node.val)
            else:
                dict_level[level] = [node.val]
            dict_level[level]
            if node.left != None:
                get_level(node.left, level + 1)
            if node.right != None:
                get_level(node.right, level + 1)

        if root == None:
            return []
        else:
            get_level(root, 0)
            result = []
            for k, v in dict_level.items():
                result.append(v)
            return result


