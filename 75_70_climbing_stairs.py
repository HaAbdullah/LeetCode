def climbStairs(n):
    memoized_results = [-1] * (n + 1) 
    def dfs(level):
        if level == n:
            return 1 
        if level > n:
            return 0 
        if memoized_results[level] != -1:
            return memoized_results[level]
        memoized_results[level] = dfs(level + 1) + dfs(level + 2)
        return memoized_results[level]
    return dfs(0)
#print(climbStairs(5))
    
# we know to solve 5 stairs we need to start at 0 and try all possibilities that eventually lead up to 5
# but we will be repeating certain sub problems again and again
# for example, 2 + 1 and 1 + 2 will both end up at 3 so if we calculate what happens after one of them, we wont need to calculate it again
# so we can store the result of each calculated result after we've calculated it and use it first if it comes again


# we now know that we can memoize results to save lots of time if we encounter that same one again, however, instead of starting from the top case and moving down
# we should instead go from the bottom fundamnetal base case and see how we can build towards the desired input (0)

# 5: how many ways to get from 5 to 5? 1, you're already there nothing is required
# 4: how many wayus to get from 4 to 5? 1, move up 1
# 3: how many ways? you can either go to 4 first which then required 1 step or you can go to 5 which requires 1: 1 + 1 = 2
# 2: you can either go to 3 (2 ways) or 4 (1 way) = 3
# 1: 2 or 3 : 3 + 2 = 5
# 0: 5 + 3 = 8

def climbStairs(n):
    steps = [-1] * (n + 1)
    steps[-1] = 1
    steps[-2] = 1
    for i in range(n - 2, -1, -1):
        steps[i] = steps[i + 1] + steps[i + 2]
    return steps[0]        
print(climbStairs(5))


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one