import heapq


class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        # print(self.stack)
        # print(self.heap)

    def pop(self) -> None:
        a = self.stack.pop()
        # print(self.stack)
        # print(self.heap)
        return a



    def top(self) -> int:
        # print(self.stack)
        # print(self.heap)
        return self.stack[-1]


    def getMin(self) -> int:
        min_value = heapq.heappop(self.heap)
        while min_value not in self.stack:
            min_value = heapq.heappop(self.heap)
        heapq.heappush(self.heap, min_value)
        # print(self.stack)
        # print(self.heap)
        return min_value

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()