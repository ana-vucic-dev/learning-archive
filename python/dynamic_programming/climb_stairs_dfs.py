def climb_stairs_dfs(n: int) -> int:
    if n < 0:
        raise ValueError('The number of stairs must be non-negative.')

    memo = {0: 0, 1: 1, 2: 2}

    def dfs(num: int) -> int:
        if num in memo:
            return memo[num]

        memo[num] = dfs(num - 1) + dfs(num - 2)
        return memo[num]

    return dfs(n)


assert climb_stairs_dfs(2) == 2
assert climb_stairs_dfs(5) == 8
assert climb_stairs_dfs(7) == 21
assert climb_stairs_dfs(10) == 89
