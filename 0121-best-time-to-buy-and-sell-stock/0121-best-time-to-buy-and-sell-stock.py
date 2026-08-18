class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_prof = 0
        #res = [] ## for debug only
        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_prof = max(max_prof, profit)
            #res.append(max_prof) # not required, for debug only
        return max_prof
        


## 7,1,5,3,6,4 - maxprofit = 1 par stock buy karun and 6 par sell kar du
# sabse min price lo, profit nikalo, usko max_profit kardo
## max_prof = 0, 0, 4, 4, 5, 

