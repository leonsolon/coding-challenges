
# 20 / 22 test cases passed.


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.len = 0
        self.dict = dict()
        self.used = []

    def get(self, key: int) -> int:
        if key in self.dict:
            self.used.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if self.len < self.capacity:
                self.len += 1
            else:
                set_used = set()
                used = self.used[::-1]
                next_used = []
                for i, k in enumerate(used):
                    if k in self.dict:
                        set_used.add(k)
                        if len(set_used) == self.capacity:
                            self.dict.pop(k)
                            break
                        next_used.append(k)
                self.used = next_used[::-1]

        self.used.append(key)
        self.dict[key] = value
        # print(self.dict, self.used, self.len)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)