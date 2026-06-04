class Solution(object):
    def maxProfit(self, prices):
        minprice = float('inf')
        maxprofit = 0
        for price in prices:
            if price < minprice:
                minprice = price
            maxprofit = max(price-minprice, maxprofit)
        return maxprofit  