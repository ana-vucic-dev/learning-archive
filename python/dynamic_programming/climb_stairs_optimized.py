def climb_stairs_optimized(n: int) -> int:
    if n < 0:
        raise ValueError('The number of stairs must be non-negative.')

    if n <= 2:
        return n

    previous1 = 1
    previous2 = 2

    for _ in range(3, n + 1):
        current = previous1 + previous2
        previous1 = previous2
        previous2 = current

    return previous2


assert climb_stairs_optimized(2) == 2
assert climb_stairs_optimized(5) == 8
assert climb_stairs_optimized(7) == 21
assert climb_stairs_optimized(10) == 89
