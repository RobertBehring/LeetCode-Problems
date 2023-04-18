class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsCopy = nums.copy()
        for i in range(len(nums)):
            nums[i] = numsCopy[(len(nums)-k+i)%len(nums)]
