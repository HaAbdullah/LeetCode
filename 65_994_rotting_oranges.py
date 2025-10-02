
# BFS 

from collections import deque 
def orangeRotting(grid):
    row = len(grid)
    col = len(grid[0])
    q = deque()
    fresh = 0 
    # add all exisiting rotted oranges to the queue
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 2:
                q.append((r, c))
                print(f"intial q: {q}")
            elif grid[r][c] == 1:
                fresh += 1 
    
    def checkBoundaries(r, c):
        return not (r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1 )
    time = 0

    while q and fresh > 0:
        print(q)
        for i in range(len(q)):
            r, c = q.popleft()
            # add all oranges from the next layer 
            # up
            if checkBoundaries(r - 1, c):
                grid[r - 1][c] = 2
                q.append((r - 1, c))
                fresh -= 1
            if checkBoundaries(r + 1, c):
                grid[r + 1][c] = 2
                q.append((r + 1, c))
                fresh -= 1
            if checkBoundaries(r, c - 1):
                grid[r][c - 1] = 2
                q.append((r, c - 1))
                fresh -= 1
            if checkBoundaries(r, c + 1):
                grid[r][c + 1] = 2
                q.append((r, c + 1))
                fresh -= 1
        time += 1 
    return time if fresh == 0 else -1
    





print(orangeRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))

#print(orangeRotting(grid = [[0]]))
#print(orangeRotting(grid = [[2,1,1],[0,1,1],[1,0,1]]))