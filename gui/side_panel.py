from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout

class SidePanel(QFrame):
    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setFixedWidth(250)
        self.side_panel_layout = QVBoxLayout()
        self.setStyleSheet("border: 2px solid black;")

        self.setObjectName("SidePanel")
        self.setStyleSheet("#SidePanel { border: 2px solid black; }")

        self.setLayout(self.side_panel_layout)