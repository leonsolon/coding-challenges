# 20 / 22 test cases passed.


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.count = 0
        self.dict = dict()

    def get(self, key: int) -> int:
        if key in self.dict:
            self.dict[key][1] = self.count
            self.count += 1
            return self.dict[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.len < self.capacity:
                self.len += 1
            else:
                key_del = min(self.dict.items(), key=lambda x: x[1][1])
                del (self.dict[key_del[0]])
        self.dict[key] = [value, self.count]
        self.count += 1
        # print(self.dict, self.count, self.len)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)