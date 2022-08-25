from collections import deque

class MyQueue:

    def __init__(self):
        self.queue = deque()        

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return not len(self.queue)

# Runtime: 49 ms, faster than 44.54% of Python3 online submissions for Implement Queue using Stacks.
# Memory Usage: 13.9 MB, less than 75.94% of Python3 online submissions for Implement Queue using Stacks.