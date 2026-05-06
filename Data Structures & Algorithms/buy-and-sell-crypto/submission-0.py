class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_max = prices[len(prices)-1]
        for i in range(len(prices)-1,-1,-1):
            max_profit = max(max_profit,cur_max - prices[i])
            cur_max = max(prices[i],cur_max)
        return max_profit