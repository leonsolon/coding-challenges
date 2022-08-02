# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        def get_bad(start, end):
            if start == end:
                return start
            middle = start + (end - start) // 2
            if isBadVersion(middle):
                return get_bad(start, middle)
            else:
                return get_bad(middle + 1, end)

        return get_bad(1, n)