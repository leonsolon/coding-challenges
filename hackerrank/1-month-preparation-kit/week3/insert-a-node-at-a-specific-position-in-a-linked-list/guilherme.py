def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = llist

    current_node = llist

    if position == 0:
        first_node = new_node
    else:
        first_node = current_node

    i = 0
    while i < position - 1:
        print(current_node.data)
        current_node = current_node.next
        i += 1

    next_node = current_node.next
    current_node.next = new_node
    new_node.next = next_node

    return first_node