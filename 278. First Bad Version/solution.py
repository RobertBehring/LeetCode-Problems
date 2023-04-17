# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 0
        hi = n
        while lo < hi:
            mid = lo + (hi-lo+1) // 2
            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid

        return lo+1
