from bisect import insort


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:
            return [newInterval]

        overlapping_intevals_idx = []
        min_start = newInterval[0]
        max_end = newInterval[1]
        idx_insert = float('inf')
        for i, interval in enumerate(intervals):
            if newInterval[0] <= interval[1] and interval[0] <= newInterval[1]:
                min_start = min(min_start, interval[0])
                max_end = max(max_end, interval[1])
                overlapping_intevals_idx.append(i)
                idx_insert = min(i, idx_insert)

        if len(overlapping_intevals_idx) == 0:
            insort(intervals, newInterval)
        else:
            intervals[idx_insert] = [min_start, max_end]
            overlapping_intevals_idx.remove(idx_insert)

            for i in overlapping_intevals_idx[::-1]:
                intervals.pop(i)

        return intervals