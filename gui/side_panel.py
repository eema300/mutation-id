from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QHBoxLayout

class SidePanel(QFrame):
    def __init__(self):
        super().__init__()

        self.setFrameShape(QFrame.Shape.Box)
        self.setFixedWidth(250)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.side_panel_layout = QVBoxLayout()

        self.wt_widget = QWidget()
        self.mt_widget = QWidget()
        self.wt_widget_layout = QHBoxLayout()
        self.mt_widget_layout = QHBoxLayout()
        self.wt_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.mt_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.side_panel_layout.addWidget(self.wt_widget)
        self.side_panel_layout.addWidget(self.mt_widget)

        self.setLayout(self.side_panel_layout)