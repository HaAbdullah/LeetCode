
# 1 0 
# 0 1 

# res = 1 
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0 
# 0 0 0 0 0 

# res = 2 
# 0 0 0
# 0 0 0
# 0 0 0 


# 1 1 0 0 0 
# 1 1 0 0 0 
# 0 0 1 0 0 
# 0 0 0 1 1 

def numIslands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0 
    
    def dfs(r, c):
        
        # Base case: if we are out of bounds or in water
        
        if r < 0 or r > rows or c < 0 or c > cols or grid[r][c] == '0':
            return 
        
        grid[r][c] = '0'
        
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1 
                dfs(r, c)
    return count 