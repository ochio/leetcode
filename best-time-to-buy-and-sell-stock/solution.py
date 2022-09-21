class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        i, j = 0, 1
        profit = 0

        while j < len(prices):
            buy = prices[i]
            sell = prices[j]
            d = sell - buy
            if d <= 0:
                i = j
                j += 1
            elif d > 0:
                profit = max(profit, d)
                j += 1
        return profit
