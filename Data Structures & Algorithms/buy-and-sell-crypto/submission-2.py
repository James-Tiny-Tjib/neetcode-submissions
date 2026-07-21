class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        max_profit = 0
        l = 0

        for r in range(len(prices)):
            
            if prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]
            
            if prices[r] < prices[l]:
                l += r - l
        
        return max_profit


            


 




