from typing import List
from PyQt6.QtWidgets import QWidget, QGridLayout
from .snake import *


class Map(QWidget):

    map_size: int
    map: List[List[int]]
    layout: QGridLayout

    def __init__(self, map_size):
        super().__init__()
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.map_size = map_size
        self.build_map()
        self.draw_map()
        self.setLayout(self.layout)

    def build_map(self):
        # self.board = [[] for _ in range(self.map_size)]
        self.map = []
        for y in range(0, self.map_size):
            # self.board[y] = [0 for _ in range(self.map_size)]
            self.map.append([])
            for x in range(0, self.map_size):
                if y == 0 or y == self.map_size - 1 or x == 0 or x == self.map_size - 1:
                    self.map[y].append(1)
                else:
                    self.map[y].append(0)

    def draw_map(self):
        for y in range(0, self.map_size):
            for x in range(0, self.map_size):
                if self.map[y][x] == 0:
                    block = QWidget()
                    block.setStyleSheet('background-color: #fff')
                    self.layout.addWidget(block, y, x)
                elif self.map[y][x] == 1:
                    block = QWidget()
                    block.setStyleSheet('background-color: #f00')
                    self.layout.addWidget(block, y, x)
