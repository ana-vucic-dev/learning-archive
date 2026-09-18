def display_banner() -> None:
    print(f'{"":=^54}')
    print(f'| {"LEAP YEAR CHECKER":^50} |')
    print(f'{"":=^54}')
    print('Check if a year is a leap year.\n')


def get_year(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print('Invalid input. Year must be a whole number.')


def is_leap_year(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def should_check_again() -> bool:
    while True:
        user_input = input('\nCheck another year? (y/n): ').strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Enter 'y' to check another year or 'n' to exit.")


def leap_year_checker() -> None:
    display_banner()
    while True:
        year = get_year('Enter year: ')

        if is_leap_year(year):
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is not a leap year.')

        if not should_check_again():
            print('Goodbye.')
            break


assert is_leap_year(1400) is False
assert is_leap_year(1600) is True
assert is_leap_year(1700) is False
assert is_leap_year(2000) is True
assert is_leap_year(2024) is True
assert is_leap_year(2026) is False


leap_year_checker()
