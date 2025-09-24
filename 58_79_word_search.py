def exist(board, word):

    def backtrack(i, x, y):
        # base case: reached last char
        if i == len(word) - 1:
            return True

        left = right = up = down = False
        temp = board[x][y]
        board[x][y] = -1
        # option 1: left
        if x - 1 >= 0 and board[x-1][y] == word[i+1] and board[x-1][y] != -1 :
            left = backtrack(i + 1, x - 1, y)

        # option 2: up
        if y - 1 >= 0 and board[x][y-1] == word[i+1] and board[x][y-1] != -1:
            up = backtrack(i + 1, x, y - 1)

        # option 3: right
        if x + 1 < rows and board[x+1][y] == word[i+1] and board[x+1][y] != -1:
            right = backtrack(i + 1, x + 1, y)

        # option 4: down
        if y + 1 < cols and board[x][y+1] == word[i+1] and board[x][y+1] != -1:
            down = backtrack(i + 1, x, y + 1)

        board[x][y] = temp
        return left or right or up or down

    rows, cols = len(board), len(board[0])
    for x in range(rows):
        for y in range(cols):
            if board[x][y] == word[0]:
                if backtrack(0, x, y): 
                    return True
    return False

print(exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        m, n = len(board), len(board[0])
        wlen = len(word)

        # Quick feasibility: if the board lacks enough occurrences of a character required by word -> False
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        for ch, req in word_count.items():
            if board_count.get(ch, 0) < req:
                return False

        # Minor heuristic: search from rarer end of the word to reduce branching
        if board_count[word[-1]] < board_count[word[0]]:
            word = word[::-1]

        # Localize for speed
        B = board
        W = word

        def dfs(i: int, j: int, k: int) -> bool:
            # k is index in W
            if k == wlen:
                return True

            # bounds + char check
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            ch = B[i][j]
            if ch != W[k]:
                return False

            # mark visited in-place
            B[i][j] = '#'
            # explore 4 neighbors
            nk = k + 1
            if (dfs(i+1, j, nk) or dfs(i-1, j, nk) or
                dfs(i, j+1, nk) or dfs(i, j-1, nk)):
                return True

            # restore and backtrack
            B[i][j] = ch
            return False

        # start DFS from every cell equal to first char
        first = W[0]
        for i in range(m):
            for j in range(n):
                if B[i][j] == first:
                    if dfs(i, j, 0):
                        return True
        return False