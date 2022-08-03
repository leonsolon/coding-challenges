from bisect import insort


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        min_start = newInterval[0]
        max_end = newInterval[1]
        overlapping = []
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[1] and interval[0] <= newInterval[1]:
                min_start = min(min_start, interval[0])
                max_end = max(max_end, interval[1])
                overlapping.append(i)

        newInterval = [min_start, max_end]
        print(overlapping)
        if len(overlapping) == 0:
            insort(intervals, newInterval)
        else:
            overlapping = overlapping[::-1]
            intervals[overlapping.pop()] = newInterval

        for i in overlapping:
            intervals.pop(i)

        return intervals

