# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        global dict_level
        dict_level = {}

        def rightSideView_rec(node, level):
            if level in dict_level:
                dict_level[level].append(node.val)
            else:
                dict_level[level] = [node.val]

            if node.left != None:
                rightSideView_rec(node.left, level + 1)
            if node.right != None:
                rightSideView_rec(node.right, level + 1)

        result = []
        if root != None:
            rightSideView_rec(root, 0)
            # print(dict_level)
            for level, values in dict_level.items():
                result.append(values[-1])

        return result



