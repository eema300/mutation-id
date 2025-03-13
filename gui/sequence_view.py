# from PyQt6.QtCharts import QChartView
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from .side_panel import SidePanel
from .view_area import ViewArea
from .view_caller import init_alignment_view


# if one is on, call that sub veiw
# if both on, call the normal view


class SequenceView(QWidget):
    def __init__(self, main_window, 
                 seqidWT, sequenceWT, WT_ON,
                 seqidMT, sequenceMT, MT_ON):
        super().__init__()

        # main layout
        self.layout = QHBoxLayout()

        # side panel
        self.side_panel = SidePanel()

        # if both on, load both sequences
        if WT_ON and MT_ON:
            # add seq ids, alignment button to side panel
            seqid_WT_label = QLabel(seqidWT)
            seqid_WT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            seqid_MT_label = QLabel(seqidMT)
            seqid_MT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.side_panel.side_panel_layout.addWidget(seqid_WT_label)
            self.side_panel.side_panel_layout.addWidget(seqid_MT_label)
            alignment_button = QPushButton("Align Sequences")
            alignment_button.clicked.connect(lambda: init_alignment_view(main_window))
            self.side_panel.side_panel_layout.addWidget(alignment_button)
            self.side_panel.side_panel_layout.addStretch(1)
            self.side_panel.setLayout(self.side_panel.side_panel_layout)

            # add sequences to view area
            self.view_area = ViewArea()
            sequence_WT_label = QLabel(sequenceWT)
            sequence_MT_label = QLabel(sequenceMT)
            self.view_area.inner_widget_layout.addWidget(sequence_WT_label)
            self.view_area.inner_widget_layout.addWidget(sequence_MT_label)
            self.view_area.inner_widget_layout.addStretch(1)
            self.view_area.inner_widget.setLayout(self.view_area.inner_widget_layout)

        # if WT on, load WT sequence, keep load MT button
        elif WT_ON and not MT_ON:
            from .view_caller import init_sequence_view_MT
            # add seq ids, alignment button to side panel
            seqid_WT_label = QLabel(seqidWT)
            seqid_WT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.side_panel.side_panel_layout.addWidget(seqid_WT_label)
            load_mutation_button = QPushButton("Load Mutated FASTA")
            load_mutation_button.clicked.connect(lambda: init_sequence_view_MT(main_window))
            self.side_panel.side_panel_layout.addWidget(load_mutation_button)
            self.side_panel.side_panel_layout.addStretch(1)
            self.side_panel.setLayout(self.side_panel.side_panel_layout)

            # add sequences to view area
            self.view_area = ViewArea()
            sequence_WT_label = QLabel(sequenceWT)
            self.view_area.inner_widget_layout.addWidget(sequence_WT_label)
            self.view_area.inner_widget_layout.addStretch(1)
            self.view_area.inner_widget.setLayout(self.view_area.inner_widget_layout)

        # if MT on, load MT sequence, keep load WT button
        elif MT_ON and not WT_ON:
            from .view_caller import init_sequence_view_WT
            # add seq ids, alignment button to side panel
            seqid_MT_label = QLabel(seqidMT)
            seqid_MT_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.side_panel.side_panel_layout.addWidget(seqid_MT_label)
            load_wt_button = QPushButton("Load Mutated FASTA")
            load_wt_button.clicked.connect(lambda: init_sequence_view_WT(main_window))
            self.side_panel.side_panel_layout.addWidget(load_wt_button)
            self.side_panel.side_panel_layout.addStretch(1)
            self.side_panel.setLayout(self.side_panel.side_panel_layout)

            # add sequences to view area
            self.view_area = ViewArea()
            sequence_MT_label = QLabel(sequenceMT)
            self.view_area.inner_widget_layout.addWidget(sequence_MT_label)
            self.view_area.inner_widget_layout.addStretch(1)
            self.view_area.inner_widget.setLayout(self.view_area.inner_widget_layout)

        else:
            print("something very bad happened!!!!!!!!!")

        # add child widgets and set main layout
        self.layout.addWidget(self.side_panel)
        self.layout.addWidget(self.view_area)
        self.setLayout(self.layout)
