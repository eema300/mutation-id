from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QFrame, QWidget

class ViewArea(QFrame):
    def __init__(self):
        super().__init__()

        self.inner_widget_layout = QVBoxLayout()
        self.inner_widget_layout.setContentsMargins(10, 10, 10, 10)

        self.setLayout(self.inner_widget_layout)