from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QWidget
from .graph_area import Graph_Area
from .table_widget import Table

class StatSummary(QWidget):
    def __init__(self, main_window, sequence_wt, sequence_mt, mutation, seqid_wt, seqid_mt):
        super().__init__()

        self.inner_widget_layout = QVBoxLayout()
        self.inner_widget_layout.setContentsMargins(5, 5, 5, 5)

        summary = QWidget()
        summary_layout = QHBoxLayout()
        summary_layout.setContentsMargins(0, 0, 5, 5)

        # table
        self.table = Table(main_window, mutation, sequence_wt, sequence_mt)

        # graph
        self.graph = Graph_Area(main_window, sequence_wt, sequence_mt, mutation, seqid_wt, seqid_mt)

        summary_layout.addWidget(self.table)
        summary_layout.addWidget(self.graph)
        summary_layout.addStretch(1)
        summary.setLayout(summary_layout)

        self.inner_widget_layout.addWidget(summary)
        self.inner_widget_layout.addStretch(1)
        self.setLayout(self.inner_widget_layout)