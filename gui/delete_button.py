from PyQt6.QtWidgets import QPushButton


class DeleteButton(QPushButton):
    def __init__(self):
        super().__init__(' x ')