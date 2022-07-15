def reverse(llist):
    current_node = llist
    while True:
        next_node = current_node.next
        prev_node = current_node.prev
        current_node.next = prev_node
        current_node.prev = next_node
        if next_node == None:
            break
        current_node = next_node
    return current_node