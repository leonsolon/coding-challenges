def mergeLists(head1, head2):
    if head1 == None and head2 != None:
        return head2
    elif head2 == None and head1 != None:
        return head1
    elif head2 == None and head1 == None:
        return head1

    current_1 = head1
    current_2 = head2
    head = None

    while current_1 != None or current_2 != None:
        if current_1 == None:
            next_el = current_2
            current_2 = current_2.next
        elif current_2 == None:
            next_el = current_1
            current_1 = current_1.next
        elif current_1.data <= current_2.data:
            next_el = current_1
            current_1 = current_1.next
        elif current_2.data < current_1.data:
            next_el = current_2
            current_2 = current_2.next

        if head == None:
            head = next_el
            current = head
        else:
            current.next = next_el
            current = current.next

    return head