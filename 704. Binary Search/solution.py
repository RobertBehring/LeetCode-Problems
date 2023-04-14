class Solution:
    """
    The following solution is derived from AminiCK's solution from the post
    Binary Search 101 (https://leetcode.com/problems/binary-search/solutions
    /423162/binary-search-101/?envType=study-plan&id=algorithm-i&orderBy=most_votes)
    posted on Nov. 07, 2019
    """
    def search(self, nums: list, target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi-lo+1) // 2
            # can also calculate mid the following ways
            # mid = lo + (hi-lo) // 2 # left/lower mid
            # mid = lo + (hi-lo+1) // 2 # right/upper mid
            # mid = (lo+hi) // 2 # worst, easy to overflow
            # mid = lo + (hi-lo) // 2 # better
            # mid = (lo+hi) >>> 1 # best, but can't do this in python
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid
        return lo if nums[lo] == target else -1
