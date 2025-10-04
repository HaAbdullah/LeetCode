def coinChange(coins, amount):
    def dfs(amount):
        if amount == 0:
            return 0 
        res = float('inf')
        for coin in coins:
            if (amount - coin) >= 0:
                res = min(res, 1 + dfs(amount - coin))
        return res 
    
    res = dfs(amount)
    return res 

print(coinChange([1,2,5], 11))