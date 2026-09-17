def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(5) is True
assert is_prime(6) is False
assert is_prime(23) is True
assert is_prime(225) is False
