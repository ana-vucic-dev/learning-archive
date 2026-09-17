def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Argument 'n' must be a non-negative integer.")

    result = 1
    i = 1

    while i <= n:
        result *= i
        i += 1

    return result


assert factorial(0) == 1
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
