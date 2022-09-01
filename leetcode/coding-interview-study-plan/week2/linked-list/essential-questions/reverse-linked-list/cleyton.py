#9'




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next : return head
        
        curr = head
        prev = None
        while curr:
            aux = curr.next
            curr.next = prev
            prev = curr
            curr = aux
        
        return prev



class Solution: #Better
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
