def dfs_n_queens_with_board(n: int) -> list[list[str]]:
    """
    Find all solutions to the N-Queens problem
    for an `n` x `n` board using DFS with backtracking.

    Return each solution as a list of strings
    representing the board, with `Q` marking a Queen
    and `.` marking an empty square.
    """

    if n < 1 or n == 2 or n == 3:
        return []

    if n == 1:
        return [['Q']]

    solutions = []
    board = [['.'] * n for _ in range(n)]

    cols = set()
    main_diagonal = set()
    anti_diagonal = set()

    def dfs(row: int) -> None:
        if row == n:
            solutions.append([''.join(r) for r in board])
            return

        for col in range(n):
            diagonal_1 = row - col + (n - 1)
            diagonal_2 = row + col

            if (
                col in cols
                or diagonal_1 in main_diagonal
                or diagonal_2 in anti_diagonal
            ):
                continue

            board[row][col] = 'Q'
            cols.add(col)
            main_diagonal.add(diagonal_1)
            anti_diagonal.add(diagonal_2)

            dfs(row + 1)

            board[row][col] = '.'
            cols.remove(col)
            main_diagonal.remove(diagonal_1)
            anti_diagonal.remove(diagonal_2)

    dfs(0)
    return solutions


assert dfs_n_queens_with_board(1) == [['Q']]
assert dfs_n_queens_with_board(2) == []
assert dfs_n_queens_with_board(3) == []

solutions = dfs_n_queens_with_board(4)

assert len(solutions) == 2
assert solutions[0] == ['.Q..', '...Q', 'Q...', '..Q.']
