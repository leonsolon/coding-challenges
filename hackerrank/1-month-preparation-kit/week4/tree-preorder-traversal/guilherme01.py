def preOrder(root):
    # Write your code here
    print(get_s(root))


def get_s(root, s=''):
    if len(s) > 0:
        s += " "
    s += str(root.info)
    if root.left != None:
        s = get_s(root.left, s)
    if root.right != None:
        s = get_s(root.right, s)
    return s