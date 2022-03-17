from PyQt5.QtWidgets import QWidget, QLabel

MENU_OPTIONS = ('PLAY', 'QUIT')


class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.show()
