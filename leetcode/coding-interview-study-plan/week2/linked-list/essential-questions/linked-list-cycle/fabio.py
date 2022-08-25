class Solution:
    def hasCycle(self, head):
        if head:
            traversed = set()
            current = head
            while current.next:
                if id(current) in traversed:
                    return True
                traversed.add(id(current))
                current = current.next
            return False

# Runtime: 86 ms, faster than 51.75% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 17.9 MB, less than 10.42% of Python3 online submissions for Linked List Cycle.