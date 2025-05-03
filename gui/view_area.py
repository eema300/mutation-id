from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame, QWidget

class ViewArea(QFrame):
    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Sunken)

        self.inner_widget_layout = QVBoxLayout()
        self.inner_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.inner_widget_layout)