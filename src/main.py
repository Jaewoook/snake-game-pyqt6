import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from game import Game


class SnakeGame(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake Game')
        self.game = Game()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.game)
        self.setLayout(self.layout)
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    game = SnakeGame()
    sys.exit(qApp.exec())

