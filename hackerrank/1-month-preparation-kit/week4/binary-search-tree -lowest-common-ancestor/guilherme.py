def lca(root, v1, v2):
    if v1 == root.info or v2 == root.info:
        return root
    ancestor_dict = {}
    node_stack = [[root, None]]

    while len(node_stack) > 0:

        element = node_stack.pop()

        current = element[0]
        ancestor = element[1]
        # print(current.info)
        if ancestor != None:
            info = current.info
            if info in ancestor_dict:
                ancestor_dict[info].append(ancestor)
            else:
                if ancestor.info in ancestor_dict:
                    ancestor_dict[info] = [ancestor] + ancestor_dict[ancestor.info]
                else:
                    ancestor_dict[info] = [ancestor]

        if current.left != None:
            node_stack.append([current.left, current])
            # print('left', current.left.info)
        if current.right != None:
            node_stack.append([current.right, current])
            # print('right', current.right.info)

    # print(ancestor_dict)
    for a in ancestor_dict[v1][::-1]:
        if a.info == v2:
            return a
    for a in ancestor_dict[v2][::-1]:
        if a.info == v1:
            return a

    for a in ancestor_dict[v1]:
        if a in ancestor_dict[v2]:
            return a

    for a in ancestor_dict[v2]:
        if a in ancestor_dict[v1]:
            return a