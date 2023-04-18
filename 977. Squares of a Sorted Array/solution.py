class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sortedSquares = list()

        neg_idx = -1
        for i in range(len(nums)):
            if nums[i] < 0:
                neg_idx = i
        pos_idx = neg_idx + 1

        while pos_idx < len(nums) or neg_idx >= 0:
            if pos_idx >= len(nums) or (abs(nums[neg_idx]) < nums[pos_idx]):
                sortedSquares.append(nums[neg_idx]**2)
                neg_idx -= 1
            else:
                sortedSquares.append(nums[pos_idx]**2)
                pos_idx += 1

        return sortedSquares
