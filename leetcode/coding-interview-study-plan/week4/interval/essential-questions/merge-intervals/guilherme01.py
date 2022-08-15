class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        last_interval = []
        new_intervals = []
        for i, interval in enumerate(intervals):
            if i != 0:
                if last_interval[1] >= interval[0]:
                    start = min(interval[0], last_interval[0])
                    end = max(interval[1], last_interval[1])
                    last_interval = [start, end]
                else:
                    new_intervals.append(last_interval)
                    last_interval = interval
            else:
                last_interval = interval

        new_intervals.append(last_interval)
        return new_intervals
