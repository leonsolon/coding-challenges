# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue


class Solution:
    from queue import PriorityQueue
    def mergeKLists(self, lists):
        queue = PriorityQueue()
        for current in lists:
            while current != None:
                queue.put(current.val)
                current = current.next

        if not queue.empty():
            current = ListNode(queue.get())
            head = current
            while not queue.empty():
                print(current.val)
                current.next = ListNode(queue.get())
                current = current.next

            return head
        else:
            return None