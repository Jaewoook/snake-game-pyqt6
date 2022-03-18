from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QSizePolicy

MENU_OPTIONS = ('PLAY', 'QUIT')


class Menu(QWidget):

    # UI widgets
    layout: QVBoxLayout
    start_button: QPushButton
    quit_button: QPushButton

    # signals
    start = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.start_button = QPushButton(MENU_OPTIONS[0])
        self.quit_button = QPushButton(MENU_OPTIONS[1])
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.quit_button)

        self.start_button.clicked.connect(self.start.emit)
        self.quit_button.clicked.connect(self.on_quit_click)
        self.setLayout(self.layout)

    def on_quit_click(self):
        quit(0)
