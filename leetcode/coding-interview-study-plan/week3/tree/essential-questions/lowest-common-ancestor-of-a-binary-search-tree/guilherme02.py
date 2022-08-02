# Definition for a sum-of-two-integers tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        common_ancestor = []

        def get_ancestor(node):
            print(node.val, p.val, q.val)
            if (p.val > node.val) != (q.val > node.val) or p.val == node.val or q.val == node.val:
                common_ancestor.append(node)
                # print('common_ancestor',common_ancestor[0].val)
                return

            elif p.val < node.val and node.left != None:
                get_ancestor(node.left)
            elif p.val > node.val and node.right != None:
                get_ancestor(node.right)

        if root != None:
            get_ancestor(root)
        # print(common_ancestor[0].val)
        return common_ancestor[0]