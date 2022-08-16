from bisect import bisect, insort


class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            insort(self.time_map[key], (timestamp, value))

        else:
            self.time_map[key] = [(timestamp, value)]

        # print(self.time_map)

    def get(self, key: str, timestamp: int) -> str:

        if not key in self.time_map:
            return ''
        else:
            idx = bisect(self.time_map[key], (timestamp, 'None'))
            # print(idx, timestamp)
            if idx >= len(self.time_map[key]):
                return self.time_map[key][idx - 1][1]
            else:
                if self.time_map[key][idx][0] == timestamp:
                    return self.time_map[key][idx][1]
                else:
                    if idx == 0:
                        return ""
                    else:
                        return self.time_map[key][idx - 1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)