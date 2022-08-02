# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return list1
        elif list1 == None or (list2 != None and list2.val <= list1.val):
            current = list2
            current1 = list1
            current2 = list2.next
        elif list2 == None or (list1 != None and list1.val < list2.val):
            current = list1
            current1 = list1.next
            current2 = list2

        head = current

        while current1 != None or current2 != None:
            if (current1 == None) or (current2 != None and current2.val <= current1.val):
                current.next = current2
                current2 = current2.next
            elif (current2 == None) or (current1 != None and current1.val < current2.val):
                current.next = current1
                current1 = current1.next
            current = current.next

        return head


