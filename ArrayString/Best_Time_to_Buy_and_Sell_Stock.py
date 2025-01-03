class Solution:
    def maxProfit(self, prices: list) -> int:
        result = 0
        max_index = 0
        i = 0
        while i < len(prices):
            maximum = max(prices[i:])
            max_index = prices.index(maximum, i)
            minimum = min(prices[:max_index + 1])
            if maximum - minimum > result:
                result = maximum - minimum
            i = max_index + 1
        return result

        #min_price = prices[0]
        #max_profit = 0
        #
        #for price in prices[1:]:
        #    max_profit = max(max_profit, price - min_price)
        #    min_price = min(min_price, price)
        #    
        #return max_profit

nums = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(nums))
