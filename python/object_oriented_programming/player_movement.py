import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self) -> None:
        self.moves: list[tuple[int, int]] = []
        self.position = (0, 0)
        self.path = [self.position]

    def move(self) -> tuple[int, int]:
        x, y = random.choice(self.moves)
        new_position = (self.position[0] + x, self.position[1] + y)
        self.position = new_position
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self) -> None:
        pass


class Pawn(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def level_up(self) -> None:
        self.moves += [(1, -1), (1, 1), (-1, -1), (-1, 1)]


class Knight(Player):
    def __init__(self) -> None:
        super().__init__()
        self.moves = [
            (-2, -1),
            (-2, 1),
            (-1, -2),
            (-1, 2),
            (1, -2),
            (1, 2),
            (2, -1),
            (2, 1),
        ]

    def level_up(self) -> None:
        self.moves += [
            (-3, -1),
            (-3, 1),
            (-1, -3),
            (-1, 3),
            (1, -3),
            (1, 3),
            (3, -1),
            (3, 1),
        ]


pawn = Pawn()

assert pawn.position == (0, 0)
assert pawn.path == [(0, 0)]

pawn.move()

assert len(pawn.path) == 2
assert pawn.path[-1] == pawn.position

pawn.level_up()

assert len(pawn.moves) == 8

knight = Knight()
knight.move()
knight.move()

assert len(knight.path) == 3

knight.level_up()

assert len(knight.moves) == 16
