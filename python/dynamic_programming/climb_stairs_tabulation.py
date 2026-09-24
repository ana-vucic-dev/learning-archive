def climb_stairs_tabulation(n: int) -> int:
    if n < 0:
        raise ValueError('The number of stairs must be non-negative.')

    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


assert climb_stairs_tabulation(2) == 2
assert climb_stairs_tabulation(5) == 8
assert climb_stairs_tabulation(7) == 21
assert climb_stairs_tabulation(10) == 89
