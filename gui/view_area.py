from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QScrollArea)
from PyQt6.QtCore import Qt

class ViewArea(QScrollArea):
    def __init__(self):
        super().__init__()

        self.inner_widget = QWidget()
        self.inner_widget_layout = QVBoxLayout()
        self.inner_widget.setLayout(self.inner_widget_layout)

        self.setWidget(self.inner_widget)
        self.setWidgetResizable(True)