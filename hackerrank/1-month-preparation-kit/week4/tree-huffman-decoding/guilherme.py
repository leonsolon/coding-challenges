def decodeHuff(root, s):
    current = root
    NULL = "\x00"
    for i, el in enumerate(s):
        if el == '0':
            current = current.left
        else:
            current = current.right

        if current != None and current.data != NULL:
            print(current.data, end='')
            current = root
