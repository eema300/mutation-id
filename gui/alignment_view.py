from PyQt6.QtWidgets import (QApplication, QMainWindow, QStackedWidget, 
                            QHBoxLayout, QPushButton,
                            QWidget, QFrame)
from PyQt6.QtGui import QAction

from gui import SidePanel, ViewArea


class AlignmentView(QWidget):
    def __init__(self, sequence_1_aligned, sequence_2_aligned):
        super().__init__()

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()

        # view area
        self.view_are = ViewArea()
        