def stock(prices):
    prices.reverse()
    max = 0
    for i in range(len(prices)):
        difference = prices[i] - min(prices[i:])
        if (difference) > max:
            max = (difference)
    return max
            
# 4 6 3 5
print(stock([7,1,5,3,6,4]))