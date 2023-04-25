class Solution:

    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        # return self.robFrom(0, nums)
        # return self.dpRob(nums)
        return self.optDPRob(nums)

    def optDPRob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[n - 1]

        for i in range(n - 2, -1, -1):
            current = max(rob_next, rob_next_plus_one + nums[i])

            rob_next_plus_one = rob_next
            rob_next = current

        return rob_next

    def dpRob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        maxRobbedAmount = [None for _ in range(len(nums) + 1)]
        n = len(nums)

        maxRobbedAmount[n], maxRobbedAmount[n - 1] = 0, nums[n - 1]

        for i in range(n - 2, -1, -1):
            maxRobbedAmount[i] = max(maxRobbedAmount[i + 1],
                                     maxRobbedAmount[i + 2] + nums[i])

        return maxRobbedAmount[0]

    def robFrom(self, i, nums):
        if i >= len(nums):
            return 0

        if i in self.memo:
            return self.memo[i]

        ans = max(self.robFrom(i + 1, nums),
                  self.robFrom(i + 2, nums) + nums[i])

        self.memo[i] = ans
        return ans
