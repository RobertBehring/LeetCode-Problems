class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid
        return True if self.binarySearch(matrix[lo], target) != -1 else False

    def binarySearch(self, nums: list, target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid
        return lo if nums[lo] == target else -1