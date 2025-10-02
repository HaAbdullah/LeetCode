def pacificAtlantic(heights):
    pacific = set()
    atlantic = set()
    ROW = len(heights)
    COL = len(heights[0])

    def dfs(r, c, prev_height, ocean_set):
        if (
            r < 0 or r >= ROW or c < 0 or c >= COL or
            heights[r][c] < prev_height or (r, c) in ocean_set
        ):
            return
        ocean_set.add((r, c))
        dfs(r - 1, c, heights[r][c], ocean_set)
        dfs(r + 1, c, heights[r][c], ocean_set)
        dfs(r, c - 1, heights[r][c], ocean_set)
        dfs(r, c + 1, heights[r][c], ocean_set)

    # Pacific
    for i in range(COL):
        dfs(0, i, 0, pacific)
        dfs(ROW - 1, i, 0, atlantic)
    for i in range(ROW):
        dfs(i, 0, 0, pacific)
        dfs(i, COL - 1, 0, atlantic)

    return list(pacific & atlantic)

# Test
heights = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]

print(pacificAtlantic(heights))
