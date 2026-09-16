def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('n must be a non-negative integer.')

    if n < 2:
        return n

    sequence = [0, 1]

    for i in range(2, n + 1):
        sequence.append(sequence[i - 1] + sequence[i - 2])

    return sequence[n]


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(6) == 8
assert fibonacci(10) == 55
assert fibonacci(15) == 610
