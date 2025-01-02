def isValidSudoku(board):
    # 3 x 3 board:
    sums = {
        1:set(),
        2:set(),
        3:set(),
        4:set(),
        5:set(),
        6:set(),
        7:set(),
        8:set(),
        9:set(),   
    }
    # Check row 
    Squares = [[],[],[],[],[],[],[],[],[]]
    for i in range(len(board)):
        currentRow = set()
        currentColumn = set()
        for j in range(len(board[i])): 
            if board[i][j] != ".":
                if board[i][j] not in currentRow:
                    currentRow.add(board[i][j])
                else:
                    return False
            if board[j][i] != ".":
                if board[j][i] not in currentColumn:
                    currentColumn.add(board[j][i])
                else:
                    return False
    Squares[0].append(board[0][0:3])
    Squares[0].append(board[1][0:3])
    Squares[0].append(board[2][0:3])
    Squares[1].append(board[0][3:6])
    Squares[1].append(board[1][3:6])
    Squares[1].append(board[2][3:6])
    Squares[2].append(board[0][6:])
    Squares[2].append(board[1][6:])
    Squares[2].append(board[2][6:])
    Squares[3].append(board[0][0:3])
    Squares[3].append(board[1][0:3])
    Squares[3].append(board[2][0:3])
    Squares[4].append(board[0][3:6])
    Squares[4].append(board[1][3:6])
    Squares[4].append(board[2][3:6])
    Squares[5].append(board[0][6:])
    Squares[5].append(board[1][6:])
    Squares[5].append(board[2][6:])
    Squares[6].append(board[1][0:3])
    Squares[6].append(board[2][0:3])
    Squares[6].append(board[0][0:3])
    Squares[7].append(board[1][3:6])
    Squares[7].append(board[2][3:6])
    Squares[7].append(board[0][3:6])
    Squares[8].append(board[1][6:6])
    Squares[8].append(board[2][6:6])
    Squares[8].append(board[0][3:6])
    
    for i in range(9):
        currentSquare = set()
        for j in range(3):
            if Squares[j][i] != ".":
                if Squares[j][i] not in currentSquare:
                    currentSquare.add(Squares[j][i])
                else:
                    return False

    
    
    print(Squares)
    return True

print(isValidSudoku([
 ["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))