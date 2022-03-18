import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QStackedLayout
from menu import Menu
from board import Map

MAP_SIZE = 30


class SnakeGame(QWidget):

    root_layout: QVBoxLayout
    content: QStackedLayout
    title: QLabel
    menu: Menu
    map: Map

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake Game')
        self.setGeometry(200, 200, 500, 500)

        self.root_layout = QVBoxLayout()
        self.content = QStackedLayout()

        self.title = QLabel('Snake Game')
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet('font-size: 20px;')
        self.root_layout.addWidget(self.title)

        self.menu = Menu()
        self.menu.start.connect(self.start_game)
        self.map = Map(MAP_SIZE)
        self.content.addWidget(self.menu)
        self.content.addWidget(self.map)
        self.root_layout.addLayout(self.content)

        self.setLayout(self.root_layout)
        self.show()

    def start_game(self):
        print('Starting the game..')
        self.content.setCurrentIndex(1)

    def reset_game(self):
        pass

    def quit_game(self):
        pass


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    game = SnakeGame()
    sys.exit(qApp.exec())
