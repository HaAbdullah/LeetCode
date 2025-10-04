# constraint: either rob i or rob i + 1 

# nums = 1, 2, 3, 1
# 1, 2, 1, 3
# 1 _ 3 _ = 4
# 1 _ _ 3 = 4 
# _ 2 _ 1  = 3
# 
#  max(rob([0] + rob([2], rob[1])))

def rob(nums):
    cache = [-1] * len(nums)
    def dfs(i):
        if i >= len(nums):
            return 0
        if cache[i] != -1:
            return cache[i]
        cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        return cache[i]
    return dfs(0) 

def rob(nums):
    dp = [0] * len(nums)
    dp_1 = 0 
    dp_2 = 0 

    for i in range(len(nums) - 1, -1, -1):
        dp[i] = max(dp_1, nums[i] + dp_2)
        dp_2 = dp_1
        dp_1 = dp[i]
    return dp_1 
    
 
print(rob([2,7,9,3,1]))