class Solution:
    def reverseList(self, head):
        
        if head:
            current = head
            temp = current.next
            next_ = None

            while current.next:

                current.next = next_
                next_ = current
                current = temp
                temp = current.next

            current.next = next_
            head = current
        
        return head

# Runtime: 58 ms, faster than 47.84% of Python3 online submissions for Reverse Linked List.
# Memory Usage: 15.4 MB, less than 56.30% of Python3 online submissions for Reverse Linked List.