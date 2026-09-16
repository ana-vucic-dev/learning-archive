def fibonacci_o1_space(n: int) -> int:
    if n < 0:
        raise ValueError('n must be a non-negative integer.')

    if n <= 1:
        return n

    num1, num2 = 0, 1

    for _ in range(2, n + 1):
        temp = num1 + num2
        num1 = num2
        num2 = temp

    return num2


assert fibonacci_o1_space(0) == 0
assert fibonacci_o1_space(1) == 1
assert fibonacci_o1_space(2) == 1
assert fibonacci_o1_space(3) == 2
assert fibonacci_o1_space(6) == 8
assert fibonacci_o1_space(10) == 55
assert fibonacci_o1_space(15) == 610
