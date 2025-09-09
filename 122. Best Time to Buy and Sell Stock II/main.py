class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = -1
        for i in range(len(prices) - 1):
            if prices[i +1] > prices[i]:
                n = i
                break
        if n == -1:
            return 0
        mp = 0
        for i in range(n, len(prices) - 1):
            if prices[i +1] > prices[i]:
                mp += prices[i +1] - prices[i]
        return mp