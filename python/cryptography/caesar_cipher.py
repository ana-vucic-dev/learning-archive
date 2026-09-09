def caesar_cipher(text: str, shift: int, encrypt: bool = True) -> str:
    if not isinstance(shift, int):
        return 'Shift must be an integer.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    if not encrypt:
        shift = -shift

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    translation_table = str.maketrans(
        alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text: str, shift: int) -> str:
    return caesar_cipher(text, shift)


def decrypt(text: str, shift: int) -> str:
    return caesar_cipher(text, shift, encrypt=False)


assert encrypt('hello world', 5) == 'mjqqt btwqi'
assert decrypt('Gus nby Zilwy vy qcnb sio', 20) == 'May the Force be with you'
