class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buyDay = 0
        sellDay = 1
        while sellDay < len(prices):
            if prices[buyDay] < prices[sellDay]:
                profit = prices[sellDay] - prices[buyDay]
                max_profit = max(max_profit, profit)
            else:
                buyDay = sellDay
            sellDay += 1

        return max_profit