#11'

#Link: https://leetcode.com/problems/linked-list-cycle/


# Runtime: 57 ms, faster than 93.67% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.5 MB, less than 67.21% of Python3 online submissions for Linked List Cycle.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next: return False
        
        fast, slow  = head, head
        
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next
            if fast == slow:
                return True
            
        
        return False
