def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("Argument 'n' must be a non-negative integer.")

    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


assert factorial_recursive(0) == 1
assert factorial_recursive(3) == 6
assert factorial_recursive(4) == 24
assert factorial_recursive(5) == 120
assert factorial_recursive(6) == 720
