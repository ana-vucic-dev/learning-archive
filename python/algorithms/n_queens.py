def dfs_n_queens(n: int) -> list[list[int]]:
    """
    Find all solutions to the N-Queens problem
    for an `n` x `n` board using DFS with backtracking.

    Return each solution as a list of column indices,
    where the element at index `i` represents the column
    occupied by the Queen in row `i`.
    """

    if n < 1 or n == 2 or n == 3:
        return []

    if n == 1:
        return [[0]]

    solutions = []
    cols = set()
    main_diagonal = set()
    anti_diagonal = set()

    def dfs(row: int, solution: list[int]) -> None:
        if row == n:
            solutions.append(list(solution))
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

            solution.append(col)
            cols.add(col)
            main_diagonal.add(diagonal_1)
            anti_diagonal.add(diagonal_2)

            dfs(row + 1, solution)

            solution.pop()
            cols.remove(col)
            main_diagonal.remove(diagonal_1)
            anti_diagonal.remove(diagonal_2)

    dfs(0, [])
    return solutions


assert dfs_n_queens(1) == [[0]]
assert dfs_n_queens(2) == []
assert dfs_n_queens(3) == []
assert dfs_n_queens(4) == [[1, 3, 0, 2], [2, 0, 3, 1]]
assert len(dfs_n_queens(5)) == 10
assert len(dfs_n_queens(8)) == 92
