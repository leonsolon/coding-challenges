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
        # SOLUÇÃO SEM CONSIDERAR ARVORE (filho da esquerda menor que nodo e filho da direita maior que nodo)
        dict_ancestor = {}
        def get_ancestor(node, ancestor_node):

            if ancestor_node != None and ancestor_node in dict_ancestor:
                dict_ancestor[node] = [ancestor_node] + dict_ancestor[ancestor_node]
            elif ancestor_node == None:
                dict_ancestor[node] = [None]
            else:
                dict_ancestor[node] = [ancestor_node]

            if node.left != None:
                get_ancestor(node.left, node)
            if node.right != None:
                get_ancestor(node.right, node)

        if root == None:
            return root
        get_ancestor(root, None)

        if p in dict_ancestor[q]:
            return p
        if q in dict_ancestor[p]:
            return q

        for ancestor in dict_ancestor[p]:
            if ancestor in dict_ancestor[q]:
                return ancestor