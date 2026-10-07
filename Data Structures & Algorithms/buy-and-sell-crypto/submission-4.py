class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_pr = 0
        while j<len(prices):
            if prices[i]>prices[j]:
                i=j
                j+=1
            else:
                max_pr = max(max_pr, prices[j]-prices[i])
                j+=1
        return max_pr

