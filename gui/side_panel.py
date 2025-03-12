from PyQt6.QtWidgets import QWidget, QFrame, QVBoxLayout

class SidePanel(QWidget):
    def __init__(self):
        super().__init__()

        self.side_panel = QFrame()
        self.side_panel.setFrameShape(QFrame.Shape.StyledPanel)
        self.side_panel.setFixedWidth(250)
        self.side_panel_layout = QVBoxLayout()