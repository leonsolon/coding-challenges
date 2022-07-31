# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for current in lists:
            while current != None:
                heapq.heappush(heap, current.val)
                current = current.next
        if len(heap) > 0:
            head = prev = ListNode(heapq.heappop(heap))
            while len(heap) > 0:
                prev.next = ListNode(heapq.heappop(heap))
                prev = prev.next

            return head
        else:
            return None