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

        # self.table = QTableWidget()
        # self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # self.table.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        # self.table.setFocus()
        # self.table.setFixedWidth(340)
        # self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # self.table.setRowCount(14)
        # self.table.setColumnCount(3)

        # self.table.horizontalHeader().setFixedHeight(30)

        # cell_height = self.table.verticalHeader().defaultSectionSize()
        # header_height = self.table.horizontalHeader().height()

        # self.table.setFixedHeight(2 + header_height + cell_height * 14)

        # # length
        # self.table.setItem(0, 0, QTableWidgetItem("GC Content"))
        # self.table.setItem(0, 1, QTableWidgetItem(get_gc_content(sequence_wt)))
        # self.table.setItem(0, 2, QTableWidgetItem(get_gc_content(sequence_mt)))

        # # gc content
        # self.table.setItem(1, 0, QTableWidgetItem("Length"))
        # self.table.setItem(1, 1, QTableWidgetItem(str(len(sequence_wt.replace('-', '')))))
        # self.table.setItem(1, 2, QTableWidgetItem(str(len(sequence_mt.replace('-', '')))))

        # # base proportions
        # self.table.setItem(2, 0, QTableWidgetItem("A"))
        # self.table.setItem(2, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'A')))
        # self.table.setItem(2, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'A')))
        # self.table.setItem(3, 0, QTableWidgetItem("T"))
        # self.table.setItem(3, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'T')))
        # self.table.setItem(3, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'T')))
        # self.table.setItem(4, 0, QTableWidgetItem("G"))
        # self.table.setItem(4, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'G')))
        # self.table.setItem(4, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'G')))
        # self.table.setItem(5, 0, QTableWidgetItem("C"))
        # self.table.setItem(5, 1, QTableWidgetItem(get_base_proportion(sequence_wt, 'C')))
        # self.table.setItem(5, 2, QTableWidgetItem(get_base_proportion(sequence_mt, 'C')))

        # # repeat content
        # self.table.setItem(6, 0, QTableWidgetItem("Repeat Content"))
        # self.table.setItem(6, 1, QTableWidgetItem(find_repeats(sequence_wt)))
        # self.table.setItem(6, 2, QTableWidgetItem(find_repeats(sequence_mt)))

        # # mutation types
        # if mutation:
        #     mutation_types = get_mutation_types(sequence_wt, sequence_mt)
        #     self.table.setItem(7, 0, QTableWidgetItem("Deletions"))
        #     self.table.item(7, 0).setToolTip("Click to highlight deletion mutations")
        #     self.table.setItem(7, 2, QTableWidgetItem(str(mutation_types['deletion'])))
        #     self.table.setItem(8, 0, QTableWidgetItem("Substitutions"))
        #     self.table.item(8, 0).setToolTip("Click to highlight substitution mutations")
        #     self.table.setItem(8, 2, QTableWidgetItem(str(mutation_types['substitution'])))
        #     self.table.setItem(9, 0, QTableWidgetItem("Insertions"))
        #     self.table.item(9, 0).setToolTip("Click to highlight insertion mutations")
        #     self.table.setItem(9, 2, QTableWidgetItem(str(mutation_types['insertion'])))
        #     self.table.cellClicked.connect(lambda row, column: 
        #                                    self.handle_cell_click(main_window, row, column,
        #                                                           sequence_wt, sequence_mt))

        # # colnames
        # self.table.setHorizontalHeaderLabels(['Summary', 'Reference', 'Mutated'])
        # font = QFont()
        # font.setBold(True)
        # font.setPointSize(14)

        # for col in range(self.table.columnCount()):
        #     item = self.table.horizontalHeaderItem(col)
        #     item.setFont(font)
        #     item.setBackground(QBrush(QColor("#383b42")))
        #     item.setForeground(QBrush(QColor("white")))

        # self.table.verticalHeader().setVisible(False)
        # self.table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        # self.table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

        # self.table.setAlternatingRowColors(True)
        # done table

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