def n_queens(n):
    result = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    diag1 = set()
    diag2 = set()

    def backtracking(row):
        if row == n:
            result.append(["".join(r) for r in board])

        for col in range(n):
            if(col in cols or 
               (row - col) in diag1 or
               (row + col) in diag2):
                continue

            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            backtracking(row+1)

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtracking(0)
    return result