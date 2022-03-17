import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class SnakeGame(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Snake Game')
        self.show()


if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    game = SnakeGame()
    sys.exit(qApp.exec())

