from collections import deque


def coin_change_bfs(coins: list[int], amount: int) -> int:
    if amount < 0:
        raise ValueError('Amount must be non-negative.')
    if amount == 0:
        return 0

    queue = deque([0])
    visited = [False] * (amount + 1)
    visited[0] = True
    min_coins = 0

    while queue:
        min_coins += 1

        for _ in range(len(queue)):
            current = queue.popleft()

            for coin in coins:
                next_amount = current + coin

                if next_amount == amount:
                    return min_coins

                if next_amount < amount and not visited[next_amount]:
                    visited[next_amount] = True
                    queue.append(next_amount)

    return -1


assert coin_change_bfs([1], 0) == 0
assert coin_change_bfs([1, 3, 4], 6) == 2
assert coin_change_bfs([1, 5, 10], 12) == 3
assert coin_change_bfs([1, 2, 5], 11) == 3
assert coin_change_bfs([2, 1], 3) == 2
