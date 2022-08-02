# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        links = []
        while current != None:
            if current in links:
                return True
            else:
                links.append(current)

            current = current.next

        return False