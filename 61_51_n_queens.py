def solveNQueens(n):
    board = ["." * n for _ in range(n)]


    res = []
    queenN = 0 
    def backtrack(queenN, forbidden_cols, forbidden_up_diagonals, forbidden_down_diagonals, queen_positions):
        if queenN == n:
            res.append(board[:])
            return
        # Try all possible columns for each row 
        for i in range(n):
            up_diagonal = i + queenN 
            down_diagonal = queenN - i 
            if i not in forbidden_cols and up_diagonal not in forbidden_up_diagonals and down_diagonal not in forbidden_down_diagonals:
                forbidden_cols.add(i)
                forbidden_up_diagonals.add(up_diagonal)
                forbidden_down_diagonals.add(down_diagonal)
                queen_positions.append(i)


                board[queenN] = "." * n
                board[queenN] = board[queenN][:i] + 'Q' + board[queenN][i+1:]
                backtrack(queenN + 1, forbidden_cols, forbidden_up_diagonals, forbidden_down_diagonals, queen_positions)

                forbidden_cols.remove(i)
                forbidden_up_diagonals.remove(up_diagonal)
                forbidden_down_diagonals.remove(down_diagonal)
                queen_positions.pop()

    backtrack(0, set(), set(), set(), [])
    return res
print(solveNQueens(4))