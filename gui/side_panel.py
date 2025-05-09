from PyQt6.QtWidgets import QFrame, QVBoxLayout, QWidget, QHBoxLayout

class SidePanel(QFrame):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(250)
        self.side_panel_layout = QVBoxLayout()
        self.side_panel_layout.setContentsMargins(15, 23, 15, 13)

        self.wt_widget = QWidget()
        self.mt_widget = QWidget()
        self.wt_widget_layout = QHBoxLayout()
        self.mt_widget_layout = QHBoxLayout()
        self.wt_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.mt_widget_layout.setContentsMargins(0, 0, 0, 0)

        self.side_panel_layout.addWidget(self.wt_widget)
        self.side_panel_layout.addWidget(self.mt_widget)

        self.setLayout(self.side_panel_layout)