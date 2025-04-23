from PyQt6.QtWidgets import QFrame, QHBoxLayout, QTableWidgetItem, QTableWidget, QAbstractItemView, QHeaderView
from PyQt6.QtCore import Qt
from logic import get_gc_content, get_base_proportion, find_repeats

class StatSummary(QFrame):
    def __init__(self, sequence_wt, sequence_mt):
        super().__init__()

        self.inner_widget_layout = QHBoxLayout()
        self.inner_widget_layout.setContentsMargins(10, 10, 10, 10)

        summary = QFrame()
        summary.setFixedWidth(370)
        summary.setFrameShape(QFrame.Shape.Box)
        summary.setFrameShadow(QFrame.Shadow.Sunken)
        summary.layout = QHBoxLayout()

        table = QTableWidget(summary)
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        table.setFixedWidth(340)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        table.setRowCount(15)
        table.setColumnCount(3)

        # length
        table.setItem(0, 0, QTableWidgetItem("GC Content"))
        table.setItem(0, 1, QTableWidgetItem(get_gc_content(sequence_wt)))
        table.setItem(0, 2, QTableWidgetItem(get_gc_content(sequence_mt)))

        # gc content
        table.setItem(1, 0, QTableWidgetItem("Length"))
        table.setItem(1, 1, QTableWidgetItem(str(len(sequence_wt.replace('-', '')))))
        table.setItem(1, 2, QTableWidgetItem(str(len(sequence_mt.replace('-', '')))))

        # base proportions
        table.setItem(2, 0, QTableWidgetItem("A"))
        table.setItem(2, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'A')))
        table.setItem(2, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'A')))
        table.setItem(3, 0, QTableWidgetItem("T"))
        table.setItem(3, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'T')))
        table.setItem(3, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'T')))
        table.setItem(4, 0, QTableWidgetItem("G"))
        table.setItem(4, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'G')))
        table.setItem(4, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'G')))
        table.setItem(5, 0, QTableWidgetItem("C"))
        table.setItem(5, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'C')))
        table.setItem(5, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'C')))

        # repeat content
        table.setItem(6, 0, QTableWidgetItem("Repeat Content"))
        table.setItem(6, 1, QTableWidgetItem(find_repeats(sequence_wt)))
        table.setItem(6, 2, QTableWidgetItem(find_repeats(sequence_mt)))

        # colnames
        table.setHorizontalHeaderLabels(['Summary', 'Wild Type', 'Mutated Type'])
        table.verticalHeader().setVisible(False)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        table.setAlternatingRowColors(True)

        summary.layout.addWidget(table)
        summary.setLayout(summary.layout)

        self.inner_widget_layout.addWidget(summary)
        self.inner_widget_layout.addStretch(1)
        self.setLayout(self.inner_widget_layout)




# retrieve the stat summary info from the csv