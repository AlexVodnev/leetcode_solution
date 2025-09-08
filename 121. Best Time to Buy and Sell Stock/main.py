class ComboSolution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 4
        mp = 0
        for i in range(len(prices)):
            if prices[i] >= min_price:
                pass
            else:
                min_price = prices[i]        
            p = prices[i] - min_price
            if p > mp:
                mp = p
        return mp

class MySolution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10 ** 4
        mp = 0
        for i in range(len(prices) - 1):
            if prices[i + 1] < prices[i]:
                pass
            else:
                if prices[i] >= min_price:
                    pass
                else:
                    min_price = prices[i]
                    for j in range(i, len(prices)):
                        p = prices[j] - prices[i]
                        if p > mp:
                            mp = p
        return mp