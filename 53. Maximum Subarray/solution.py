class Solution:
    def maxSubArray(self, nums: list) -> int:
        """
        Given an integer array `nums`, find the subarray with the largest
        sum, and return its sum.

        Subarray: Contiguous non-empty sequence of elements in an array

        :param nums:
        :return:
        """
        current_sum = nums[0]  # starting idx by default
        max_sum = current_sum

        for i in range(1, len(nums)):
            running_sum = current_sum + nums[i]
            local_sum = nums[i-1] + nums[i]
            current_sum = max(running_sum, local_sum, nums[i])
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
