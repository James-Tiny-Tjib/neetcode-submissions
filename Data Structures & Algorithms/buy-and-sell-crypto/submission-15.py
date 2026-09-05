class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l = 0
        for r in range(len(prices)):
            if prices[l] < prices[r]:
                maxP = max(prices[r] - prices[l], maxP)
            else:
                l = r
        
        return maxP