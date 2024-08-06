from __future__ import annotations

import enum
from collections import namedtuple
from typing import List


class Player(enum.Enum):
    BLACK = 1
    WHITE = 2

    @property
    def other(self) -> Player:
        return Player.BLACK if self == Player.WHITE else Player.WHITE


class Point(namedtuple("Point", "row col")):
    __slots__ = ()  # for optimization, prevents creation of __dict__

    row: int
    col: int

    def neighbors(self) -> List[Point]:
        row, col = self.row, self.col
        return [
            Point(row - 1, col),
            Point(row + 1, col),
            Point(row, col - 1),
            Point(row, col + 1),
        ]
