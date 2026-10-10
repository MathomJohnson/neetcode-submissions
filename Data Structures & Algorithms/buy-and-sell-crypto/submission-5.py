class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0
        l, r = 0, 1

        while r < len(prices):

            curr = prices[r] - prices[l]
            res = max(res, curr)

            if prices[r] < prices[l]:
                l = r

            r += 1

        return res