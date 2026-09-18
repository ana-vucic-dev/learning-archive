import secrets
import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = '!@#$%^&*'

characters = lowercase + uppercase + digits + special


def display_banner() -> None:
    print(f'{"":=^54}')
    print(f'| {"Random Password Generator":^50} |')
    print(f'{"":=^54}')
    print(
        'Get a random password of the specified length\nbetween 16 and 256 characters.\n'
    )


def get_password_length(prompt: str) -> int:
    while True:
        user_input = input(prompt)
        try:
            length = min(max(int(user_input), 16), 256)
            print(f'Generating a random password of length {length}...')
            return length
        except ValueError:
            print('Invalid input. Please enter a number between 16 and 256.')


def generate_password(length: int) -> str:
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special),
    ]

    password.extend(secrets.choice(characters) for _ in range(length - 4))
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


def run_password_generator() -> None:
    length = get_password_length('Enter password length (16-256): ')
    password = generate_password(length)
    print(f'Random password: {password}')


def should_generate_again() -> bool:
    while True:
        answer = input('\nGenerate another random password? (y/n): ')
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Invalid input. Enter 'y' to generate again or 'n' to exit.")


def password_generator() -> None:
    display_banner()
    while True:
        run_password_generator()
        if not should_generate_again():
            print('Goodbye.')
            break


assert len(generate_password(16)) == 16
assert len(generate_password(50)) == 50
assert len(generate_password(256)) == 256


password_generator()
