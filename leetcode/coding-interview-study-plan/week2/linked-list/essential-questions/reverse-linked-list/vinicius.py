'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Success
Details 
Runtime: 67 ms, faster than 26.55% of Python3 online submissions for Reverse Linked List.
Memory Usage: 15.4 MB, less than 56.30% of Python3 online submissions for Reverse Linked List.
Next challenges:
Reverse Linked List II
Binary Tree Upside Down
Palindrome Linked List
Reverse Nodes in Even Length Groups
Maximum Twin Sum of a Linked List
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return ListNode(val='', next=None)
        node = head
        prev = None
        while node:
            prox = node.next
            node.next = prev
            prev = node
            node = prox
        return prev