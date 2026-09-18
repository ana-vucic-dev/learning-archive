from decimal import Decimal, DecimalException
from typing import Literal


def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b


def subtract(a: Decimal, b: Decimal) -> Decimal:
    return a - b


def multiply(a: Decimal, b: Decimal) -> Decimal:
    return a * b


def divide(a: Decimal, b: Decimal) -> Decimal:
    return a / b


def parse_to_decimal(input_string: str) -> Decimal:
    """Parse a string input directly into a high-precision Decimal object."""
    return Decimal(input_string.strip())


def format_decimal(d: Decimal) -> str:
    """Format a Decimal to drop trailing zeros (`.0`) and prevent scientific notation."""
    normalized = d.normalize()
    _, _, exponent = normalized.as_tuple()

    if exponent >= 0:
        return f'{normalized:f}'

    return str(normalized)


def display_banner() -> None:
    print(f'{"=" * 52}')
    print(f'|{"Simple Calculator":^50}|')
    print(f'{"=" * 52}')


def display_description() -> None:
    print('Perform basic arithmetic operations on two numbers.\n')


def display_menu() -> None:
    print("""
Options:\n
  A, a             Perform addition
  S, s             Perform subtraction
  M, m             Perform multiplication
  D, d             Perform division
  help             Show this help menu
  E, e, Q, q       Exit/Quit program\n""")


def get_valid_input(prompt: str) -> Decimal | Literal['quit']:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'e' or user_input == 'q':
            return 'quit'

        try:
            return parse_to_decimal(user_input)
        except DecimalException:
            print('Invalid input. Please enter a number.')


def process_input() -> tuple[Decimal, Decimal] | None:
    a = get_valid_input('Enter first number: ')
    if a == 'quit':
        return None
    b = get_valid_input('Enter second number: ')
    if b == 'quit':
        return None
    return a, b


def handle_zero_division() -> Decimal | None:
    print('You cannot divide by zero.')
    b = get_valid_input('Enter a number greater than 0: ')
    if b == 'quit':
        return None
    return b


def run_calculator() -> None:
    display_banner()
    display_description()
    display_menu()

    while True:
        user_input = (input('Choose an option: ')).strip().lower()

        match user_input:
            case 'a':
                print('Addition\n')
                a, b = process_input()
                if a is None or b is None:
                    print('Exit\nGoodbye.')
                    return
                result = add(a, b)
                print(
                    f'{format_decimal(a)} + {format_decimal(b)} = {format_decimal(result)}'
                )
            case 's':
                print('Subtraction\n')
                a, b = process_input()
                if a is None or b is None:
                    print('Exit\nGoodbye.')
                    return
                result = subtract(a, b)
                print(
                    f'{format_decimal(a)} - {format_decimal(b)} = {format_decimal(result)}'
                )
            case 'm':
                print('Multiplication\n')
                a, b = process_input()
                if a is None or b is None:
                    print('Exit\nGoodbye.')
                    return
                result = multiply(a, b)
                print(
                    f'{format_decimal(a)} x {format_decimal(b)} = {format_decimal(result)}'
                )
            case 'd':
                print('Division\n')
                a, b = process_input()
                if a is None or b is None:
                    print('Exit\nGoodbye.')
                    return
                while b == 0:
                    b = handle_zero_division()
                if b is None:
                    print('Exit\nGoodbye.')
                    return
                result = divide(a, b)
                print(
                    f'{format_decimal(a)} / {format_decimal(b)} = {format_decimal(result)}'
                )
            case 'help':
                display_menu()
            case 'e' | 'q':
                print('Exit\nGoodbye.')
                return
            case _:
                print(f"Unknown option: {user_input}. Enter 'help' for menu.")


assert add(Decimal('2'), Decimal('3')) == Decimal('5')
assert subtract(Decimal('5'), Decimal('3')) == Decimal('2')
assert multiply(Decimal('2.5'), Decimal('4')) == Decimal('10')
assert divide(Decimal('10'), Decimal('4')) == Decimal('2.5')
assert add(Decimal('0.1'), Decimal('0.2')) == Decimal('0.3')

assert parse_to_decimal(' 12.50 ') == Decimal('12.50')

assert format_decimal(Decimal('5.0')) == '5'
assert format_decimal(Decimal('5.50')) == '5.5'
assert format_decimal(Decimal('10')) == '10'

run_calculator()
