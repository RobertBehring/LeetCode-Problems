class Solution:
    def runningSum(self, nums: list) -> list:
        """
        Given an array `nums`. We define a running sum of an array as
        `runningSum[i] = sum(nums[0]...nums[i]).

        Return the running sum of `nums`.
        """
        runningSum = 0
        outputNums = []
        for x in range(len(nums)):
            runningSum += nums[x]
            outputNums.append(runningSum)
        return outputNums
