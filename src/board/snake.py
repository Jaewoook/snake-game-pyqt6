from enum import Enum
from PyQt6.QtWidgets import QWidget
from utils import GameOverError


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3


class SnakeHead(QWidget):

    direction = Direction.RIGHT
    length = 1

    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: rgb(0, 0, 255);')

    def reset(self):
        self.direction = Direction.RIGHT
        self.length = 1

    def grow(self):
        self.length += 1

    def shrink(self):
        if self.length == 1:
            raise GameOverError('Snake cannot be shrink anymore!')
        self.length -= 1


class SnakeBody(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: rgb(80, 80, 255);')


class SnakeTail(QWidget):

    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: rgb(0, 150, 255);')
