class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_prices=prices[0]
        max_p=0
        for i in range(1,len(prices)):
            if prices[i]<min_prices:
                min_prices=prices[i]
            profit=prices[i]-min_prices
            if profit>max_p:
                max_p=profit
        return max_p        
            
                
