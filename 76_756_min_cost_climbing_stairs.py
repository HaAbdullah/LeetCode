def minCostClimbingStairs(cost):
    n = len(cost)
    memo = [-1] * n
    def dfs(i):
        if i >= n:
            return 0
        if memo[i] != -1:
            return memo[i] 
        memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
        return memo[i]
    return min(dfs(0), dfs(1))


def minCostClimbingStairs(cost):
    L = cost[0]
    R = cost[1]
    n = len(cost)
    for i in range(2, n):
        print(L, R)
        new = cost[i] + min(L, R) 
        L = R 
        R = new 

        
    return min(L, R)
    
print(minCostClimbingStairs(cost = [10,15,20]))