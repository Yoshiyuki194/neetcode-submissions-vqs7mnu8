class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minP = prices[0]
        res = 0
        for price in prices:
            minP = min(minP, price)
            res = max(res, price - minP)
        return res