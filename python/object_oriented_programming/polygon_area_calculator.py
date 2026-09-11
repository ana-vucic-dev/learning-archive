from __future__ import annotations
from math import sqrt


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def set_width(self, value: float) -> None:
        self.width = abs(value)

    def set_height(self, value: float) -> None:
        self.height = abs(value)

    def get_area(self) -> float:
        return self.width * self.height

    def get_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def get_diagonal(self) -> float:
        return sqrt(pow(self.width, 2) + pow(self.height, 2))

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return 'Too big for a picture.'

        line = f'{self.width * "*"}\n'
        return f'{line * self.height}'

    def get_amount_inside(self, shape: Rectangle) -> float:
        """
        Return the ratio of this shape's area
        to the given shape's area.
        """

        this_area = self.get_area()
        shape_area = shape.get_area()

        if this_area == 0 or shape_area == 0:
            return 0
        return this_area / shape_area

    def __repr__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        super().__init__(side, side)

    def set_width(self, side: float) -> None:
        self.width = abs(side)
        self.height = abs(side)

    def set_height(self, side: float) -> None:
        self.height = abs(side)
        self.width = abs(side)

    def set_side(self, side: float) -> None:
        self.width = abs(side)
        self.height = abs(side)

    def __repr__(self) -> str:
        return f'Square(side={self.width})'


rectangle = Rectangle(10, 5)

assert rectangle.get_area() == 50
assert rectangle.get_perimeter() == 30
assert rectangle.get_diagonal() == sqrt(125)

rectangle.set_width(20)
assert rectangle.width == 20

rectangle.set_height(10)
assert rectangle.height == 10

square = Square(5)

assert square.get_area() == 25
assert square.get_perimeter() == 20
assert square.get_diagonal() == sqrt(50)

square.set_width(10)
assert square.width == 10
assert square.height == 10

square.set_height(15)
assert square.width == 15
assert square.height == 15

square.set_side(20)
assert square.width == 20
assert square.height == 20

assert Rectangle(10, 20).get_amount_inside(Square(5)) == 8
assert Rectangle(5.5, 10).get_amount_inside(Square(4.8)) == 2.3871527777777777
assert Square(25).get_amount_inside(Rectangle(5, 3.2)) == 39.0625
