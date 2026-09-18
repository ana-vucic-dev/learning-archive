from typing import Literal


def is_winning_line(strings: list[list[str]]) -> bool:
    strings = set(strings)
    return len(strings) == 1 and ' ' not in strings


def is_row_winner(board: list[list[str]]) -> bool:
    return any(is_winning_line(row) for row in board)


def is_column_winner(board: list[list[str]]) -> bool:
    return is_row_winner(zip(*board))


def is_main_diagonal_winner(board: list[list[str]]) -> bool:
    return is_winning_line(row[i] for i, row in enumerate(board))


def is_diagonal_winner(board: list[list[str]]) -> bool:
    return is_main_diagonal_winner(board) or is_main_diagonal_winner(reversed(board))


def is_winner(board: list[list[str]]) -> bool:
    return is_row_winner(board) or is_column_winner(board) or is_diagonal_winner(board)


def print_winner(player: str) -> None:
    print(f'Player {player} wins!')


def print_draw() -> None:
    print("It's a draw!")


def get_board_size() -> int:
    while True:
        board_size = input('Enter board size (3-9): ')

        try:
            size = min(max(int(board_size), 3), 9)
            print(f'Making a {size}x{size} board.\n')
            return size
        except ValueError:
            print('Invalid input. Please enter a valid number.')


def make_board(size: int) -> list[list[str]]:
    return [[' '] * size for _ in range(size)]


def render_board(board: list[list[str]]) -> str:
    size = len(board)
    line = f'\n  {"+".join("-" * size)}\n'
    rows = [f'{i + 1} {"|".join(row)}' for i, row in enumerate(board)]
    return f'  {" ".join(str(i + 1) for i in range(size))}\n{line.join(rows)}'


def get_coordinate(prompt: str, max_value: int) -> int | Literal['quit']:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'q':
            return 'quit'

        try:
            value = int(user_input) - 1
            if 0 <= value < max_value:
                return value
            print(f'Out of bounds. Please enter a number between 1 and {max_value}.')
        except ValueError:
            print("Invalid input. Please enter a number or 'q'.")


def play_move(player: str, board_size: int) -> tuple[int, int] | None:
    print(f"\n{player}'s turn!\n")

    row = get_coordinate("Enter row number (or 'q' to quit): ", board_size)
    if row == 'quit':
        return None

    col = get_coordinate("Enter column number (or 'q' to quit): ", board_size)
    if col == 'quit':
        return None

    return (row, col)


def get_valid_move(board: list[list[str]], player: str) -> tuple[int, int] | None:
    while True:
        move = play_move(player, len(board))
        if move is None:
            return None

        row, col = move

        if board[row][col] == ' ':
            return row, col
        else:
            print(f'Row {row}, column {col} cell already occupied. Try again.')


def display_banner() -> None:
    print(f'{"=" * 52}')
    print(f'|{"Tic-Tac-Toe":^50}|')
    print(f'{"=" * 52}')


def display_description() -> None:
    print("""Take turns entering row and column numbers
to place a mark in the specified cell.
Type 'q' anytime to quit the game.\n""")


def start_game() -> None:
    while True:
        display_banner()
        display_description()
        board_size = get_board_size()
        board = make_board(board_size)
        print(render_board(board))
        moves = board_size * board_size
        game_over = False

        for turn in range(moves):
            current_player = 'X' if turn % 2 == 0 else 'O'

            move = get_valid_move(board, current_player)

            if move is None:
                print('Game over. Thanks for playing!')
                return

            row, col = move
            board[row][col] = current_player
            print('\n' + render_board(board) + '\n')

            if is_winner(board):
                print_winner(current_player)
                game_over = True
                break

        if not game_over:
            print_draw()

        play_again = input('\nPlay again? (y/n): ').strip().lower()
        if play_again != 'y':
            print('Thanks for playing!')
            break


start_game()
