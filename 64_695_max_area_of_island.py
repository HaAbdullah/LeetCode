# max_size = 0 

def maxAreaOfIsland(grid):
    max_size = 0 

    row = len(grid)
    col = len(grid[0])
    def areaOfIsland(r, c):
        nonlocal max_size
        if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
            return 0 
        grid[r][c] = 0
        left = areaOfIsland(r, c - 1)
        right = areaOfIsland(r, c + 1)
        up = areaOfIsland(r - 1, c)
        down = areaOfIsland(r + 1, c)

        current_size = 1 + left + right + up + down 
        #print(current_size)
        max_size = max(current_size, max_size)
        return current_size
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                print("found island!")
                areaOfIsland(r, c)
    return max_size

print(maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))