class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # This is a dynamic programming problem
        def memoizationClimb(i):
            if i <= 1:
                return 0

            if i in memo:
                return memo[i]

            down_one = cost[i-1] + memoizationClimb(i-1)
            down_two = cost[i-2] + memoizationClimb(i-2)
            memo[i] = min(down_one, down_two)

            return memo[i]

        memo = {}
        return memoizationClimb(len(cost))
        # return self.tabulationClimb(cost)   # bottom up tabulation


    def tabulationClimb(self, cost: list[int]) -> int:
        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            one_step = min_cost[i-1] + cost[i-1]
            two_step = min_cost[i-2] + cost[i-2]
            min_cost[i] = min(one_step, two_step)

        return min_cost[-1]
