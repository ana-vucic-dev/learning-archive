def fibonacci_memoized(n: int, memo: dict[int, int] | None = None) -> int:
    if n < 0:
        raise ValueError('n must be a non-negative integer.')

    if memo is None:
        memo = {0: 0, 1: 1}

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


assert fibonacci_memoized(0) == 0
assert fibonacci_memoized(1) == 1
assert fibonacci_memoized(2) == 1
assert fibonacci_memoized(3) == 2
assert fibonacci_memoized(6) == 8
assert fibonacci_memoized(10) == 55
assert fibonacci_memoized(15) == 610
