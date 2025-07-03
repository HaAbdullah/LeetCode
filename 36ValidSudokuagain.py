def isValidSudoku(board):
    r = { 0 : set(), 1 : set(), 2 : set(), 3 : set(), 4 : set(), 5 : set(), 6 : set(), 7 : set(), 8 : set()}
    c = { 0 : set(), 1 : set(), 2 : set(), 3 : set(), 4 : set(), 5 : set(), 6 : set(), 7 : set(), 8 : set()}
    b = { 0 : set(), 1 : set(), 2 : set(), 3 : set(), 4 : set(), 5 : set(), 6 : set(), 7 : set(), 8 : set()}
    for i in range(len(board)):
        for j in range(i):
            currentNum = board[i][j]
            if currentNum == ".":
                continue
            if currentNum in r[i]:
                print(f"currentNum: {currentNum}, r[]: {r[i]}")
                return False
            else:
                r[i].add(currentNum)
            if currentNum in c[j]:
                print(f"currentNum: {currentNum}, c[]: {c[i]}")
                return False
            else:
                r[i].add(currentNum)
                
            box_index = (i // 3) * 3 + (j // 3)
            if currentNum in b[box_index]:
                print(f"currentNum: {currentNum}, b[{box_index}]: {b[box_index]}")
                return False
            else:
                b[box_index].add(currentNum)
            
    return True
            
    
    
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))