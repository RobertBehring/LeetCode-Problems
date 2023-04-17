class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi-lo+1) // 2
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid

        ret = -1

        if nums[lo] == target:
            ret = lo
        if nums[lo] > target:
            ret = lo
        if nums[lo] < target:
            ret = lo + 1

        return ret
