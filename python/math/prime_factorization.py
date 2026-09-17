def prime_factorization(n: int) -> list[int]:
    if n <= 1:
        raise ValueError("Argument 'n' must be greater than 1.")

    if n <= 3:
        return [n]

    factors = []
    i = n

    while i % 2 == 0:
        factors.append(2)
        i //= 2

    while i % 3 == 0:
        factors.append(3)
        i //= 3

    divisor = 5
    step = 2

    while divisor * divisor <= i:
        while i % divisor == 0:
            factors.append(divisor)
            i //= divisor
        divisor += step
        step = 6 - step

    if i > 1:
        factors.append(i)

    return factors


assert prime_factorization(3) == [3]
assert prime_factorization(15) == [3, 5]
assert prime_factorization(20) == [2, 2, 5]
assert prime_factorization(360) == [2, 2, 2, 3, 3, 5]
assert prime_factorization(999) == [3, 3, 3, 37]
assert prime_factorization(1000) == [2, 2, 2, 5, 5, 5]
assert prime_factorization(1001) == [7, 11, 13]
