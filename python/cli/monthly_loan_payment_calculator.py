def display_banner() -> None:
    print(f'{"":=^54}')
    print(f'| {"Monthly Loan Payment Calculator":^50} |')
    print(f'{"":=^54}')
    print('Enter loan details to calculate monthly payments.\n')


def get_valid_input(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print('Invalid input. Please enter a number.')


def get_valid_integer(prompt: str) -> int:
    while True:
        user_input = input(prompt).strip()
        try:
            return int(user_input)
        except ValueError:
            print('Invalid input. Please enter a whole number.')


def calculate_monthly_payment(principal: float, apr: float, num_of_years: int) -> float:
    months = num_of_years * 12

    if apr == 0:
        return principal / months

    monthly_interest_rate = apr / 1200

    return (
        principal
        * monthly_interest_rate
        / (1 - (1 + monthly_interest_rate) ** (-months))
    )


def should_calculate_again() -> bool:
    while True:
        answer = input('\nCalculate again? (y/n): ').strip().lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Invalid input. Enter 'y' to calculate again or 'n' to exit.")


def monthly_loan_payment_calculator() -> None:
    display_banner()

    while True:
        principal = get_valid_input('\nLoan amount: ')
        apr = get_valid_input('Annual interest rate: ')
        years = get_valid_integer('Total repayment period in years: ')

        monthly_payment = calculate_monthly_payment(principal, apr, years)
        print(f'Monthly payment: ${monthly_payment:.2f}')

        if not should_calculate_again():
            print('Goodbye.')
            break


assert calculate_monthly_payment(12000, 0, 5) == 200
assert round(calculate_monthly_payment(10000, 6, 5), 2) == 193.33
assert round(calculate_monthly_payment(250000, 7.5, 30), 2) == 1748.04


monthly_loan_payment_calculator()
