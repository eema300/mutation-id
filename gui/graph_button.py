from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize


class GraphButton(QPushButton):
    def __init__(self, path, normal_icon_path, hover_icon_path):
        super().__init__()
        self.normal_image = QPixmap(f"{path}{normal_icon_path}")
        self.hover_image = QPixmap(f"{path}{hover_icon_path}")
        self.normal_icon = QIcon(self.normal_image)
        self.hover_icon = QIcon(self.hover_image)

        self.setIcon(self.normal_icon)
        self.setIconSize(QSize(20, 20))

        self.setObjectName("graph_button")

    def enterEvent(self, event):
        self.setIcon(self.hover_icon)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setIcon(self.normal_icon)
        super().leaveEvent(event)
