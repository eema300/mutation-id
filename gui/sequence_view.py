# from PyQt6.QtCharts import QChartView
from PyQt6.QtWidgets import (QWidget, QHBoxLayout, QLabel)
from gui import SidePanel, ViewArea

class SequenceView(QWidget):
    def __init__(self, seqid_1, sequence_1,
                 seqid_2, sequence_2):
        super().__init__()

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()
        seqid_1_label = QLabel(seqid_1)
        seqid_2_label = QLabel(seqid_2)
        self.side_panel.side_panel_layout.addWidget(seqid_1_label)
        self.side_panel.side_panel_layout.addWidget(seqid_2_label)

        # view area
        self.view_area = ViewArea()
        sequence_1_label = QLabel(sequence_1)
        sequence_2_label = QLabel(sequence_2)
        self.view_area.view_area_layout.addWidget(sequence_1_label)
        self.view_area.view_area_layout.addWidget(sequence_2_label)