# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        count = 0
        current = head

        while current != None:
            current = current.next
            count += 1

        current = head

        for _ in range(0, count // 2):
            current = current.next
            count += 1

        return current
