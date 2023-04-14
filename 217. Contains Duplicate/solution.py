class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        """
        Given an integer array `nums`, return `true` if any value appears at
        least twice in the array, and return `false` if every element
        is distinct.

        :param nums:
        :return:
        """
        numsSet = set(nums)
        if len(numsSet) == len(nums):
            return False
        return True
