from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout

MENU_OPTIONS = ('PLAY', 'QUIT')


class Menu(QWidget):

    container: QVBoxLayout
    start_button: QPushButton
    quit_button: QPushButton

    def __init__(self):
        super().__init__()
        self.container = QVBoxLayout()
        self.start_button = QPushButton(MENU_OPTIONS[0])
        self.quit_button = QPushButton(MENU_OPTIONS[1])
        self.container.addWidget(self.start_button)
        self.container.addWidget(self.quit_button)
        self.show()
