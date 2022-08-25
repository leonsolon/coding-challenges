# Runtime: 8714 ms, faster than 5.00% of Python3 online submissions for LRU Cache.
# Memory Usage: 71.9 MB, less than 99.85% of Python3 online submissions for LRU Cache.
from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.dict = dict()
        self.used = deque()

    def get(self, key: int) -> int:
        if key in self.dict:
            if key in self.used:
                self.used.remove(key)
            self.used.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.len < self.capacity:
                self.len += 1
            else:
                key_del = self.used.popleft()
                self.dict.pop(key_del)
        if key in self.used:
            self.used.remove(key)
        self.used.append(key)
        self.dict[key] = value
        # print(self.dict, self.used, self.len)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)