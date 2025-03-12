from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout

class ViewArea(QWidget):
    def __init__(self):
        super().__init__()

        self.view_area = QFrame()
        self.view_area_layout = QVBoxLayout()