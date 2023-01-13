# v1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        cur_price = prices[0]
        for val in prices[1 : ]:
            if (val > cur_price) and (val - cur_price > profit):
                profit = val - cur_price
            elif val < cur_price:
                cur_price = val
        return profit
