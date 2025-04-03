from PyQt6.QtWidgets import QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt

from .side_panel import SidePanel
from .view_area import ViewArea
from .sequence_design import SequenceDesign

class MutationView(QWidget):
    def __init__(self, main_window,
                 seqid_1, sequence_1_aligned, 
                 seqid_2, sequence_2_aligned):
        super().__init__()

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()
        seqid_1_label = QLabel(seqid_1)
        seqid_1_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        seqid_2_label = QLabel(seqid_2)
        seqid_2_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.side_panel.side_panel_layout.addWidget(seqid_1_label)
        self.side_panel.side_panel_layout.addWidget(seqid_2_label)
        self.side_panel.side_panel_layout.addStretch(1)
        self.side_panel.setLayout(self.side_panel.side_panel_layout)

        # view area
        # mutations need to be highlighted
        self.view_area = ViewArea()
        # sequence_1_label = QLabel(sequence_1_aligned)
        # sequence_2_label = QLabel(sequence_2_aligned)
        # self.view_area.inner_widget_layout.addWidget(sequence_1_label)
        # self.view_area.inner_widget_layout.addWidget(sequence_2_label)
        sequence_design = SequenceDesign(sequence_1=sequence_1_aligned,
                                         sequence_2=sequence_2_aligned)
        self.view_area.inner_widget_layout.addWidget(sequence_design)
        self.view_area.inner_widget_layout.addStretch(1)
        self.view_area.inner_widget.setLayout(self.view_area.inner_widget_layout)

        # add child widgets and set main layout
        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.view_area)
        self.setLayout(self.layout)