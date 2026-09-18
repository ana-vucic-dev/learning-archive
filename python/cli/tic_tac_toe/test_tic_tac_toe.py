from tic_tac_toe import (
    is_row_winner,
    is_column_winner,
    is_diagonal_winner,
    is_winner,
    make_board,
    render_board
)


assert is_column_winner([
    ['X', 'O', ' '],
    ['X', 'O', ' '],
    ['O', 'X', ' ']
]) is False


assert is_row_winner([
    ['X', ' ', 'X'],
    ['O', 'X', 'X'],
    ['O', 'O', 'O']
]) is True

assert is_column_winner([
    ['X', 'O', ' ', 'X'],
    [' ', 'O', 'X', 'O'],
    ['O', 'O', 'X', 'X'],
    ['O', 'O', 'X', ' '],
]) is True

assert is_diagonal_winner([
    ['O', 'X', 'O', 'X'],
    [' ', 'O', 'X', ' '],
    ['X', 'X', ' ', 'X'],
    ['X', ' ', 'O', 'O'],
]) is True

assert is_diagonal_winner([
        ['X', 'X', ' '],
        ['X', ' ', 'O'],
        [' ', 'O', 'O']
]) is False

assert is_winner([
    ['X', ' '],
    ['X', 'O']
]) is True

assert is_winner([
    ['X', ' ', 'X'],
    ['O', 'X', 'O'],
    ['O', 'O', 'O']
]) is True

assert is_winner([
    ['X', 'X', 'X', ' '],
    ['X', 'X', ' ', ' '],
    ['X', ' ', 'O', 'X'],
    [' ', ' ', 'O', 'X'],
]) is False

assert render_board([
    ['X', 'O', 'X'],
    ['O', ' ', ' '],
    [' ', 'X', 'O']
]) == """  1 2 3
1 X|O|X
  -+-+-
2 O| | 
  -+-+-
3  |X|O"""

board = make_board(3)

assert board == [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

board[1][1] = 'X'

assert board == [
    [' ', ' ', ' '],
    [' ', 'X', ' '],
    [' ', ' ', ' '],
]
