# Week 2
# Stacks
# Implement Queue using Stacks
# Runtime: 17 ms, faster than 88.27% of Python online submissions for Implement Queue using Stacks.
# Memory Usage: 13.6 MB, less than 12.26% of Python online submissions for Implement Queue using Stacks.

class MyQueue(object):

    def __init__(self):
        self.myq = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.myq.append(x)
        return

    def pop(self):
        """
        :rtype: int
        """
        return self.myq.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.myq[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.myq) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
