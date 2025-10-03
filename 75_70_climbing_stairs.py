def climbingStairs(n):

    def dfs(current_level):
        if current_level == n:
            return 1
        if current_level > n: 
            return 0
        # option 1: take 1 step or option 2: take 2 steps 
        return dfs(current_level + 1) + dfs(current_level + 2)
    return dfs(0)
print(climbingStairs(2))