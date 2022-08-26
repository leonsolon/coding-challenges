# Week 2
# Queue
# Implement Stack using Queues
# Runtime: 30 ms, faster than 28.85% of Python online submissions for Implement Stack using Queues.
# Memory Usage: 13.2 MB, less than 97.73% of Python online submissions for Implement Stack using Queues.

class MyStack(object):

    def __init__(self):
        self.mystack = []    

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.mystack.append(x)
        return

    def pop(self):
        """
        :rtype: int
        """
        return self.mystack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.mystack[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.mystack) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
