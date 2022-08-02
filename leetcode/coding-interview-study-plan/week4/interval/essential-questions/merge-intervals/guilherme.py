class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while i+1 < len(intervals):
            interval1 = intervals[i]
            interval2 = intervals[i+1]

            if interval2[0] <= interval1[1]:
                intervals[i] = [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
                intervals.remove(interval2)
            else:
                i += 1
        return intervals