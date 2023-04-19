class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeroes, pos = 0, 0
        cur = pos + num_zeroes
        while cur < len(nums):
            if nums[cur] != 0:
                nums[pos] = nums[cur]
                pos += 1
            else:
                num_zeroes += 1
            cur = pos + num_zeroes

        while pos < len(nums):
            nums[pos] = 0
            pos += 1