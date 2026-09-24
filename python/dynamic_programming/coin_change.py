def coin_change(coins: list[int], amount: int) -> int:
    if amount < 0:
        raise ValueError('Amount must be non-negative.')

    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


assert coin_change([1], 0) == 0
assert coin_change([1, 3, 4], 6) == 2
assert coin_change([1, 5, 10], 12) == 3
assert coin_change([1, 2, 5], 11) == 3
assert coin_change([2, 1], 3) == 2
