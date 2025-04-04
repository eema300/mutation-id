from PyQt6.QtWidgets import QFrame, QVBoxLayout

class SidePanel(QFrame):
    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.Shape.Box)
        self.setFixedWidth(250)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        self.side_panel_layout = QVBoxLayout()
        self.setLayout(self.side_panel_layout)