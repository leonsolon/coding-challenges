def mergeLists(head1, head2):
    if head1 == None:
        return head2

    if head2 == None:
        return head1

    current1 = head1
    current2 = head2
    current_new = head_new = None
    while current1 != None or current2 != None:
        if (current2 == None and current1 != None) or (
                current2 != None and current1 != None and current1.data <= current2.data):
            if head_new == None:
                current_new = head_new = current1
            else:
                current_new.next = current1
                current_new = current_new.next
            current1 = current1.next
        elif (current1 == None and current2 != None) or (
                current2 != None and current1 != None and current2.data <= current1.data):
            if head_new == None:
                current_new = head_new = current2
            else:
                current_new.next = current2
                current_new = current_new.next
            current2 = current2.next

    return head_new