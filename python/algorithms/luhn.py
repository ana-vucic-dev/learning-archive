def is_valid_card_number(card_number: str) -> bool:
    """
    Validate a string representing a card number
    using the Luhn algorithm.
    """

    clean_number = card_number.replace(' ', '').replace('-', '')

    if not clean_number.isdigit():
        return False

    total_sum = 0
    reversed_digits = clean_number[::-1]

    for i, num in enumerate(reversed_digits):
        digit = int(num)

        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9

        total_sum += digit

    return total_sum % 10 == 0


assert is_valid_card_number('79927398713') is True
assert is_valid_card_number('79927398710') is False
assert is_valid_card_number('453914889') is True
assert is_valid_card_number('453914881') is False
assert is_valid_card_number('4111-1111-1111-1111') is True
assert is_valid_card_number('1234 5678 9012 3456') is False
assert is_valid_card_number('4539 1488 0343 6467') is True
assert is_valid_card_number('4539-1488-0343-6468') is False
