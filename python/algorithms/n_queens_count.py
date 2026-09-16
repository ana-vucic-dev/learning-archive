def count_n_queens_solutions(n: int) -> int:
    """
    Count the number of solutions to the N-Queens problem
    for an `n` x `n` board using DFS with backtracking.
    """

    if n < 1 or n == 2 or n == 3:
        return 0

    if n == 1:
        return 1

    def dfs(
        row: int, cols: set[int], main_diagonal: set[int], anti_diagonal: set[int]
    ) -> int:
        if row == n:
            return 1

        count = 0

        for col in range(n):
            diagonal_1 = row - col + (n - 1)
            diagonal_2 = row + col

            if (
                col in cols
                or diagonal_1 in main_diagonal
                or diagonal_2 in anti_diagonal
            ):
                continue

            cols.add(col)
            main_diagonal.add(diagonal_1)
            anti_diagonal.add(diagonal_2)

            count += dfs(row + 1, cols, main_diagonal, anti_diagonal)

            cols.remove(col)
            main_diagonal.remove(diagonal_1)
            anti_diagonal.remove(diagonal_2)

        return count

    return dfs(0, set(), set(), set())


assert count_n_queens_solutions(1) == 1
assert count_n_queens_solutions(2) == 0
assert count_n_queens_solutions(3) == 0
assert count_n_queens_solutions(4) == 2
assert count_n_queens_solutions(5) == 10
assert count_n_queens_solutions(8) == 92
