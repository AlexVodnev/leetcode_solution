def maxProfit(prices) -> int:
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

prices = [7,1,5,3,4,6]
print(maxProfit(prices))