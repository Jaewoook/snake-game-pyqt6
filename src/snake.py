from enum import Enum
from PyQt5.QtWidgets import QWidget
from utils import GameOverError


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3


class Snake(QWidget):

    direction = Direction.RIGHT
    length = 1

    def __init__(self):
        super().__init__()

    def reset(self):
        self.direction = Direction.RIGHT
        self.length = 1

    def grow(self):
        self.length += 1

    def shrink(self):
        if self.length == 1:
            raise GameOverError('Snake cannot be shrink anymore!')
        self.length -= 1
