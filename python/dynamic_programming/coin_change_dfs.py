def coin_change_dfs(coins: list[int], amount: int) -> int:
    if amount < 0:
        raise ValueError('Amount must be non-negative.')

    memo = {0: 0}

    def dfs(amount: int) -> int:
        if amount in memo:
            return memo[amount]

        result = float('inf')

        for coin in coins:
            if amount - coin >= 0:
                result = min(result, 1 + dfs(amount - coin))

        memo[amount] = result
        return result

    min_coins = dfs(amount)
    return min_coins if min_coins != float('inf') else -1


assert coin_change_dfs([1], 0) == 0
assert coin_change_dfs([1, 3, 4], 6) == 2
assert coin_change_dfs([1, 5, 10], 12) == 3
assert coin_change_dfs([1, 2, 5], 11) == 3
assert coin_change_dfs([2, 1], 3) == 2
