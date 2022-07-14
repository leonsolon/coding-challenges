def reverse(llist):
    # Write your code here
    prev_node = None
    current_node = llist

    while current_node != None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node