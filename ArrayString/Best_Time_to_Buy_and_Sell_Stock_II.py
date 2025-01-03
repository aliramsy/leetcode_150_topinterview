class Solution:
    def maxProfit(self, prices: list) -> int:
        max_profit = 0
        full_profit = 0
        minimum = prices[0]
        length = len(prices)
        for i, price in enumerate(prices):
            if max_profit < price - minimum:
                max_profit = price - minimum
            else:
                full_profit += max_profit
                minimum = price
                max_profit = 0
        return full_profit + max_profit


nums = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(nums))
