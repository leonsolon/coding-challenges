from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return not len(self.stack)

# Runtime: 54 ms, faster than 30.43% of Python3 online submissions for Implement Stack using Queues.
# Memory Usage: 13.9 MB, less than 98.63% of Python3 online submissions for Implement Stack using Queues.