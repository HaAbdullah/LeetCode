class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:  
        row = len(grid)
        col = len(grid[0])
        def dfs(r, c, distance_from_0):
            # grid[r][c] < distance_from_0 allows you to change values that are -1 or already smaller than what is being returned rn 
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] < distance_from_0:
                return
            
            # we have made sure that the current distance from the 0 is the shortest path so far so:
            grid[r][c] = distance_from_0
            distance_from_0 += 1 
            dfs(r - 1, c, distance_from_0)
            dfs(r + 1, c, distance_from_0)
            dfs(r, c - 1, distance_from_0) 
            dfs(r, c + 1, distance_from_0)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    dfs(r, c, 0)

# BFS Optimal Solution
from collections import deque 
row = len(grid)
col = len(grid[0])
def checkBoundaries(r, c, distance):
    return not (r >= row or r < 0 or c >= col or c < 0 or grid[r][c] < distance)
def islandsAndTreasure (grid):
    q = deque()
    
    # add all the starting locations (treasures) to the queue 
    for r in range(row):
        for c in range(col):
            if grid[r][c] == 0:
                q.append((r, c))

    distance = 0
    # perform BFS on the q
    while q:
        # each layer of BFS
        for i in range(len(q)):
            r, c = q.popLeft()
            grid[r][c] = distance 

            # left 
            if checkBoundaries(r, c - 1):
                q.append((r, c, distance))
            # right
            if checkBoundaries(r, c + 1):
                q.append((r,c,distance))
            #up 
            if checkBoundaries(r - 1, c):
                q.append((r,c,distance))
            # down 
            if checkBoundaries(r - 1, c):
                q.append((r,c,distance))

        distance += 1 
# this is the inopitmal O(m * n)^2 solution
INF = 2147483647

def nearest_treasure_from_houses(grid):
    if not grid or not grid[0]:
        return

    m, n = len(grid), len(grid[0])

    def dfs(i, j, dist, visited):
        # Boundary, water, and cycle check
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == -1:
            return INF
        # Found a treasure
        if grid[i][j] == 0:
            return dist
        visited.add((i, j))
        # Explore 4 directions
        dists = [
            dfs(i + 1, j, dist + 1, visited),
            dfs(i - 1, j, dist + 1, visited),
            dfs(i, j + 1, dist + 1, visited),
            dfs(i, j - 1, dist + 1, visited)
        ]
        visited.remove((i, j))
        return min(dists)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == INF:
                grid[i][j] = dfs(i, j, 0, set())

# Example
grid = [
    [INF,-1,0,INF],
    [INF,INF,INF,-1],
    [INF,-1,INF,-1],
    [0,-1,INF,INF]
]

nearest_treasure_from_houses(grid)
print(grid)
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
