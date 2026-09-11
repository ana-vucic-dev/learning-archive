def square_root_bisection(
    num: float, tolerance: float = 1e-7, max_iterations: int = 100
) -> float:
    if num < 0:
        raise ValueError(
            'Square root of a negative number is not defined over the real numbers.'
        )

    if num == 0 or num == 1:
        return num

    left = 0
    right = max(1, num)

    for _ in range(max_iterations):
        middle = left + (right - left) / 2

        if right - left <= tolerance:
            return middle

        if middle < num / middle:
            left = middle
        else:
            right = middle

    raise RuntimeError(f'Failed to converge within {max_iterations} iterations.')


assert square_root_bisection(0) == 0
assert abs(square_root_bisection(0.001, 1e-7, 50) - 0.0316227766) < 1e-7
assert abs(square_root_bisection(0.25, 1e-7, 50) - 0.5) < 1e-7
assert abs(square_root_bisection(81, 1e-3, 50) - 9) < 1e-3

assert abs(square_root_bisection(225, 1e-3, 100) - 15) < 1e-3
assert abs(square_root_bisection(225, 1e-5, 100) - 15) < 1e-5
assert abs(square_root_bisection(225, 1e-7, 100) - 15) < 1e-7

try:
    square_root_bisection(225, 1e-7, 10)
except RuntimeError as error:
    assert str(error) == 'Failed to converge within 10 iterations.'
