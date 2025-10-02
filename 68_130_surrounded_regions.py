def solve(board):
    # x x x x 
    # x o o x 
    # x x o x 
    # x o x x
    ROW = len(board)
    COL = len(board[0])
    def dfs(r, c, symbol):
        if r < 0 or r >= ROW or c < 0 or c >= COL or board[r][c] != 'O':
            return 
        board[r][c] = symbol
        dfs(r - 1, c, symbol)
        dfs(r + 1, c, symbol)
        dfs(r, c - 1, symbol)
        dfs(r, c + 1, symbol)
        
    # find all "o"'s that are on the border and mark them as safe
    for row in range(ROW):
        if board[row][0] == "O":
            dfs(row, 0, "S")
        if board[row][COL - 1] == "O":
            dfs(row, COL - 1, "S")
    for col in range(1, COL - 1):
        if board[0][col] == "O":
            dfs(0, col, "S")
        if board[ROW - 1][col] == "O":
            dfs(ROW - 1, col, "S")

    # find all "o"'s that are left over, and mark them as captured 
    for i in range(ROW):
        for j in range(COL):
            if board[i][j] == 'O':
                board[i][j] = 'X'
                
    for i in range(ROW):
        for j in range(COL):
            if board[i][j] == 'S': board[i][j] = 'O'
    
print(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))

print(solve([["O","O"],["O","O"]]))

# O O 
# O O