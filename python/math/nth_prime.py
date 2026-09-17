from is_prime import is_prime


def nth_prime(n: int) -> int:
    if n <= 0:
        raise ValueError("Argument 'n' must be a positive integer.")

    count = 0
    num = 1

    while count < n:
        num += 1

        if is_prime(num):
            count += 1

    return num


assert nth_prime(1) == 2
assert nth_prime(5) == 11
assert nth_prime(10) == 29
assert nth_prime(15) == 47
assert nth_prime(100) == 541
assert nth_prime(1000) == 7919
