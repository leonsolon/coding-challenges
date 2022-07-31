import queue
class MyStack:

    def __init__(self):
        self.queue = queue.LifoQueue()

    def push(self, x: int) -> None:
        self.queue.put(x)

    def pop(self) -> int:
        return self.queue.get()

    def top(self) -> int:
        x = self.queue.get()
        self.queue.put(x)
        return x

    def empty(self) -> bool:
        return self.queue.empty()
