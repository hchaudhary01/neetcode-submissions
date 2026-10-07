class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1

        while j<len(prices):
            if prices[i]>=prices[j]:
                #print(prices[i],"prices[i] and prices[j]", prices[j])
                i =j
            else:
                profit = max(profit, prices[j]-prices[i])
                #print(profit, prices[i], prices[j])
            j+=1
        return profit
