from PyQt6.Widgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

class SidePanel(QWidget):
    def __init__(self):
        super().__init__()

        side_panel_layout = QVBoxLayout()

    def update_side_panel(self, state):
        pass