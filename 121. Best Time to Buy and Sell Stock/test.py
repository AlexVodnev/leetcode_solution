def maxProfit(prices) -> int:
    min_price = 10 ** 4
    mp = 0
    for i in range(len(prices)):
        if prices[i] >= min_price:
            pass
        else:
            min_price = prices[i]        
        mp = max(prices[i] - min_price, mp)
    return mp


pr = [1,2]
print(maxProfit(pr))